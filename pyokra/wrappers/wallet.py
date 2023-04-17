from pyokra.base import BaseAPIWrapper, BaseAsyncAPIWrapper
from pyokra.utils import Currency, HTTPMethod


class Wallet(BaseAPIWrapper):
    def check_balance(self, currency=Currency.NGN):
        payload = {"currency": currency}
        return self._api_call(
            url=f"{self.base_url}/wallet/balance/check",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    def get(self, company: str, id: str):
        payload = {"company": company, "id": id}
        return self._api_call(
            url=f"{self.base_url}/wallet/get",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    def all(self, page: int, limit: int):
        payload = {"page": page, "limit": limit}
        return self._api_call(
            url=f"{self.base_url}/wallet/list",
            method=HTTPMethod.POST,
            json_data=payload,
        )


class AsyncWallet(BaseAsyncAPIWrapper):
    async def check_balance(self, currency=Currency.NGN):
        payload = {"currency": currency}
        return await self._api_call(
            url=f"{self.base_url}/wallet/balance/check",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    async def get(self, company: str, id: str):
        payload = {"company": company, "id": id}
        return await self._api_call(
            url=f"{self.base_url}/wallet/get",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    async def all(self, page: int, limit: int):
        payload = {"page": page, "limit": limit}
        return await self._api_call(
            url=f"{self.base_url}/wallet/list",
            method=HTTPMethod.POST,
            json_data=payload,
        )
