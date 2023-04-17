from pyokra.utils import APIResponse
from pyokra.wrappers.identity import Identity, AsyncIdentity
from tests.mocked_api_call_testcase import MockedAPICallTestCase
from httpx import codes as HTTP_STATUS_CODES


class IdentityTestCase(MockedAPICallTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.wrapper = AsyncIdentity(token=cls.token)

    async def test_wrapper_can_get_by_id(self):
        response = await self.wrapper.get_by_id(id="valid-id")
        self.assertIsNotNone(response)
        self.assertIsInstance(response, APIResponse)
        self.assertEqual(response.status_code, HTTP_STATUS_CODES.OK)

    async def test_wrapper_can_get_by_customer(self):
        response = await self.wrapper.get_by_customer(customer="valid-customer-id")
        self.assertIsNotNone(response)
        self.assertIsInstance(response, APIResponse)
        self.assertEqual(response.status_code, HTTP_STATUS_CODES.OK)

    async def test_wrapper_can_get_by_date(self):
        response = await self.wrapper.get_by_date(from_="2023-03-25", to="2023-04-29")
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

    async def test_wrapper_can_verify_bvn(self):
        response = await self.wrapper.verify_bvn(bvn="valid-bvn")
        self.assertIsNotNone(response)
        self.assertIsInstance(response, APIResponse)
        self.assertEqual(response.status_code, HTTP_STATUS_CODES.OK)

    async def test_wrapper_can_verify_bvn_bulk(self):
        response = await self.wrapper.verify_bvn_bulk(bvn_bulk=["valid-bvn"])
        self.assertIsNotNone(response)
        self.assertIsInstance(response, APIResponse)
        self.assertEqual(response.status_code, HTTP_STATUS_CODES.OK)

    async def test_wrapper_can_verify_nuban(self):
        response = await self.wrapper.verify_nuban(
            nuban="valid-nuban", bank="valid-bank"
        )
        self.assertIsNotNone(response)
        self.assertIsInstance(response, APIResponse)
        self.assertEqual(response.status_code, HTTP_STATUS_CODES.OK)

    async def test_wrapper_can_verify_nuban_name(self):
        response = await self.wrapper.verify_nuban_name(
            nuban="valid-nuban", bank="valid-bank"
        )
        self.assertIsNotNone(response)
        self.assertIsInstance(response, APIResponse)
        self.assertEqual(response.status_code, HTTP_STATUS_CODES.OK)
