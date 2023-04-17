from pyokra.wrappers.income import AsyncIncome
from tests.mocked_api_call_testcase import MockedAPICallTestCase


class IncomeTestCase(MockedAPICallTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.wrapper = AsyncIncome(token=cls.token)

    async def test_wrapper_can_get_by_id(self):
        ...

    async def test_wrapper_can_get_by_customer(self):
        ...

    async def test_wrapper_can_get_by_date(self):
        ...

    async def test_wrapper_can_get_by_record(self):
        ...

    async def test_wrapper_can_all(self):
        ...

    async def test_wrapper_can_process(self):
        ...
