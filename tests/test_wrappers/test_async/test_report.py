from pyokra.wrappers.report import AsyncReport
from tests.mocked_api_call_testcase import MockedAPICallTestCase


class ReportTestCase(MockedAPICallTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.wrapper = AsyncReport(token=cls.token)

    async def test_wrapper_can_get_schedule_reports(self):
        ...

    async def test_wrapper_can_schedule_report(self):
        ...

    async def test_wrapper_can_get_reports_list(self):
        ...

    async def test_wrapper_can_get_report_details_by_id(self):
        ...

    async def test_wrapper_can_delete_report(self):
        ...

    async def test_wrapper_can_download_report(self):
        ...

    async def test_wrapper_can_get_schedule_report_by_id(self):
        ...

    async def test_wrapper_can_update_schedule_report(self):
        ...

    async def test_wrapper_can_delete_schedule_report(self):
        ...
