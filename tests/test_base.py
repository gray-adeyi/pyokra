from unittest import TestCase, IsolatedAsyncioTestCase

from pyokra.base import AbstractAPIWrapper, __version__
from pyokra.utils import ResponseType, HTTPMethod
from pyokra.exceptions import MissingTokenException

TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI2NjlkNDZiNC1mNDZjLTQ2ZjUtYWIwZC1kYzM4OWMwMTEzYTkiLCJpYXQiOjE2Nzg2Njk2MTEsIm5iZiI6MTY3ODY2OTYxMSwianRpIjoiMGQ1MjIwZTctNzQzZC00MmIzLWIxMDktZDg4ODIzODlkNWFiIiwiZXhwIjoxNjc4NjcwNTExLCJ0eXBlIjoiYWNjZXNzIiwiZnJlc2giOmZhbHNlfQ.Mpnohf_Blri0gJNVm-BIKtJAh6SCMo05ijyCobU4XjAb5Rdjpcsdjd1u9l1sLu891HFGOM9EDtBdiiCxvS4cbg"


class APIWrapper(AbstractAPIWrapper):
    ...


class APIWrapperTestCase(IsolatedAsyncioTestCase):
    async def test__api_call(self):
        ...


class APIWrapperSyncTestCase(TestCase):
    def test_wrapper_raises_exception_when_no_token_provided(self):
        with self.assertRaises(MissingTokenException) as error:
            APIWrapper()
        error_message = (
            "No token was provided! You can provide your Okra token on "
            "instantiation or as an environmental variable "
            f"{APIWrapper.ENV_TOKEN_NAME}=<your-okra-token>"
        )
        self.assertEqual(error.exception.args[0], error_message)

    def test_base_url(self):
        wrapper = APIWrapper(token="invalid-token")
        self.assertEqual(wrapper.base_url, "https://api.okra.ng/v2/sandbox")

    def test_headers(self):
        wrapper = APIWrapper(token="dummy-token")
        self.assertDictEqual(
            wrapper.headers,
            {
                "authorization": f"Bearer dummy-token",
                "accept": "application/json; charset=utf-8",
                "content-type": "application/json",
                "user-agent": f"PyOkra {__version__}",
            },
        )

    def test__api_call_sync(self):
        ...
