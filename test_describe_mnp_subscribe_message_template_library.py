#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试用例：DescribeMNPSubscribeMessageTemplateLibrary
产品：tcsas
版本：2025-01-06
API 文档地址：https://capi.woa.com/api/detail?product=tcsas&version=2025-01-06&action=DescribeMNPSubscribeMessageTemplateLibrary
"""

import logging
import os
import uuid
import unittest
from typing import Any, Dict, List, Optional
from unittest.mock import Mock, patch

import requests

# ---------- 常量 ----------
PRODUCT = "tcsas"
VERSION = "2025-01-06"
ACTION = "DescribeMNPSubscribeMessageTemplateLibrary"
DEFAULT_API_URL = "https://capi.woa.com/api"
REQUEST_ID_MAX_LENGTH = 128
REQUEST_TIMEOUT = 30

# 预期错误码集合
EXPECTED_ERROR_CODES = {"InvalidParameterValue", "MissingParameter", "InvalidMNPId"}

# ---------- 日志配置 ----------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
)
logger = logging.getLogger(__name__)

ResponseData = Dict[str, Any]


# ---------- 工具函数 ----------
def _build_base_headers() -> Dict[str, Any]:
    """构建基础请求头，每次调用生成新的 RequestId"""
    return {
        "Uin": os.getenv("TENCENT_CLOUD_UIN", "123456789"),
        "RequestSource": "API",
        "ApiModule": PRODUCT,
        "RequestId": str(uuid.uuid4()),
        "AccountArea": "0",  # 0-国内站, 1-国际站
        "CamContext": "",
        "ClientIp": "127.0.0.1",
        "AppId": int(os.getenv("TENCENT_CLOUD_APPID", "1234567890")),
    }


def _build_mock_response(
    status_code: int = 200,
    error_code: Optional[str] = None,
    error_message: str = "",
    data: Any = None,
    request_id: Optional[str] = None,
) -> Mock:
    """构建统一的 mock 响应对象"""
    mock_resp = Mock(spec=requests.Response)
    mock_resp.status_code = status_code

    body: ResponseData = {"Response": {"RequestId": request_id or str(uuid.uuid4())}}
    if error_code:
        body["Response"]["Error"] = {"Code": error_code, "Message": error_message}
    if data is not None:
        body["Response"]["Data"] = data

    mock_resp.json.return_value = body
    return mock_resp


class TestDescribeMNPSubscribeMessageTemplateLibrary(unittest.TestCase):
    """DescribeMNPSubscribeMessageTemplateLibrary API 测试类"""

    api_url: str = ""
    base_headers: Dict[str, Any]

    @classmethod
    def setUpClass(cls) -> None:
        """全局一次性设置"""
        cls.api_url = os.getenv("TENCENT_CLOUD_API_URL", DEFAULT_API_URL)

    def setUp(self) -> None:
        """每个测试用例前置准备"""
        self.base_headers = _build_base_headers()

    # ---------- 辅助方法 ----------

    def _post(
        self,
        extra_headers: Optional[Dict[str, Any]] = None,
        extra_params: Optional[Dict[str, Any]] = None,
    ) -> requests.Response:
        """统一 POST 请求方法，通过 extra_headers/extra_params 增量覆盖"""
        headers = self.base_headers.copy()
        if extra_headers:
            headers.update(extra_headers)

        payload: Dict[str, Any] = {"Action": ACTION, "Version": VERSION}
        if extra_params:
            payload.update(extra_params)

        resp = requests.post(
            self.api_url,
            headers=headers,
            json=payload,
            timeout=REQUEST_TIMEOUT,
        )
        logger.info("POST %s → %s %s", self.api_url, resp.status_code, resp.text[:500])
        return resp

    @staticmethod
    def _extract_response(data: ResponseData) -> ResponseData:
        """安全提取 Response 字段"""
        return data.get("Response", {})

    @staticmethod
    def _get_error_code(data: ResponseData) -> Optional[str]:
        """从响应体中提取错误码"""
        response = data.get("Response", {})
        error = response.get("Error", {})
        return error.get("Code")

    @staticmethod
    def _get_data(data: ResponseData) -> Any:
        """从响应体中提取 Data 字段"""
        return data.get("Response", {}).get("Data")

    def _assert_error(self, data: ResponseData, expected_code: str) -> None:
        """断言响应包含指定错误码"""
        actual = self._get_error_code(data)
        self.assertEqual(actual, expected_code)

    def _assert_data_exists(self, data: ResponseData) -> None:
        """断言响应包含 Data 字段"""
        self.assertIn("Data", self._extract_response(data))

    # ==================== 正常场景测试 ====================

    @patch("requests.post")
    def test_normal_request_success(self, mock_post: Mock) -> None:
        """【正常场景】携带完整必填参数请求成功"""
        mock_post.return_value = _build_mock_response(
            status_code=200,
            data=[{"TemplateId": "tpl_001", "TemplateName": "示例模板"}],
        )

        resp = self._post()
        data = resp.json()

        self.assertIn(resp.status_code, {200, 201})
        self._assert_data_exists(data)
        mock_post.assert_called_once()

    @patch("requests.post")
    def test_request_with_valid_params(self, mock_post: Mock) -> None:
        """【正常场景】携带有效 PlatformId + MNPId 参数请求"""
        mock_post.return_value = _build_mock_response(
            status_code=200,
            data=[{"TemplateId": "tpl_002", "TemplateName": "业务模板"}],
        )

        resp = self._post(extra_params={
            "PlatformId": "platform_001",
            "MNPId": "mnp_001",
        })
        self.assertEqual(resp.status_code, 200)
        self._assert_data_exists(resp.json())

    # ==================== 必填参数缺失/异常测试 ====================

    @patch("requests.post")
    def test_missing_request_id(self, mock_post: Mock) -> None:
        """【异常场景】缺少必填参数 RequestId"""
        mock_post.return_value = _build_mock_response(
            status_code=400,
            error_code="MissingParameter",
            error_message="RequestId 为必填参数",
        )

        headers = self.base_headers.copy()
        headers.pop("RequestId", None)
        resp = self._post(extra_headers={"RequestId": ""})  # 覆盖为无效值

        data = resp.json()
        self.assertIn("Error", self._extract_response(data))
        self._assert_error(data, "MissingParameter")

    @patch("requests.post")
    def test_empty_request_id(self, mock_post: Mock) -> None:
        """【异常场景】RequestId 为空字符串"""
        mock_post.return_value = _build_mock_response(
            status_code=400,
            error_code="InvalidParameterValue",
            error_message="RequestId 不能为空",
        )

        resp = self._post(extra_headers={"RequestId": ""})
        data = resp.json()

        error_code = self._get_error_code(data)
        self.assertIn(error_code, EXPECTED_ERROR_CODES)

    # ==================== 参数格式/类型错误测试 ====================

    @patch("requests.post")
    def test_invalid_appid_type_string(self, mock_post: Mock) -> None:
        """【异常场景】AppId 传入字符串而非 int"""
        mock_post.return_value = _build_mock_response(
            status_code=400,
            error_code="InvalidParameterValue",
            error_message="AppId 类型错误",
        )

        resp = self._post(extra_headers={"AppId": "not_a_number"})
        data = resp.json()

        self.assertIn("Error", self._extract_response(data))

    @patch("requests.post")
    def test_invalid_appid_negative(self, mock_post: Mock) -> None:
        """【异常场景】AppId 为负数"""
        mock_post.return_value = _build_mock_response(
            status_code=400,
            error_code="InvalidParameterValue",
            error_message="AppId 不合法",
        )

        resp = self._post(extra_headers={"AppId": -1})
        data = resp.json()

        self.assertIn("Error", self._extract_response(data))

    @patch("requests.post")
    def test_invalid_platform_id(self, mock_post: Mock) -> None:
        """【异常场景】InvalidParameterValue.InvalidPlatformId"""
        mock_post.return_value = _build_mock_response(
            status_code=400,
            error_code="InvalidParameterValue.InvalidPlatformId",
            error_message="PlatformId 不存在",
        )

        resp = self._post(extra_params={"PlatformId": "invalid_platform"})
        data = resp.json()

        self.assertIn("InvalidPlatformId", str(data))

    @patch("requests.post")
    def test_invalid_mnp_id(self, mock_post: Mock) -> None:
        """【异常场景】InvalidParameterValue.InvalidMNPId"""
        mock_post.return_value = _build_mock_response(
            status_code=400,
            error_code="InvalidParameterValue.InvalidMNPId",
            error_message="MNPId 不存在",
        )

        resp = self._post(extra_params={"MNPId": "invalid_mnp_id"})
        data = resp.json()

        self.assertIn("InvalidMNPId", str(data))

    # ==================== 业务异常测试 ====================

    @patch("requests.post")
    def test_package_already_expired(self, mock_post: Mock) -> None:
        """【异常场景】FailedOperation.PackageAlreadyExpired"""
        mock_post.return_value = _build_mock_response(
            status_code=400,
            error_code="FailedOperation.PackageAlreadyExpired",
            error_message="套餐已过期",
        )

        self._assert_error(self._post().json(), "FailedOperation.PackageAlreadyExpired")

    @patch("requests.post")
    def test_get_operate_resource_failed(self, mock_post: Mock) -> None:
        """【异常场景】FailedOperation.GetOperateResourceFailed"""
        mock_post.return_value = _build_mock_response(
            status_code=500,
            error_code="FailedOperation.GetOperateResourceFailed",
            error_message="获取操作资源失败",
        )

        self._assert_error(
            self._post().json(),
            "FailedOperation.GetOperateResourceFailed",
        )

    # ==================== 系统级异常测试 ====================

    @patch("requests.post")
    def test_internal_error(self, mock_post: Mock) -> None:
        """【异常场景】InternalError 内部错误"""
        mock_post.return_value = _build_mock_response(
            status_code=500,
            error_code="InternalError",
            error_message="内部错误",
        )

        self._assert_error(self._post().json(), "InternalError")

    @patch("requests.post")
    def test_failed_operation(self, mock_post: Mock) -> None:
        """【异常场景】FailedOperation 操作失败"""
        mock_post.return_value = _build_mock_response(
            status_code=400,
            error_code="FailedOperation",
            error_message="操作失败",
        )

        self._assert_error(self._post().json(), "FailedOperation")

    # ==================== 边界测试 ====================

    @patch("requests.post")
    def test_request_id_max_length(self, mock_post: Mock) -> None:
        """【边界测试】RequestId 刚好等于最大长度"""
        mock_post.return_value = _build_mock_response(status_code=200, data=[])

        resp = self._post(extra_headers={
            "RequestId": "x" * REQUEST_ID_MAX_LENGTH,
        })
        self.assertIn(resp.status_code, {200, 400})

    @patch("requests.post")
    def test_request_id_exceeds_max_length(self, mock_post: Mock) -> None:
        """【边界测试】RequestId 超过最大长度"""
        mock_post.return_value = _build_mock_response(
            status_code=400,
            error_code="InvalidParameterValue",
            error_message="RequestId 长度超限",
        )

        resp = self._post(extra_headers={
            "RequestId": "x" * (REQUEST_ID_MAX_LENGTH + 1),
        })
        self.assertIn(resp.status_code, {200, 400})

    @patch("requests.post")
    def test_special_characters_in_request_id(self, mock_post: Mock) -> None:
        """【边界测试】RequestId 包含特殊字符"""
        mock_post.return_value = _build_mock_response(status_code=200, data=[])

        resp = self._post(extra_headers={"RequestId": "req-id_123.test"})
        self.assertIn(resp.status_code, {200, 400})

    @patch("requests.post")
    def test_account_area_boundary(self, mock_post: Mock) -> None:
        """【边界测试】AccountArea 边界值测试"""
        test_values = ["0", "1", "2", "-1", ""]
        for area in test_values:
            with self.subTest(account_area=area):
                mock_post.return_value = _build_mock_response(
                    status_code=200 if area in ("0", "1") else 400,
                    data=[],
                )
                resp = self._post(extra_headers={"AccountArea": area})
                self.assertIn(resp.status_code, {200, 400})

    # ==================== 响应数据结构测试 ====================

    @patch("requests.post")
    def test_response_data_structure(self, mock_post: Mock) -> None:
        """【响应测试】验证响应 Data 字段结构"""
        mock_post.return_value = _build_mock_response(
            status_code=200,
            data=[
                {
                    "TemplateId": "tpl_001",
                    "TemplateName": "订阅消息模板1",
                    "TemplateContent": "{{thing1.DATA}}",
                    "CreateTime": "2024-01-01T00:00:00Z",
                }
            ],
        )

        resp = self._post()
        data = resp.json()
        response = self._extract_response(data)

        self.assertIn("Data", response)
        data_list = response["Data"]
        self.assertIsInstance(data_list, list)
        if data_list:
            self.assertIn("TemplateId", data_list[0])
            self.assertIn("TemplateName", data_list[0])

    @patch("requests.post")
    def test_response_empty_data(self, mock_post: Mock) -> None:
        """【响应测试】Data 为空数组场景"""
        mock_post.return_value = _build_mock_response(status_code=200, data=[])

        data = self._post().json()
        self.assertEqual(self._get_data(data), [])

    # ==================== 网络异常测试 ====================

    @patch("requests.post")
    def test_network_timeout(self, mock_post: Mock) -> None:
        """【网络异常】请求超时"""
        mock_post.side_effect = requests.exceptions.Timeout("请求超时")

        with self.assertRaises(requests.exceptions.Timeout):
            self._post()

    @patch("requests.post")
    def test_connection_error(self, mock_post: Mock) -> None:
        """【网络异常】连接失败"""
        mock_post.side_effect = requests.exceptions.ConnectionError("连接被拒绝")

        with self.assertRaises(requests.exceptions.ConnectionError):
            self._post()


class TestDescribeMNPSubscribeMessageTemplateLibraryIntegration(unittest.TestCase):
    """集成测试（需要真实环境）"""

    api_url: str = ""

    @classmethod
    def setUpClass(cls) -> None:
        cls.api_url = os.getenv("TENCENT_CLOUD_API_URL", DEFAULT_API_URL)

    @unittest.skipUnless(
        os.getenv("RUN_INTEGRATION_TESTS"),
        "需要设置 RUN_INTEGRATION_TESTS=1 环境变量才能运行集成测试",
    )
    def test_real_api_call(self) -> None:
        """真实环境 API 调用测试"""
        headers = _build_base_headers()
        payload: Dict[str, str] = {"Action": ACTION, "Version": VERSION}

        resp = requests.post(
            self.api_url, headers=headers, json=payload, timeout=REQUEST_TIMEOUT
        )

        logger.info("Integration Test Response: %s", resp.status_code)
        logger.info("Response Body: %s", resp.text[:1000])

        self.assertEqual(resp.status_code, 200)
        self.assertIn("Response", resp.json())


if __name__ == "__main__":
    unittest.main(verbosity=2)
