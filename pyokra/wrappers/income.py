from typing import Optional

from pyokra.base import BaseAPIWrapper, BaseAsyncAPIWrapper
from pyokra.utils import APIVersion, HTTPMethod


class Income(BaseAPIWrapper):
    def get_by_id(self, id: str, version=APIVersion.V2):
        payload = {"id": id, "version": version}
        return self._api_call(
            url=f"{self.base_url}/income/getById",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    def get_by_customer(self, customer: str, version=APIVersion.V2):
        payload = {"customer": customer, "version": version}
        return self._api_call(
            url=f"{self.base_url}/income/getByCustomer",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    def get_by_date(self, from_: str, to: str, version=APIVersion.V2):
        payload = {"from": from_, "to": to, "version": version}
        return self._api_call(
            url=f"{self.base_url}/income/getByDate",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    def get_by_record(self, record: str, version=APIVersion.V2):
        payload = {"record": record, "version": version}
        return self._api_call(
            url=f"{self.base_url}/income/getByRecord",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    def all(self, page: str, limit: Optional[int] = 100, version=APIVersion.V2):
        payload = {"page": page, "limit": limit, "version": version}
        return self._api_call(
            url=f"{self.base_url}/income/getAll",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    def process(self, customer_id: str, version=APIVersion.V2):
        payload = {"customer_id": customer_id, "version": version}
        return self._api_call(
            url=f"{self.base_url}/income/process",
            method=HTTPMethod.POST,
            json_data=payload,
        )


class AsyncIncome(BaseAsyncAPIWrapper):
    async def get_by_id(self, id: str, version=APIVersion.V2):
        payload = {"id": id, "version": version}
        return await self._api_call(
            url=f"{self.base_url}/income/getById",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    async def get_by_customer(self, customer: str, version=APIVersion.V2):
        payload = {"customer": customer, "version": version}
        return await self._api_call(
            url=f"{self.base_url}/income/getByCustomer",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    async def get_by_date(self, from_: str, to: str, version=APIVersion.V2):
        payload = {"from": from_, "to": to, "version": version}
        return await self._api_call(
            url=f"{self.base_url}/income/getByDate",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    async def get_by_record(self, record: str, version=APIVersion.V2):
        payload = {"record": record, "version": version}
        return await self._api_call(
            url=f"{self.base_url}/income/getByRecord",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    async def all(self, page: str, limit: Optional[int] = 100, version=APIVersion.V2):
        payload = {"page": page, "limit": limit, "version": version}
        return await self._api_call(
            url=f"{self.base_url}/income/getAll",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    async def process(self, customer_id: str, version=APIVersion.V2):
        payload = {"customer_id": customer_id, "version": version}
        return await self._api_call(
            url=f"{self.base_url}/income/process",
            method=HTTPMethod.POST,
            json_data=payload,
        )
