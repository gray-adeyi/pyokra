from io import BytesIO
from unittest import IsolatedAsyncioTestCase, TestCase
from unittest.mock import patch, Mock, MagicMock

from pyokra.utils import APIResponse


class TestDummyData:
    @classmethod
    def setUpClass(cls) -> None:
        cls.token = "dummy-token"
        cls.mocked_api_response = Mock(spec="httpx.Response")
        cls.mocked_api_response.status_code = 200
        cls.mocked_api_response.json = Mock()
        cls.mocked_api_response.json.return_value = {
            "status": "successful",
            "message": "This is a mocked response. No real API call to Okra servers was made.",
            "data": {"isValid": True},
            "content": b"s/n,name,user\n1,Gbenga,Superuser",
        }


class MockedAPICallTestCase(TestDummyData, IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        get_patcher = patch("httpx._client.AsyncClient.get")
        post_patcher = patch("httpx._client.AsyncClient.post")
        put_patcher = patch("httpx._client.AsyncClient.put")
        patch_patcher = patch("httpx._client.AsyncClient.patch")
        delete_patcher = patch("httpx._client.AsyncClient.delete")
        options_patcher = patch("httpx._client.AsyncClient.options")
        head_patcher = patch("httpx._client.AsyncClient.head")

        mock_get = get_patcher.start()
        mock_get.return_value = cls.mocked_api_response

        mock_post = post_patcher.start()
        mock_post.return_value = cls.mocked_api_response

        mock_put = put_patcher.start()
        mock_put.return_value = cls.mocked_api_response

        mock_patch = patch_patcher.start()
        mock_patch.return_value = cls.mocked_api_response

        mock_delete = delete_patcher.start()
        mock_delete.return_value = cls.mocked_api_response

        mock_options = options_patcher.start()
        mock_options.return_value = cls.mocked_api_response

        mock_head = head_patcher.start()
        mock_head.return_value = cls.mocked_api_response


class MockedAPICallSyncTestCase(TestDummyData, TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        get_patcher = patch("httpx.get")
        post_patcher = patch("httpx.post")
        put_patcher = patch("httpx.put")
        patch_patcher = patch("httpx.patch")
        delete_patcher = patch("httpx.delete")
        options_patcher = patch("httpx.options")
        head_patcher = patch("httpx.head")

        mock_get = get_patcher.start()
        mock_get.return_value = cls.mocked_api_response

        mock_post = post_patcher.start()
        mock_post.return_value = cls.mocked_api_response

        mock_put = put_patcher.start()
        mock_put.return_value = cls.mocked_api_response

        mock_patch = patch_patcher.start()
        mock_patch.return_value = cls.mocked_api_response

        mock_delete = delete_patcher.start()
        mock_delete.return_value = cls.mocked_api_response

        mock_options = options_patcher.start()
        mock_options.return_value = cls.mocked_api_response

        mock_head = head_patcher.start()
        mock_head.return_value = cls.mocked_api_response
