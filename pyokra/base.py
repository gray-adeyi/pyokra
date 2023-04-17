import os
from abc import ABC
from io import BytesIO
from json import JSONDecodeError
from typing import Optional, Union
import httpx

from pyokra.exceptions import (
    MissingTokenException,
    UnsupportedHTTPMethodException,
    ConnectionException,
    InvalidResponseException,
)

__version__ = "0.1.0"
__author__ = "Gbenga <adeyigbenga005@gmail.com>"

from pyokra.utils import APIResponse, ResponseType, HTTPMethod, Mode


class AbstractAPIWrapper(ABC):
    ENV_TOKEN_NAME = "OKRA_TOKEN"

    def __init__(self, token: Optional[str] = None, mode: Mode = Mode.DEVELOPMENT):
        self.mode = mode
        self.token = token
        if not self.token:
            self.token = os.environ.get(self.ENV_TOKEN_NAME)
        if not self.token:
            raise MissingTokenException(
                "No token was provided! You can provide your Okra token on instantiation "
                f"or as an environmental variable {self.ENV_TOKEN_NAME}=<your-okra-token>"
            )

    @property
    def base_url(self):
        return {
            Mode.PRODUCTION: "https://api.okra.ng/v2",
            Mode.DEVELOPMENT: "https://api.okra.ng/v2/sandbox",
        }[self.mode]

    @property
    def headers(self):
        return {
            "authorization": f"Bearer {self.token}",
            "accept": "application/json; charset=utf-8",
            "content-type": "application/json",
            "user-agent": f"PyOkra {__version__}",
        }

    def _api_call(
        self,
        url: str,
        method: HTTPMethod,
        form_data: Optional[dict] = None,
        json_data: Optional[Union[list, dict]] = None,
        files: Optional[Union[dict[str, BytesIO], BytesIO, str]] = None,
        process_response_as=ResponseType.JSON,
    ) -> APIResponse:
        ...

    def _parse_call_kwargs(
        self,
        url: str,
        method: HTTPMethod,
        form_data: Optional[dict] = None,
        json_data: Optional[Union[list, dict]] = None,
        files: Optional[Union[dict[str, BytesIO], BytesIO, str]] = None,
    ) -> dict:
        if form_data and json_data:
            raise ValueError("You can't have both `form_data` and `json_data` set")
        http_method_call_kwargs = {
            "url": url,
            "data": form_data,
            "json": json_data,
            "headers": self.headers,
            "files": files,
        }
        if method in {HTTPMethod.GET, HTTPMethod.DELETE}:
            http_method_call_kwargs.pop("data", None)
            http_method_call_kwargs.pop("json", None)
            http_method_call_kwargs.pop("files", None)
        return http_method_call_kwargs

    def _parse_response(
        self, response: httpx.Response, process_response_as: ResponseType
    ) -> APIResponse:
        try:
            if process_response_as == ResponseType.JSON:
                response_body = response.json()
                return APIResponse(
                    status_code=response.status_code,
                    status=response_body.get("status"),
                    message=response_body.get("message"),
                    data=response_body.get("data"),
                    file=None,
                )
            if process_response_as == ResponseType.FILE:
                return APIResponse(
                    status_code=response.status_code,
                    status=None,
                    message=None,
                    data=None,
                    file=BytesIO(response.content),
                )
        except JSONDecodeError:
            raise InvalidResponseException(
                f"Unable to decode response. STATUS_CODE: {response.status_code}"
            )


class BaseAPIWrapper(AbstractAPIWrapper):
    def _api_call(
        self,
        url: str,
        method: HTTPMethod,
        form_data: Optional[dict] = None,
        json_data: Optional[Union[list, dict]] = None,
        files: Optional[Union[dict[str, BytesIO], BytesIO, str]] = None,
        process_response_as=ResponseType.JSON,
    ):
        http_method_call_kwargs = self._parse_call_kwargs(
            url=url,
            method=method,
            form_data=form_data,
            json_data=json_data,
            files=files,
        )
        http_methods_mapping = {
            HTTPMethod.GET: httpx.get,
            HTTPMethod.POST: httpx.post,
            HTTPMethod.PUT: httpx.put,
            HTTPMethod.PATCH: httpx.patch,
            HTTPMethod.DELETE: httpx.delete,
            HTTPMethod.OPTIONS: httpx.options,
            HTTPMethod.HEAD: httpx.head,
        }
        http_method_callable = http_methods_mapping.get(method)
        if not http_method_callable:
            raise UnsupportedHTTPMethodException(
                f"{method} is not a supported HTTP method"
            )
        try:
            response = http_method_callable(**http_method_call_kwargs)
        except httpx.ConnectError:
            raise ConnectionException(
                "Unable to connect to server. Please ensure you have an internet connection"
            )
        except httpx.ConnectTimeout:
            raise ConnectionException("Server refused to respond")
        return self._parse_response(response, process_response_as)


class BaseAsyncAPIWrapper(AbstractAPIWrapper):
    async def _api_call(
        self,
        url: str,
        method: HTTPMethod,
        json_data: Optional[Union[list, dict]] = None,
        form_data: Optional[dict] = None,
        files: Optional[Union[dict[str, BytesIO], BytesIO, str]] = None,
        process_response_as=ResponseType.JSON,
    ):
        http_method_call_kwargs = self._parse_call_kwargs(
            url=url,
            method=method,
            form_data=form_data,
            json_data=json_data,
            files=files,
        )
        async with httpx.AsyncClient() as client:
            http_method_callable = getattr(client, method.value.lower(), None)
            if not http_method_callable:
                raise UnsupportedHTTPMethodException(
                    f"{method} is not a supported HTTP method"
                )
            try:
                response = await http_method_callable(**http_method_call_kwargs)
            except httpx.ConnectError:
                raise ConnectionException(
                    "Unable to connect to server. Please ensure you have an internet connection"
                )
            except httpx.ConnectTimeout:
                raise ConnectionException("Server refused to respond")
            return self._parse_response(response, process_response_as)
