from pyokra.wrappers.payments import AsyncPayment
from tests.mocked_api_call_testcase import MockedAPICallTestCase


class PaymentTestCase(MockedAPICallTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.wrapper = AsyncPayment(token=cls.token)

    async def test_wrapper_can_create_payment_link(self):
        ...

    async def test_wrapper_can_initiate_payment(self):
        ...

    async def test_wrapper_can_all(self):
        ...

    async def test_wrapper_can_get_by_id(self):
        ...

    async def test_wrapper_can_initiate_future_payment(self):
        ...

    async def test_wrapper_can_cancel_future_payment(self):
        ...

    async def test_wrapper_can_reauthorize_future_payment(self):
        ...

    async def test_wrapper_can_all_payment_authorizations(self):
        ...

    async def test_wrapper_can_get_payments(self):
        ...

    async def test_wrapper_can_get_authorization_by_customer(self):
        ...

    async def test_wrapper_can_get_payments_by_options(self):
        ...

    async def test_wrapper_can_get_authorization_by_options(self):
        ...

    async def test_wrapper_can_bulk(self):
        ...
