from pyokra.wrappers.wallet import AsyncWallet
from tests.mocked_api_call_testcase import MockedAPICallTestCase


class WalletTestCase(MockedAPICallTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.wrapper = AsyncWallet(token=cls.token)

    async def test_wrapper_can_check_balance(self):
        ...

    async def test_wrapper_can_get(self):
        ...

    async def test_wrapper_can_all(self):
        ...
