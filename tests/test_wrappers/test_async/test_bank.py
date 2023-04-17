from pyokra.utils import APIResponse
from pyokra.wrappers.bank import AsyncBank
from tests.mocked_api_call_testcase import MockedAPICallTestCase
from httpx import codes as HTTP_STATUS_CODES


class BankTestCase(MockedAPICallTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.wrapper = AsyncBank(token=cls.token)

    async def test_wrapper_can_all(self):
        response = await self.wrapper.all()
        self.assertIsNotNone(response)
        self.assertIsInstance(response, APIResponse)
        self.assertEqual(response.status_code, HTTP_STATUS_CODES.OK)

    async def test_wrapper_can_get_by_id(self):
        response = await self.wrapper.get_by_id()
        self.assertIsNotNone(response)
        self.assertIsInstance(response, APIResponse)
        self.assertEqual(response.status_code, HTTP_STATUS_CODES.OK)
