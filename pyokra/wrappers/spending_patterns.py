from pyokra.base import BaseAPIWrapper, BaseAsyncAPIWrapper
from pyokra.utils import HTTPMethod


class SpendingPattern(BaseAPIWrapper):
    def process(self, customer_id: str):
        payload = {"customer_id": customer_id}
        return self._api_call(
            url=f"{self.base_url}/spending-patterns/process",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    def all(self, page: int, limit: int):
        payload = {"page": page, "limit": limit}
        return self._api_call(
            url=f"{self.base_url}/spending-patterns/getAll",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    def get_by_id(self, id: str):
        payload = {"id": id}
        return self._api_call(
            url=f"{self.base_url}/spending-patterns/getById",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    def get_by_customer_id(self, customer_id: str):
        payload = {"customer_id": customer_id}
        return self._api_call(
            url=f"{self.base_url}/spending-patterns/getByCustomer",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    def get_by_record(self, record: str, page: int, limit: int):
        payload = {"record": record, "page": page, "limit": limit}
        return self._api_call(
            url=f"{self.base_url}/spending-patterns/getByRecord",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    def get_by_date(self, from_: str, to: str, page: int, limit: int):
        payload = {"from": from_, "to": to, "page": page, "limit": limit}
        return self._api_call(
            url=f"{self.base_url}/spending-patterns/getByDate",
            method=HTTPMethod.POST,
            json_data=payload,
        )


class AsyncSpendingPattern(BaseAsyncAPIWrapper):
    async def process(self, customer_id: str):
        payload = {"customer_id": customer_id}
        return await self._api_call(
            url=f"{self.base_url}/spending-patterns/process",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    async def all(self, page: int, limit: int):
        payload = {"page": page, "limit": limit}
        return await self._api_call(
            url=f"{self.base_url}/spending-patterns/getAll",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    async def get_by_id(self, id: str):
        payload = {"id": id}
        return await self._api_call(
            url=f"{self.base_url}/spending-patterns/getById",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    async def get_by_customer_id(self, customer_id: str):
        payload = {"customer_id": customer_id}
        return await self._api_call(
            url=f"{self.base_url}/spending-patterns/getByCustomer",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    async def get_by_record(self, record: str, page: int, limit: int):
        payload = {"record": record, "page": page, "limit": limit}
        return await self._api_call(
            url=f"{self.base_url}/spending-patterns/getByRecord",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    async def get_by_date(self, from_: str, to: str, page: int, limit: int):
        payload = {"from": from_, "to": to, "page": page, "limit": limit}
        return await self._api_call(
            url=f"{self.base_url}/spending-patterns/getByDate",
            method=HTTPMethod.POST,
            json_data=payload,
        )
