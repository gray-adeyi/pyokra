from pyokra.utils import APIResponse
from tests.mocked_api_call_testcase import MockedAPICallTestCase
from httpx import codes as HTTP_STATUS_CODES
from pyokra.wrappers.account import AsyncAccount


# TODO: Find a better way to reduce the repetition in the tests
class AccountTestCase(MockedAPICallTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.wrapper = AsyncAccount(token=cls.token)

    async def test_wrapper_can_get_details(self):
        response = await self.wrapper.get_details(account="account-id")
        self.assertIsNotNone(response)
        self.assertIsInstance(response, APIResponse)
        self.assertEqual(response.status_code, HTTP_STATUS_CODES.OK)

    async def test_wrapper_can_get_by_id(self):
        response = await self.wrapper.get_by_id(id="valid-id")
        self.assertIsNotNone(response)
        self.assertIsInstance(response, APIResponse)
        self.assertEqual(response.status_code, HTTP_STATUS_CODES.OK)

    async def test_wrapper_can_get_by_customer(self):
        response = await self.wrapper.get_by_customer(customer="customer-id")
        self.assertIsNotNone(response)
        self.assertIsInstance(response, APIResponse)
        self.assertEqual(response.status_code, HTTP_STATUS_CODES.OK)

    async def test_wrapper_can_get_by_name(self):
        response = await self.wrapper.get_by_name(name="valid-name")
        self.assertIsNotNone(response)
        self.assertIsInstance(response, APIResponse)
        self.assertEqual(response.status_code, HTTP_STATUS_CODES.OK)

    async def test_wrapper_can_get_by_bank(self):
        response = await self.wrapper.get_by_bank(bank="valid-bank")
        self.assertIsNotNone(response)
        self.assertIsInstance(response, APIResponse)
        self.assertEqual(response.status_code, HTTP_STATUS_CODES.OK)

    async def test_wrapper_can_get_by_balance(self):
        response = await self.wrapper.get_by_balance(balance="valid-balance")
        self.assertIsNotNone(response)
        self.assertIsInstance(response, APIResponse)
        self.assertEqual(response.status_code, HTTP_STATUS_CODES.OK)

    async def test_wrapper_can_get_by_customer_date(self):
        response = await self.wrapper.get_by_customer_date(
            from_="2023-03-25", to="2023-04-29", customer="valid-customer-id"
        )
        self.assertIsNotNone(response)
        self.assertIsInstance(response, APIResponse)
        self.assertEqual(response.status_code, HTTP_STATUS_CODES.OK)
