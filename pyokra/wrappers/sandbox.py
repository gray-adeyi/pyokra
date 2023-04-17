from pyokra.base import BaseAPIWrapper, BaseAsyncAPIWrapper
from pyokra.utils import SandboxCustomer, HTTPMethod


class Sandbox(BaseAPIWrapper):
    def create_customers(self, customers: list[SandboxCustomer]):
        payload = [customer.to_dict() for customer in customers]
        return self._api_call(
            url=f"{self.base_url}/sandbox/customers/create",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    def list_customers(self):
        return self._api_call(
            url=f"{self.base_url}/sandbox/customers/list",
            method=HTTPMethod.POST,
        )

    def view_customers(self, customer: str):
        payload = {"customer": customer}
        return self._api_call(
            url=f"{self.base_url}/sandbox/customers/get",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    def auto_generate(self, create: bool):
        payload = {"create": create}
        return self._api_call(
            url=f"{self.base_url}/sandbox/customers/generate",
            method=HTTPMethod.POST,
            json_data=payload,
        )


class AsyncSandbox(BaseAsyncAPIWrapper):
    async def create_customers(self, customers: list[SandboxCustomer]):
        payload = [customer.to_dict() for customer in customers]
        return await self._api_call(
            url=f"{self.base_url}/sandbox/customers/create",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    async def list_customers(self):
        return await self._api_call(
            url=f"{self.base_url}/sandbox/customers/list",
            method=HTTPMethod.POST,
        )

    async def view_customers(self, customer: str):
        payload = {"customer": customer}
        return await self._api_call(
            url=f"{self.base_url}/sandbox/customers/get",
            method=HTTPMethod.POST,
            json_data=payload,
        )

    async def auto_generate(self, create: bool):
        payload = {"create": create}
        return await self._api_call(
            url=f"{self.base_url}/sandbox/customers/generate",
            method=HTTPMethod.POST,
            json_data=payload,
        )
