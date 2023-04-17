from pyokra.base import BaseAPIWrapper, BaseAsyncAPIWrapper
from pyokra.utils import HTTPMethod


class Auth(BaseAPIWrapper):
    def get_by_id(self, id: str):
        payload = {"id": id}
        return self._api_call(
            url=f"{self.base_url}/auth/getById",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    def get_by_customer(self, customer: str, page: int, limit: int):
        payload = {"customer": customer, "page": page, "limit": limit}
        return self._api_call(
            url=f"{self.base_url}/auth/getByCustomer",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    def get_by_date(self, from_: str, to: str, page: int, limit: int):
        payload = {"from": from_, "to": to, "page": page, "limit": limit}
        return self._api_call(
            url=f"{self.base_url}/auth/getByDate",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    def get_by_bank(self, bank: str, page: int, limit: int):
        payload = {"bank": bank, "page": page, "limit": limit}
        return self._api_call(
            url=f"{self.base_url}/auth/getByBank",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    def get_by_customer_date(
        self, from_: str, to: str, customer: str, page: int, limit: int
    ):
        payload = {
            "from": from_,
            "to": to,
            "customer": customer,
            "page": page,
            "limit": limit,
        }
        return self._api_call(
            url=f"{self.base_url}/auth/getByCustomerDate",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    def get(self, page: int, limit: int):
        payload = {"page": page, "limit": limit}
        return self._api_call(
            url=f"{self.base_url}/products/auths",
            method=HTTPMethod.POST,
            json_data=payload,
        )


class AsyncAuth(BaseAsyncAPIWrapper):
    async def get_by_id(self, id: str):
        payload = {"id": id}
        return await self._api_call(
            url=f"{self.base_url}/auth/getById",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    async def get_by_customer(self, customer: str, page: int, limit: int):
        payload = {"customer": customer, "page": page, "limit": limit}
        return await self._api_call(
            url=f"{self.base_url}/auth/getByCustomer",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    async def get_by_date(self, from_: str, to: str, page: int, limit: int):
        payload = {"from": from_, "to": to, "page": page, "limit": limit}
        return await self._api_call(
            url=f"{self.base_url}/auth/getByDate",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    async def get_by_bank(self, bank: str, page: int, limit: int):
        payload = {"bank": bank, "page": page, "limit": limit}
        return await self._api_call(
            url=f"{self.base_url}/auth/getByBank",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    async def get_by_customer_date(
        self, from_: str, to: str, customer: str, page: int, limit: int
    ):
        payload = {
            "from": from_,
            "to": to,
            "customer": customer,
            "page": page,
            "limit": limit,
        }
        return await self._api_call(
            url=f"{self.base_url}/auth/getByCustomerDate",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    async def get(self, page: int, limit: int):
        payload = {"page": page, "limit": limit}
        return await self._api_call(
            url=f"{self.base_url}/products/auths",
            method=HTTPMethod.POST,
            json_data=payload,
        )
