from pyokra.base import BaseAPIWrapper, BaseAsyncAPIWrapper
from pyokra.utils import HTTPMethod


class Balance(BaseAPIWrapper):
    def get_by_id(self, id: str, include_periodic: bool):
        payload = {"id": id, "includePeriodic": include_periodic}
        return self._api_call(
            url=f"{self.base_url}/balance/getById",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    def get_by_customer(
        self, customer: str, page: int, limit: int, include_periodic: bool
    ):
        payload = {
            "customer": customer,
            "page": page,
            "limit": limit,
            "includePeriodic": include_periodic,
        }
        return self._api_call(
            url=f"{self.base_url}/balance/getByCustomer",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    def get_by_account(
        self, account_id: str, page: int, limit: int, include_periodic: bool
    ):
        payload = {
            "account_id": account_id,
            "page": page,
            limit: int,
            "includePeriodic": include_periodic,
        }
        return self._api_call(
            url=f"{self.base_url}/balance/getByAccount",
            method=HTTPMethod.POST,
            form_data=payload,
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
            url=f"{self.base_url}/balance/getByCustomerDate",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    def get_by_date(
        self, from_: str, to: str, page: int, limit: int, include_periodic: bool
    ):
        payload = {
            "from": from_,
            "to": to,
            "page": page,
            "limit": limit,
            "includePeriodic": include_periodic,
        }
        return self._api_call(
            url=f"{self.base_url}/balance/getByDate",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    def get_by_options(self, tester_id: str):
        payload = {"options": {"tester_id": tester_id}}
        return self._api_call(
            url=f"{self.base_url}/balance/byOptions",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    def refresh(self, account_id: str):
        payload = {"account_id": account_id}
        return self._api_call(
            url=f"{self.base_url}/balance/refresh",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    def check(self, account_id: str, record_id: str):
        payload = {"account_id": account_id, "record_id": record_id}
        return self._api_call(
            url=f"{self.base_url}/balance/check",
            method=HTTPMethod.POST,
            json_data=payload,
        )


class AsyncBalance(BaseAsyncAPIWrapper):
    async def get_by_id(self, id: str, include_periodic: bool):
        payload = {"id": id, "includePeriodic": include_periodic}
        return await self._api_call(
            url=f"{self.base_url}/balance/getById",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    async def get_by_customer(
        self, customer: str, page: int, limit: int, include_periodic: bool
    ):
        payload = {
            "customer": customer,
            "page": page,
            "limit": limit,
            "includePeriodic": include_periodic,
        }
        return await self._api_call(
            url=f"{self.base_url}/balance/getByCustomer",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    async def get_by_account(
        self, account_id: str, page: int, limit: int, include_periodic: bool
    ):
        payload = {
            "account_id": account_id,
            "page": page,
            limit: int,
            "includePeriodic": include_periodic,
        }
        return await self._api_call(
            url=f"{self.base_url}/balance/getByAccount",
            method=HTTPMethod.POST,
            form_data=payload,
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
            url=f"{self.base_url}/balance/getByCustomerDate",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    async def get_by_date(
        self, from_: str, to: str, page: int, limit: int, include_periodic: bool
    ):
        payload = {
            "from": from_,
            "to": to,
            "page": page,
            "limit": limit,
            "includePeriodic": include_periodic,
        }
        return await self._api_call(
            url=f"{self.base_url}/balance/getByDate",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    async def get_by_options(self, tester_id: str):
        payload = {"options": {"tester_id": tester_id}}
        return await self._api_call(
            url=f"{self.base_url}/balance/byOptions",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    async def refresh(self, account_id: str):
        payload = {"account_id": account_id}
        return await self._api_call(
            url=f"{self.base_url}/balance/refresh",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    async def check(self, account_id: str, record_id: str):
        payload = {"account_id": account_id, "record_id": record_id}
        return await self._api_call(
            url=f"{self.base_url}/balance/check",
            method=HTTPMethod.POST,
            json_data=payload,
        )
