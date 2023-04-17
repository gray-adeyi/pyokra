from io import BytesIO
from typing import Optional

from pyokra.base import (
    BaseAPIWrapper,
    BaseAsyncAPIWrapper,
)
from pyokra.utils import Currency, Country, HTTPMethod


class Payment(BaseAPIWrapper):
    def create_payment_link(
        self,
        amount: int,
        name: str,
        account: str,
        country=Country.NG,
        currency=Currency.NGN,
        note: Optional[str] = None,
    ):
        payload = {
            "amount": amount,
            "name": name,
            "currency": currency,
            "note": note,
            "countries": country,
            "account": account,
        }
        return self._api_call(
            url=f"{self.base_url}/pay/link/create",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    def initiate_payment(
        self,
        account_to_debit: str,
        account_to_credit,
        amount: int,
        currency=Currency.NGN,
    ):
        payload = {
            "account_to_debit": account_to_debit,
            "account_to_credit": account_to_credit,
            "amount": amount,
            "currency": currency,
        }
        return self._api_call(
            url=f"{self.base_url}/pay/initiate",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    def all(self, payment_id: str):
        payload = {"payment_id": payment_id}
        return self._api_call(
            url=f"{self.base_url}/pay/list",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    def get_by_id(self, payment_id: str):
        payload = {"payment_id": payment_id}
        return self._api_call(
            url=f"{self.base_url}/pay/get/id",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    def initiate_future_payment(
        self,
        authorization: str,
        amount: int,
        initial_amount,
        start_date: str,
        end_date: str,
        currency=Currency.NGN,
    ):
        payload = {
            "authorization": authorization,
            "amount": amount,
            "initialAmount": initial_amount,
            "currency": currency,
            "startDate": start_date,
            "endDate": end_date,
        }
        return self._api_call(
            url=f"{self.base_url}/pay/authorization/initiate",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    def cancel_future_payment(self, authorization: str, customer: str, link: str):
        payload = {"authorization": authorization, "customer": customer, "link": link}
        return self._api_call(
            url=f"{self.base_url}/pay/authorization/cancel",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    def reauthorize_future_payment(
        self, authorization: str, customer: str, link: str, account: str
    ):
        payload = {
            "authorization": authorization,
            "customer": customer,
            "link": link,
            "account": account,
        }
        return self._api_call(
            url=f"{self.base_url}/pay/authorization/reauth",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    def all_payment_authorizations(self, page: int):
        payload = {"page": page}
        return self._api_call(
            url=f"{self.base_url}/pay/authorization/list",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    def get_payments(self):
        return self._api_call(
            url=f"{self.base_url}/pay/get",
            method=HTTPMethod.POST,
            json_data=None,
        )

    def get_authorization_by_customer(self, reference: str):
        payload = {"options": {"reference": reference}}
        return self._api_call(
            url=f"{self.base_url}/pay/authorization/getByCustomer",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    def get_payments_by_options(self, options: str, page: int, limit: int):
        payload = {"options": options, "page": page, "limit": limit}
        return self._api_call(
            url=f"{self.base_url}/pay/verifyByOptions",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    def get_authorization_by_options(self, reference: str):
        payload = {"options": {"reference": reference}}
        return self._api_call(
            url=f"{self.base_url}/pay/authorization/getByOptions",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    def bulk(self, file: BytesIO, product: str):
        files = {"file": file}
        payload = {"product": product}
        return self._api_call(
            url=f"{self.base_url}/bulkfiles/initiate",
            method=HTTPMethod.POST,
            form_data=payload,
            files=files,
        )


class AsyncPayment(BaseAsyncAPIWrapper):
    async def create_payment_link(
        self,
        amount: int,
        name: str,
        account: str,
        country=Country.NG,
        currency=Currency.NGN,
        note: Optional[str] = None,
    ):
        payload = {
            "amount": amount,
            "name": name,
            "currency": currency,
            "note": note,
            "countries": country,
            "account": account,
        }
        return await self._api_call(
            url=f"{self.base_url}/pay/link/create",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    async def initiate_payment(
        self,
        account_to_debit: str,
        account_to_credit,
        amount: int,
        currency=Currency.NGN,
    ):
        payload = {
            "account_to_debit": account_to_debit,
            "account_to_credit": account_to_credit,
            "amount": amount,
            "currency": currency,
        }
        return await self._api_call(
            url=f"{self.base_url}/pay/initiate",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    async def all(self, payment_id: str):
        payload = {"payment_id": payment_id}
        return await self._api_call(
            url=f"{self.base_url}/pay/list",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    async def get_by_id(self, payment_id: str):
        payload = {"payment_id": payment_id}
        return await self._api_call(
            url=f"{self.base_url}/pay/get/id",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    async def initiate_future_payment(
        self,
        authorization: str,
        amount: int,
        initial_amount,
        start_date: str,
        end_date: str,
        currency=Currency.NGN,
    ):
        payload = {
            "authorization": authorization,
            "amount": amount,
            "initialAmount": initial_amount,
            "currency": currency,
            "startDate": start_date,
            "endDate": end_date,
        }
        return await self._api_call(
            url=f"{self.base_url}/pay/authorization/initiate",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    async def cancel_future_payment(self, authorization: str, customer: str, link: str):
        payload = {"authorization": authorization, "customer": customer, "link": link}
        return await self._api_call(
            url=f"{self.base_url}/pay/authorization/cancel",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    async def reauthorize_future_payment(
        self, authorization: str, customer: str, link: str, account: str
    ):
        payload = {
            "authorization": authorization,
            "customer": customer,
            "link": link,
            "account": account,
        }
        return await self._api_call(
            url=f"{self.base_url}/pay/authorization/reauth",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    async def all_payment_authorizations(self, page: int):
        payload = {"page": page}
        return await self._api_call(
            url=f"{self.base_url}/pay/authorization/list",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    async def get_payments(self):
        return await self._api_call(
            url=f"{self.base_url}/pay/get",
            method=HTTPMethod.POST,
            json_data=None,
        )

    async def get_authorization_by_customer(self, reference: str):
        payload = {"options": {"reference": reference}}
        return await self._api_call(
            url=f"{self.base_url}/pay/authorization/getByCustomer",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    async def get_payments_by_options(self, options: str, page: int, limit: int):
        payload = {"options": options, "page": page, "limit": limit}
        return await self._api_call(
            url=f"{self.base_url}/pay/verifyByOptions",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    async def get_authorization_by_options(self, reference: str):
        payload = {"options": {"reference": reference}}
        return await self._api_call(
            url=f"{self.base_url}/pay/authorization/getByOptions",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    async def bulk(self, file: BytesIO, product: str):
        files = {"file": file}
        payload = {"product": product}
        return await self._api_call(
            url=f"{self.base_url}/bulkfiles/initiate",
            method=HTTPMethod.POST,
            form_data=payload,
            files=files,
        )
