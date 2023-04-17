from pyokra.wrappers.sandbox import AsyncSandbox
from tests.mocked_api_call_testcase import MockedAPICallTestCase


class SandboxTestCase(MockedAPICallTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.wrapper = AsyncSandbox(token=cls.token)

    async def test_wrapper_can_create_customers(self):
        ...

    async def test_wrapper_can_list_customers(self):
        ...

    async def test_wrapper_can_view_customers(self):
        ...

    async def test_wrapper_can_auto_generate(self):
        ...
