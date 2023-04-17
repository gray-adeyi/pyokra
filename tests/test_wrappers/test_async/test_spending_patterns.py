from pyokra.wrappers.spending_patterns import AsyncSpendingPattern
from tests.mocked_api_call_testcase import MockedAPICallTestCase


class SpendingPatternTestCase(MockedAPICallTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.wrapper = AsyncSpendingPattern(token=cls.token)

    async def test_wrapper_can_process(self):
        ...

    async def test_wrapper_can_all(self):
        ...

    async def test_wrapper_can_get_by_id(self):
        ...

    async def test_wrapper_can_get_by_customer_id(self):
        ...

    async def test_wrapper_can_get_by_record(self):
        ...

    async def test_wrapper_can_get_by_date(self):
        ...
