from pyokra.base import BaseAPIWrapper, BaseAsyncAPIWrapper
from pyokra.utils import HTTPMethod


class Identity(BaseAPIWrapper):
    def get_by_id(self, id: str):
        payload = {"id": id}
        return self._api_call(
            url=f"{self.base_url}/identity/getById",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    def get_by_customer(self, customer: str):
        payload = {"customer": customer}
        return self._api_call(
            url=f"{self.base_url}/identity/getByCustomer",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    def get_by_date(self, from_: str, to: str):
        payload = {"from": from_, "to": str}
        return self._api_call(
            url=f"{self.base_url}/identity/getByDate",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    def get_by_customer_date(self, from_: str, to: str, customer: int):
        payload = {"from": from_, "to": str, "customer": int}
        return self._api_call(
            url=f"{self.base_url}/identity/getByCustomerDate",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    def verify_bvn(self, bvn: str):
        payload = {"bvn": bvn}
        return self._api_call(
            url=f"{self.base_url}/products/kyc/bvn-verify",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    def verify_bvn_bulk(self, bvn_bulk: list):
        payload = {"bvn": ", ".join(bvn_bulk)}
        return self._api_call(
            url=f"{self.base_url}/products/kyc/bulk-bvn-verify",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    def verify_nuban(self, nuban: str, bank: str):
        payload = {"nuban": nuban, "bank": bank}
        return self._api_call(
            url=f"{self.base_url}/products/kyc/nuban-verify",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    def verify_nuban_name(self, nuban: str, bank: str):
        payload = {"nuban": nuban, "bank": bank}
        return self._api_call(
            url=f"{self.base_url}/products/kyc/nuban-name-verify",
            method=HTTPMethod.POST,
            form_data=payload,
        )


class AsyncIdentity(BaseAsyncAPIWrapper):
    async def get_by_id(self, id: str):
        payload = {"id": id}
        return await self._api_call(
            url=f"{self.base_url}/identity/getById",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    async def get_by_customer(self, customer: str):
        payload = {"customer": customer}
        return await self._api_call(
            url=f"{self.base_url}/identity/getByCustomer",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    async def get_by_date(self, from_: str, to: str):
        payload = {"from": from_, "to": str}
        return await self._api_call(
            url=f"{self.base_url}/identity/getByDate",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    async def get_by_customer_date(self, from_: str, to: str, customer: str):
        payload = {"from": from_, "to": str, "customer": customer}
        return await self._api_call(
            url=f"{self.base_url}/identity/getByCustomerDate",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    async def verify_bvn(self, bvn: str):
        payload = {"bvn": bvn}
        return await self._api_call(
            url=f"{self.base_url}/products/kyc/bvn-verify",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    async def verify_bvn_bulk(self, bvn_bulk: list):
        payload = {"bvn": ", ".join(bvn_bulk)}
        return await self._api_call(
            url=f"{self.base_url}/products/kyc/bulk-bvn-verify",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    async def verify_nuban(self, nuban: str, bank: str):
        payload = {"nuban": nuban, "bank": bank}
        return await self._api_call(
            url=f"{self.base_url}/products/kyc/nuban-verify",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    async def verify_nuban_name(self, nuban: str, bank: str):
        payload = {"nuban": nuban, "bank": bank}
        return await self._api_call(
            url=f"{self.base_url}/products/kyc/nuban-name-verify",
            method=HTTPMethod.POST,
            form_data=payload,
        )
