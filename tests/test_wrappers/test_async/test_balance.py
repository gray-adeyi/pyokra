from pyokra.utils import APIResponse
from pyokra.wrappers.balance import AsyncBalance
from tests.mocked_api_call_testcase import MockedAPICallTestCase
from httpx import codes as HTTP_STATUS_CODES


class BalanceTestCase(MockedAPICallTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.wrapper = AsyncBalance(token=cls.token)

    async def test_wrapper_can_get_by_id(self):
        response = await self.wrapper.get_by_id(id="valid-id", include_periodic=True)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, APIResponse)
        self.assertEqual(response.status_code, HTTP_STATUS_CODES.OK)

    async def test_wrapper_can_get_by_customer(self):
        response = await self.wrapper.get_by_customer(
            customer="valid-customer-id", page=1, limit=50, include_periodic=False
        )
        self.assertIsNotNone(response)
        self.assertIsInstance(response, APIResponse)
        self.assertEqual(response.status_code, HTTP_STATUS_CODES.OK)

    async def test_wrapper_can_get_by_account(self):
        response = await self.wrapper.get_by_account(
            account_id="valid-account-id", page=1, limit=50, include_periodic=False
        )
        self.assertIsNotNone(response)
        self.assertIsInstance(response, APIResponse)
        self.assertEqual(response.status_code, HTTP_STATUS_CODES.OK)

    async def test_wrapper_can_get_by_customer_date(self):
        response = await self.wrapper.get_by_customer_date(
            from_="2023-03-25",
            to="2023-04-29",
            page=1,
            limit=50,
            customer="valid-customer-id",
        )
        self.assertIsNotNone(response)
        self.assertIsInstance(response, APIResponse)
        self.assertEqual(response.status_code, HTTP_STATUS_CODES.OK)

    async def test_wrapper_can_get_by_date(self):
        response = await self.wrapper.get_by_date(
            from_="2023-03-25", to="2023-04-29", page=1, limit=50, include_periodic=True
        )
        self.assertIsNotNone(response)
        self.assertIsInstance(response, APIResponse)
        self.assertEqual(response.status_code, HTTP_STATUS_CODES.OK)

    async def test_wrapper_can_get_by_options(self):
        response = await self.wrapper.get_by_options(tester_id="valid-tester-id")
        self.assertIsNotNone(response)
        self.assertIsInstance(response, APIResponse)
        self.assertEqual(response.status_code, HTTP_STATUS_CODES.OK)

    async def test_wrapper_can_refresh(self):
        response = await self.wrapper.refresh(account_id="valid-account-id")
        self.assertIsNotNone(response)
        self.assertIsInstance(response, APIResponse)
        self.assertEqual(response.status_code, HTTP_STATUS_CODES.OK)

    async def test_wrapper_can_check(self):
        response = await self.wrapper.check(
            account_id="valid-account-id", record_id="valid-record-id"
        )
        self.assertIsNotNone(response)
        self.assertIsInstance(response, APIResponse)
        self.assertEqual(response.status_code, HTTP_STATUS_CODES.OK)
