from pyokra.base import BaseAPIWrapper, BaseAsyncAPIWrapper
from pyokra.utils import HTTPMethod


class Bank(BaseAPIWrapper):
    def all(self):
        return self._api_call(
            url=f"{self.base_url}/banks/list",
            method=HTTPMethod.GET,
        )

    def get_by_id(self):
        return self._api_call(
            url=f"{self.base_url}/banks/getById",
            method=HTTPMethod.GET,
        )


class AsyncBank(BaseAsyncAPIWrapper):
    async def all(self):
        return await self._api_call(
            url=f"{self.base_url}/banks/list",
            method=HTTPMethod.GET,
        )

    async def get_by_id(self):
        return await self._api_call(
            url=f"{self.base_url}/banks/getById",
            method=HTTPMethod.GET,
        )
