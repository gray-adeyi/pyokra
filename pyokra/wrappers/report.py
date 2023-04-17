from pyokra.base import (
    BaseAPIWrapper,
    BaseAsyncAPIWrapper,
)
from pyokra.utils import FileType, WeekDay, HTTPMethod


class Report(BaseAPIWrapper):
    def get_schedule_reports(self):
        return self._api_call(
            url=f"{self.base_url}/reports/schedule",
            method=HTTPMethod.GET,
        )

    def schedule_report(
        self, title: str, report_type: str, day: WeekDay, file_format=FileType.CSV
    ):
        payload = {
            "report_type": report_type,
            "format": file_format,
            "title": title,
            "day": day,
        }
        return self._api_call(
            url=f"{self.base_url}/reports/schedule",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    def get_reports_list(self):
        return self._api_call(
            url=f"{self.base_url}/reports/details",
            method=HTTPMethod.GET,
        )

    def get_report_details_by_id(self, report_id: str):
        return self._api_call(
            url=f"{self.base_url}/reports/details/{report_id}",
            method=HTTPMethod.GET,
        )

    def delete_report(self, report_id: str):
        return self._api_call(
            url=f"{self.base_url}/reports/details/{report_id}",
            method=HTTPMethod.DELETE,
        )

    def download_report(self, report_id: str):
        return self._api_call(
            url=f"{self.base_url}/reports/download/{report_id}",
            method=HTTPMethod.GET,
        )

    def get_schedule_report_by_id(self, report_id: str):
        return self._api_call(
            url=f"{self.base_url}/reports/schedule/{report_id}",
            method=HTTPMethod.GET,
        )

    def update_schedule_report(self, report_id: str, update_data: dict):
        return self._api_call(
            url=f"{self.base_url}/reports/schedule/{report_id}",
            method=HTTPMethod.PUT,
            json_data=update_data,
        )

    def delete_schedule_report(self, report_id: str):
        return self._api_call(
            url=f"{self.base_url}/reports/schedule/{report_id}",
            method=HTTPMethod.DELETE,
        )


class AsyncReport(BaseAsyncAPIWrapper):
    async def get_schedule_reports(self):
        return await self._api_call(
            url=f"{self.base_url}/reports/schedule",
            method=HTTPMethod.GET,
        )

    async def schedule_report(
        self, title: str, report_type: str, day: WeekDay, file_format=FileType.CSV
    ):
        payload = {
            "report_type": report_type,
            "format": file_format,
            "title": title,
            "day": day,
        }
        return await self._api_call(
            url=f"{self.base_url}/reports/schedule",
            method=HTTPMethod.POST,
            form_data=payload,
        )

    async def get_reports_list(self):
        return await self._api_call(
            url=f"{self.base_url}/reports/details",
            method=HTTPMethod.GET,
        )

    async def get_report_details_by_id(self, report_id: str):
        return await self._api_call(
            url=f"{self.base_url}/reports/details/{report_id}",
            method=HTTPMethod.GET,
        )

    async def delete_report(self, report_id: str):
        return await self._api_call(
            url=f"{self.base_url}/reports/details/{report_id}",
            method=HTTPMethod.DELETE,
        )

    async def download_report(self, report_id: str):
        return await self._api_call(
            url=f"{self.base_url}/reports/download/{report_id}",
            method=HTTPMethod.GET,
        )

    async def get_schedule_report_by_id(self, report_id: str):
        return await self._api_call(
            url=f"{self.base_url}/reports/schedule/{report_id}",
            method=HTTPMethod.GET,
        )

    async def update_schedule_report(self, report_id: str, update_data: dict):
        return await self._api_call(
            url=f"{self.base_url}/reports/schedule/{report_id}",
            method=HTTPMethod.PUT,
            json_data=update_data,
        )

    async def delete_schedule_report(self, report_id: str):
        return await self._api_call(
            url=f"{self.base_url}/reports/schedule/{report_id}",
            method=HTTPMethod.DELETE,
        )
