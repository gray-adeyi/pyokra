from pyokra.base import BaseAPIWrapper, BaseAsyncAPIWrapper
from pyokra.utils import HTTPMethod


class Customer(BaseAPIWrapper):
    def all(self, page: int, limit: int):
        payload = {"page": page, "limit": limit}
        return self._api_call(
            url=f"{self.base_url}/customers/list",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    def get_by(self, key: str, value: str):
        payload = {"key": key, "value": value}
        return self._api_call(
            url=f"{self.base_url}/customers/find-customers-by",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    def flag(self, bank: str, customer: str):
        payload = {"bank": bank, "customer": customer}
        return self._api_call(
            url=f"{self.base_url}/customers/flag",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    def unflag(self, bank: str, customer: str, unflag: bool):
        payload = {"bank": bank, "customer": customer, "unflag": unflag}
        return self._api_call(
            url=f"{self.base_url}/customers/unflag",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    def remove(self, customer: str):
        payload = {"customer": customer}
        return self._api_call(
            url=f"{self.base_url}/customers/remove",
            method=HTTPMethod.POST,
            json_data=payload,
        )


class AsyncCustomer(BaseAsyncAPIWrapper):
    async def all(self, page: int, limit: int):
        payload = {"page": page, "limit": limit}
        return await self._api_call(
            url=f"{self.base_url}/customers/list",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    async def get_by(self, key: str, value: str):
        payload = {"key": key, "value": value}
        return await self._api_call(
            url=f"{self.base_url}/customers/find-customers-by",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    async def flag(self, bank: str, customer: str):
        payload = {"bank": bank, "customer": customer}
        return await self._api_call(
            url=f"{self.base_url}/customers/flag",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    async def unflag(self, bank: str, customer: str, unflag: bool):
        payload = {"bank": bank, "customer": customer, "unflag": unflag}
        return await self._api_call(
            url=f"{self.base_url}/customers/unflag",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    async def remove(self, customer: str):
        payload = {"customer": customer}
        return await self._api_call(
            url=f"{self.base_url}/customers/remove",
            method=HTTPMethod.POST,
            json_data=payload,
        )
