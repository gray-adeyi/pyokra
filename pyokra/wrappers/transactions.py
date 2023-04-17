from pyokra.base import BaseAPIWrapper, BaseAsyncAPIWrapper
from pyokra.utils import ResponseType, HTTPMethod


class Transaction(BaseAPIWrapper):
    def get_by_id(self, id: str):
        payload = {"id": id}
        return self._api_call(
            url=f"{self.base_url}/transactions/getById",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    def get_by_customer(self, customer: str, page: int, limit: int):
        payload = {"customer": customer, "page": page, "limit": limit}
        return self._api_call(
            url=f"{self.base_url}/transactions/getByCustomer",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    def get_by_account(self, account: str, page: int, limit: int):
        payload = {"account": account, "page": page, "limit": limit}
        return self._api_call(
            url=f"{self.base_url}/transactions/getByAccount",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    def get_by_bank(self, bank: str, page: int, limit: int):
        payload = {"bank": bank, "page": page, "limit": limit}
        return self._api_call(
            url=f"{self.base_url}/transactions/getByBank",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    def get_by_date(self, from_: str, to: str, page: int, limit: int):
        payload = {"from": from_, "to": to, "page": page, "limit": limit}
        return self._api_call(
            url=f"{self.base_url}/transactions/getByDate",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    def get_by_customer_date(
        self, from_: str, to: str, page: int, limit: int, customer_id: str
    ):
        payload = {
            "from": from_,
            "to": to,
            "page": page,
            "limit": limit,
            "customer_id": customer_id,
        }
        return self._api_call(
            url=f"{self.base_url}/transactions/getByCustomerDate",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    def get_by_nuban(self, nuban: str, page: int, limit: int):
        payload = {"nuban": nuban, "page": page, "limit": limit}
        return self._api_call(
            url=f"{self.base_url}/transactions/getByNuban",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    def get_by_options(self, first_name: str, last_name: str):
        payload = {"options": {"first_name": first_name, "last_name": last_name}}
        return self._api_call(
            url=f"{self.base_url}/transactions/byOptions",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    def enhanced(self, account: str, page: int, limit: int):
        payload = {"account": account, "page": page, "limit": limit}
        return self._api_call(
            url=f"{self.base_url}/transactions/process",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    def refresh(self, account_id: str):
        payload = {"account_id": account_id}
        return self._api_call(
            url=f"{self.base_url}/transactions/refresh",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    def download_transactions(self, record: str, download_type="csv"):
        payload = {"record": record, "downloadType": download_type}
        return self._api_call(
            url=f"{self.base_url}/transactions/download",
            method=HTTPMethod.POST,
            form_data=payload,
            process_response_as=ResponseType.FILE,
        )

    def download_records(self, download_type="csv"):
        payload = {"downloadType": download_type}
        return self._api_call(
            url=f"{self.base_url}/products/record/download",
            method=HTTPMethod.POST,
            form_data=payload,
            process_response_as=ResponseType.FILE,
        )


class AsyncTransaction(BaseAsyncAPIWrapper):
    async def get_by_id(self, id: str):
        payload = {"id": id}
        return await self._api_call(
            url=f"{self.base_url}/transactions/getById",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    async def get_by_customer(self, customer: str, page: int, limit: int):
        payload = {"customer": customer, "page": page, "limit": limit}
        return await self._api_call(
            url=f"{self.base_url}/transactions/getByCustomer",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    async def get_by_account(self, account: str, page: int, limit: int):
        payload = {"account": account, "page": page, "limit": limit}
        return await self._api_call(
            url=f"{self.base_url}/transactions/getByAccount",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    async def get_by_bank(self, bank: str, page: int, limit: int):
        payload = {"bank": bank, "page": page, "limit": limit}
        return await self._api_call(
            url=f"{self.base_url}/transactions/getByBank",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    async def get_by_date(self, from_: str, to: str, page: int, limit: int):
        payload = {"from": from_, "to": to, "page": page, "limit": limit}
        return await self._api_call(
            url=f"{self.base_url}/transactions/getByDate",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    async def get_by_customer_date(
        self, from_: str, to: str, page: int, limit: int, customer_id: str
    ):
        payload = {
            "from": from_,
            "to": to,
            "page": page,
            "limit": limit,
            "customer_id": customer_id,
        }
        return await self._api_call(
            url=f"{self.base_url}/transactions/getByCustomerDate",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    async def get_by_nuban(self, nuban: str, page: int, limit: int):
        payload = {"nuban": nuban, "page": page, "limit": limit}
        return await self._api_call(
            url=f"{self.base_url}/transactions/getByNuban",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    async def get_by_options(self, first_name: str, last_name: str):
        payload = {"options": {"first_name": first_name, "last_name": last_name}}
        return await self._api_call(
            url=f"{self.base_url}/transactions/byOptions",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    async def enhanced(self, account: str, page: int, limit: int):
        payload = {"account": account, "page": page, "limit": limit}
        return await self._api_call(
            url=f"{self.base_url}/transactions/process",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    async def refresh(self, account_id: str):
        payload = {"account_id": account_id}
        return await self._api_call(
            url=f"{self.base_url}/transactions/refresh",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    async def download_transactions(self, record: str, download_type="csv"):
        payload = {"record": record, "downloadType": download_type}
        return await self._api_call(
            url=f"{self.base_url}/transactions/download",
            method=HTTPMethod.POST,
            form_data=payload,
            process_response_as=ResponseType.FILE,
        )

    async def download_records(self, download_type="csv"):
        payload = {"downloadType": download_type}
        return await self._api_call(
            url=f"{self.base_url}/products/record/download",
            method=HTTPMethod.POST,
            form_data=payload,
            process_response_as=ResponseType.FILE,
        )
