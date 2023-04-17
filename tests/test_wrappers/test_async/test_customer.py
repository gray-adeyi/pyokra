from httpx import codes as HTTP_STATUS_CODES

from pyokra.utils import APIResponse
from pyokra.wrappers.customer import AsyncCustomer
from tests.mocked_api_call_testcase import MockedAPICallTestCase


class CustomerTestCase(MockedAPICallTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.wrapper = AsyncCustomer(token=cls.token)

    async def test_wrapper_can_all(self):
        response = await self.wrapper.all(page=1, limit=50)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, APIResponse)
        self.assertEqual(response.status_code, HTTP_STATUS_CODES.OK)

    async def test_wrapper_can_get_by(self):
        response = await self.wrapper.get_by(key="valid-key", value="valid-value")
        self.assertIsNotNone(response)
        self.assertIsInstance(response, APIResponse)
        self.assertEqual(response.status_code, HTTP_STATUS_CODES.OK)

    async def test_wrapper_can_flag(self):
        response = await self.wrapper.flag(
            bank="valid-bank-id", customer="valid-customer-id"
        )
        self.assertIsNotNone(response)
        self.assertIsInstance(response, APIResponse)
        self.assertEqual(response.status_code, HTTP_STATUS_CODES.OK)

    async def test_wrapper_can_unflag(self):
        response = await self.wrapper.unflag(
            bank="valid-bank-id", customer="valid-customer-id", unflag=True
        )
        self.assertIsNotNone(response)
        self.assertIsInstance(response, APIResponse)
        self.assertEqual(response.status_code, HTTP_STATUS_CODES.OK)

    async def test_wrapper_can_remove(self):
        response = await self.wrapper.remove(customer="valid-customer-id")
        self.assertIsNotNone(response)
        self.assertIsInstance(response, APIResponse)
        self.assertEqual(response.status_code, HTTP_STATUS_CODES.OK)
