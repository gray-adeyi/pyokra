from pyokra.base import BaseAPIWrapper, BaseAsyncAPIWrapper
from pyokra.utils import HTTPMethod


class Account(BaseAPIWrapper):
    def get_details(self, account: str):
        payload = {"account": account}
        return self._api_call(
            url=f"{self.base_url}/accounts/getAccountDetails",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    def get_by_id(self, id: str):
        payload = {"id": id}
        return self._api_call(
            url=f"{self.base_url}/accounts/getById",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    def get_by_customer(self, customer: str):
        payload = {"customer": customer}
        return self._api_call(
            url=f"{self.base_url}/accounts/getByCustomer",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    def get_by_name(self, name: str):
        payload = {"name": name}
        return self._api_call(
            url=f"{self.base_url}/accounts/getByName",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    def get_by_bank(self, bank: str):
        payload = {"bank": bank}
        return self._api_call(
            url=f"{self.base_url}/accounts/getByBank",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    def get_by_balance(self, balance: str):
        payload = {"balance": balance}
        return self._api_call(
            url=f"{self.base_url}/accounts/getByBalance",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    def get_by_customer_date(self, from_: str, to: str, customer: str):
        payload = {"from": from_, "to": to, "customer": customer}
        return self._api_call(
            url=f"{self.base_url}/accounts/getByCustomerDate",
            method=HTTPMethod.POST,
            form_data=payload,
        )


class AsyncAccount(BaseAsyncAPIWrapper):
    async def get_details(self, account: str):
        payload = {"account": account}
        return await self._api_call(
            url=f"{self.base_url}/accounts/getAccountDetails",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    async def get_by_id(self, id: str):
        payload = {"id": id}
        return await self._api_call(
            url=f"{self.base_url}/accounts/getById",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    async def get_by_customer(self, customer: str):
        payload = {"customer": customer}
        return await self._api_call(
            url=f"{self.base_url}/accounts/getByCustomer",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    async def get_by_name(self, name: str):
        payload = {"name": name}
        return await self._api_call(
            url=f"{self.base_url}/accounts/getByName",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    async def get_by_bank(self, bank: str):
        payload = {"bank": bank}
        return await self._api_call(
            url=f"{self.base_url}/accounts/getByBank",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    async def get_by_balance(self, balance: str):
        payload = {"balance": balance}
        return await self._api_call(
            url=f"{self.base_url}/accounts/getByBalance",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    async def get_by_customer_date(self, from_: str, to: str, customer: str):
        payload = {"from": from_, "to": to, "customer": customer}
        return await self._api_call(
            url=f"{self.base_url}/accounts/getByCustomerDate",
            method=HTTPMethod.POST,
            form_data=payload,
        )
