from pyokra.utils import APIResponse
from pyokra.wrappers.auth import AsyncAuth
from tests.mocked_api_call_testcase import MockedAPICallTestCase
from httpx import codes as HTTP_STATUS_CODES


class AuthTestCase(MockedAPICallTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.wrapper = AsyncAuth(token=cls.token)

    async def test_wrapper_can_get_by_id(self):
        response = await self.wrapper.get_by_id(id="valid-id")
        self.assertIsNotNone(response)
        self.assertIsInstance(response, APIResponse)
        self.assertEqual(response.status_code, HTTP_STATUS_CODES.OK)

    async def test_wrapper_can_get_by_customer(self):
        response = await self.wrapper.get_by_customer(
            customer="valid-customer-id", page=1, limit=50
        )
        self.assertIsNotNone(response)
        self.assertIsInstance(response, APIResponse)
        self.assertEqual(response.status_code, HTTP_STATUS_CODES.OK)

    async def test_wrapper_can_get_by_date(self):
        response = await self.wrapper.get_by_date(
            from_="2023-03-25", to="2023-04-29", page=1, limit=50
        )
        self.assertIsNotNone(response)
        self.assertIsInstance(response, APIResponse)
        self.assertEqual(response.status_code, HTTP_STATUS_CODES.OK)

    async def test_wrapper_can_get_by_bank(self):
        response = await self.wrapper.get_by_bank(bank="valid-bank", page=1, limit=50)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, APIResponse)
        self.assertEqual(response.status_code, HTTP_STATUS_CODES.OK)

    async def test_wrapper_can_get_by_customer_date(self):
        response = await self.wrapper.get_by_customer_date(
            from_="2023-03-25",
            to="2023-04-29",
            page=1,
            limit=50,
            customer="valid-cutomer-id",
        )
        self.assertIsNotNone(response)
        self.assertIsInstance(response, APIResponse)
        self.assertEqual(response.status_code, HTTP_STATUS_CODES.OK)

    async def test_wrapper_can_get(self):
        response = await self.wrapper.get(page=1, limit=50)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, APIResponse)
        self.assertEqual(response.status_code, HTTP_STATUS_CODES.OK)
