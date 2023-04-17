from pyokra.wrappers.transactions import Transaction, AsyncTransaction
from tests.mocked_api_call_testcase import MockedAPICallTestCase


class TransactionTestCase(MockedAPICallTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.wrapper = AsyncTransaction(token=cls.token)

    async def test_wrapper_can_get_by_id(self):
        ...

    async def test_wrapper_can_get_by_customer(self):
        ...

    async def test_wrapper_can_get_by_account(self):
        ...

    async def test_wrapper_can_get_by_bank(self):
        ...

    async def test_wrapper_can_get_by_date(self):
        ...

    async def test_wrapper_can_get_by_customer_date(self):
        ...

    async def test_wrapper_can_get_by_nuban(self):
        ...

    async def test_wrapper_can_get_by_options(self):
        ...

    async def test_wrapper_can_enhanced(self):
        ...

    async def test_wrapper_can_refresh(self):
        ...

    async def test_wrapper_can_download_transactions(self):
        ...

    async def test_wrapper_can_download_records(self):
        ...
