# -*- coding: utf-8 -*-
"""
小程序公有云tcmpp OpenAPI接口及接口入参封装lib
"""
from testbase.conf import settings
import time
from tcmpp_saas_autotest.tcmpp_autotestlib.openapi.tcmpp_open_api_utils import OpenApiUtils
from tcmpp_saas_autotest.tcmpp_autotestlib.tcmpp_api_testbase import TcmppSaaSAutotestTestCase
from common.crypt_utils import CryptUtils
from datetime import datetime, timezone


# 公有云鉴权相关参数（参数取值从setting的环境变量中读取）
secret_id = CryptUtils.decrypt(settings.TCMPP_SECRET_ID)
secret_key = CryptUtils.decrypt(settings.TCMPP_SECRET_KEY)
endpoint = settings.TCMPP_ENDPOINT
service = settings.TCMPP_SERVICE
version = settings.TCMPP_VERSION
common_client = OpenApiUtils.get_common_client(secret_id, secret_key, endpoint, service, version)
print("secret_idsecret_idsecret_idsecret_id", secret_id)
print("secret_keysecret_keysecret_keysecret_key", secret_key)


# 接口入参中涉及到的某些变量在此统一定义

# 定义一个时间戳变量
temp = time.strftime("%m%d%H%M%S", time.localtime())
# 获取当前日期UTC时间的年月日（即UTC时间）
date_string = datetime.now(timezone.utc).strftime("%Y-%m-%d")
# 定义TCMPP自动化测试所需应用名称
application_name = settings.TCMPP_APPLICATION_NAME
# 定义TCMPP自动化测试所需小程序名称
mnp_name = settings.TCMPP_MNP_NAME


# 所有接口的入参均封装在lib中，接口调用时的入参直接从lib中对应的class获取
class OpenApiMiniProgramData(TcmppSaaSAutotestTestCase):
    """
    OpenApi 小程序管理相关接口入参封装
    """

    create_mnp_data = {
        "MNPType": "Logistics Services->1_Pickup/Delivery",
        "MNPName": mnp_name + temp,
        "MNPIcon": "MNPIcon",
        "MNPIntro": "autotest create",
        "MNPDesc": "autotest create",
        "TeamId": "TeamId",
        "I18nList": [
            {
              "Lang": "en-US",
              "IsDefault": 1,
              "MNPName": "英文",
              "MNPIntro": "英文简介"
            }
          ]
        }

    describe_mnp_list_data = {
        "Offset": 0,
        "Limit": 1000,
        "Keyword": "",  # 小程序名称关键字，可以通过关键字模糊搜索筛选
        "TeamId": "",   # 团队ID，可以根据团队筛选小程序
        "ApplicationId": ""     # 应用id，可以根据应用筛选和该应用关联的小程序
    }

    describe_mnp_all_stage_versions_data = {
        "MNPId": "MNPId"
    }

    create_mnp_version_data = {
        "MNPId": "MNPId",
        "MNPVersion": "MNPVersion",
        "FileUrl": "FileUrl",
        "MNPVersionIntro": "autotest_create"
    }

    describe_mnp_version_data = {
        "BusinessId": "BusinessId"
    }

    create_mnp_approval_data = {
        "MNPVersionId": 0,
        "ApplyAction": "submit"
    }

    release_mnp_version_data = {
        "MNPVersionId": "MNPVersionId"
    }

    describe_mnp_category_data = {

    }

    delete_mnp_data = {
        "MNPId": "MNPId"
    }

    describe_mnp_data = {
        "MNPId": "mnp_id"
    }

    configure_mnp_preview_data = {
            "MNPId": "mnp_id",
            "ActionType": 1,  # 1-设置体验版本，2-取消
            "MNPVersionId": "mnp_version_id",
            "PreivewEntrancePath": "page/component/index"
        }

    describe_mnp_preview_data = {
        "MNPId": "mnp_id",
        "MNPVersionId": "mnp_version_id"
    }

    describe_mnp_offline_package_url_data = {
        "MNPId": "mnp_id"
    }

    describe_mnp_released_version_history_data = {
        "MNPId": "mnp_id"
    }

    modify_mnp_data = {
        "MNPType": "Logistics Services->1_Pickup/Delivery,Life Service->144_Lilliputian Services",
        "MNPName": "autotest_miniapp",
        "MNPIntro": "",
        "MNPDesc": "",
        "MNPId": "mnp_id",
        "I18nList": [
            {
                "Lang": "en-US",
                "IsDefault": 1,
                "MNPName": "英文",
                "MNPIntro": "英文简介"
            }
        ]
    }

    remove_mnp_data = {
        "MNPId": "mnp_id"
    }

    rollback_mnp_version_data = {
        "MNPId": "mnp_id",
        "MNPVersionId": 0,
        "MNPVersion": "MNPVersion"
        }

    describe_temp_secret_4_upload_file_2_cos_data = {
        "BusinessName": "tcmpp",
        "Suffix": ".gzip"
    }

    modify_mnp_domain_data = {
        "MNPId": "autotest_mnpid",
        "Domain": [
            {
                "DomainType": 1,
                "DomainUrlList": [
                    "https://www.tencent.com"
                ]
            },
            {
                "DomainType": 2
            },
            {
                "DomainType": 3
            },
            {
                "DomainType": 4
            },
            {
                "DomainType": 5
            }
        ]
    }

    create_mnp_domain_acl_data = {
        "MNPId": "MNPId",
        "Domain": [
            {
                "DomainType": 1,
                "DomainUrlList": [
                    "https://www.baidu.com"
                ]
            },
            {
                "DomainType": 2,
                "DomainUrlList": [
                    "https://www.qq.com"
                ]
            }
        ]
    }

    describe_mnp_domain_acl_data = {
        "MNPId": "MNPId"
    }

    create_mnp_app_secret_data = {
        "MNPId": "mnp_id"  # 小程序ID
    }

    describe_mnp_app_secret_data = {
        "MNPId": "mnp_id"  # 小程序ID
    }

    reset_mnp_app_secret_data = {
        "MNPId": "mnp_id"  # 小程序ID
    }

    modify_mnp_app_secret_status_data = {
        "MNPId": "mnp_id",  # 小程序ID
        "SecretStatus": 1  # 操作状态 1.冻结 2.解冻
    }

    # ========== 小程序订阅消息模板相关接口入参 ==========
    describe_mnp_subscribe_message_template_library_list_data = {
        "MNPId": "mnp_id",  # 小程序ID
        "Limit": 10,  # 限制条数
        "QueryType": 2,  # 订阅消息模板类型 2 一次性消息，3 长期订阅消息
        "Offset": 0,  # 偏移量
        "QueryStr": ""  # 查询关键字
    }

    describe_mnp_subscribe_message_template_library_data = {
        "MNPId": "mnp_id",  # 小程序ID
        "TemplateLibraryId": ""  # 订阅消息模板库ID
    }

    create_mnp_subscribe_message_template_data = {
        "MNPId": "mnp_id",  # 小程序ID
        "TemplateLibraryId": "",  # 订阅消息模板库ID
        "Keywords": [],  # 订阅消息模版关键词
        "ScenarioDescription": "autotest_scenario"  # 订阅消息模板场景描述
    }

    describe_mnp_subscribe_message_template_list_data = {
        "MNPId": "mnp_id",  # 小程序ID
        "Offset": 0,  # 偏移量
        "Limit": 10  # 分页限制
    }

    describe_mnp_subscribe_message_template_data = {
        "MNPId": "mnp_id",  # 小程序ID
        "TemplateId": ""  # 订阅消息模板ID
    }

    delete_mnp_subscribe_message_template_data = {
        "MNPId": "mnp_id",  # 小程序ID
        "TemplateId": ""  # 模板ID
    }


class OpenApiMiniGameData(TcmppSaaSAutotestTestCase):
    """
    OpenApi 小游戏管理相关接口入参封装
    """

    create_mng_data = {
        "MNPType": "棋牌->10116_牌类",
        "MNPName": mnp_name + temp,
        "MNPIcon": "MNPIcon",
        "MNPIntro": "autotest create",
        "MNPDesc": "autotest create",
        "TeamId": "TeamId",
        "I18nList": [
            {
                "Lang": "en-US",
                "IsDefault": 1,
                "MNPName": "英文",
                "MNPIntro": "英文简介"
            }
        ]
    }

    describe_mng_list_data = {
        "Offset": 0,
        "Limit": 1000,
        "Keyword": "",  # 小游戏名称关键字，可以通过关键字模糊搜索筛选
        "TeamId": "",   # 团队ID，可以根据团队筛选小游戏
        "ApplicationId": ""     # 应用id，可以根据应用筛选和该应用关联的小游戏
    }

    describe_mng_all_stage_versions_data = {
        "MNPId": "MNPId"
    }

    create_mng_version_data = {
        "MNPId": "MNPId",
        "MNPVersion": "MNPVersion",
        "FileUrl": "FileUrl",
        "MNPVersionIntro": "autotest_create"
    }

    describe_mng_version_data = {
        "BusinessId": "BusinessId"
    }

    create_mng_approval_data = {
        "MNPVersionId": 0,
        "ApplyAction": "submit"
    }

    release_mng_version_data = {
        "MNPVersionId": "MNPVersionId"
    }

    describe_mng_category_data = {

    }

    delete_mng_data = {
        "MNPId": "MNPId"
    }

    describe_mng_data = {
        "MNPId": "mnp_id"
    }

    configure_mng_preview_data = {
            "MNPId": "mnp_id",
            "ActionType": 1,  # 1-设置体验版本，2-取消
            "MNPVersionId": "mnp_version_id"
        }

    describe_mng_preview_data = {
        "MNPId": "mnp_id",
        "MNPVersionId": "mnp_version_id"
    }

    describe_mng_offline_package_url_data = {
        "MNPId": "mnp_id"
    }

    describe_mng_released_version_history_data = {
        "MNPId": "mnp_id"
    }

    modify_mng_data = {
        "MNPType": "棋牌->10116_牌类",
        "MNPName": "autotest_miniapp",
        "MNPIntro": "",
        "MNPDesc": "",
        "MNPId": "mng_id",
        "I18nList": [
            {
                "Lang": "en-US",
                "IsDefault": 1,
                "MNPName": "英文",
                "MNPIntro": "英文简介"
            }
        ]
    }

    remove_mng_data = {
        "MNPId": "mng_id"
    }

    rollback_mng_version_data = {
        "MNPId": "mng_id",
        "MNPVersionId": 0,
        "MNPVersion": "MNPVersion"
        }

    modify_mng_domain_data = {
        "MNPId": "autotest_mnpid",
        "Domain": [
            {
                "DomainType": 1,
                "DomainUrlList": [
                    "https://www.tencent.com"
                ]
            },
            {
                "DomainType": 2
            },
            {
                "DomainType": 3
            },
            {
                "DomainType": 4
            },
            {
                "DomainType": 5
            }
        ]
    }

    create_mng_domain_acl_data = {
        "MNPId": "MNPId",
        "Domain": [
            {
                "DomainType": 1,
                "DomainUrlList": [
                    "https://www.baidu.com"
                ]
            },
            {
                "DomainType": 2,
                "DomainUrlList": [
                    "https://www.qq.com"
                ]
            }
        ]
    }

    describe_mng_domain_acl_data = {
        "MNPId": "MNPId"
    }

    create_mng_app_secret_data = {
        "MNPId": "mng_id"  # 小游戏ID
    }

    describe_mng_app_secret_data = {
        "MNPId": "mng_id"  # 小游戏ID
    }

    reset_mng_app_secret_data = {
        "MNPId": "mng_id"  # 小游戏ID
    }

    modify_mng_app_secret_status_data = {
        "MNPId": "mng_id",  # 小游戏ID
        "SecretStatus": 1  # 操作状态 1.冻结 2.解冻
    }

    # ========== 小游戏订阅消息模板相关接口入参 ==========
    describe_mng_subscribe_message_template_library_list_data = {
        "MNPId": "mng_id",  # 小游戏ID
        "Limit": 10,  # 限制条数
        "QueryType": 2,  # 订阅消息模板类型 2 一次性消息，3 长期订阅消息
        "Offset": 0,  # 偏移量
        "QueryStr": ""  # 查询关键字
    }

    describe_mng_subscribe_message_template_library_data = {
        "MNPId": "mng_id",  # 小游戏ID
        "TemplateLibraryId": ""  # 订阅消息模板库ID
    }

    create_mng_subscribe_message_template_data = {
        "MNPId": "mng_id",  # 小游戏ID
        "TemplateLibraryId": "",  # 订阅消息模板库ID
        "Keywords": [],  # 订阅消息模版关键词
        "ScenarioDescription": "autotest_scenario"  # 订阅消息模板场景描述
    }

    describe_mng_subscribe_message_template_list_data = {
        "MNPId": "mng_id",  # 小游戏ID
        "Offset": 0,  # 偏移量
        "Limit": 10  # 分页限制
    }

    describe_mng_subscribe_message_template_data = {
        "MNPId": "mng_id",  # 小游戏ID
        "TemplateId": ""  # 订阅消息模板ID
    }

    delete_mng_subscribe_message_template_data = {
        "MNPId": "mng_id",  # 小游戏ID
        "TemplateId": ""  # 订阅消息模板ID
    }


class OpenApiMiniProgram(TcmppSaaSAutotestTestCase):
    """
    OpenApi：小程序管理相关接口封装
    """

    @staticmethod
    def create_mnp_app_secret_with_client(client, data):
        """
        生成小程序密钥（使用调用方传入的独立 client，专供并发用例使用）
        """
        resp = OpenApiUtils.cloud_api_request(client, "CreateMNPAppSecret", data)
        return resp

    @staticmethod
    def create_mnp(data):
        """
         创建小程序OpenApi接口
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "CreateMNP", data)
        return resp

    @staticmethod
    def describe_mnp_list(data):
        """
         查询小程序列表
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNPList", data)
        return resp

    @staticmethod
    def describe_mnp_all_stage_versions(data):
        """
         查询小程序所有研发阶段版本
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNPAllStageVersions", data)
        return resp

    @staticmethod
    def create_mnp_version(data):
        """
         创建小程序版本(从控制台上传一个小程序版本)
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "CreateMNPVersion", data)
        return resp

    @staticmethod
    def describe_mnp_version(data):
        """
         查询小程序版本创建结果
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNPVersion", data)
        return resp

    @staticmethod
    def create_mnp_approval(data):
        """
         创建小程序审核申请
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "CreateMNPApproval", data)
        return resp

    @staticmethod
    def release_mnp_version(data):
        """
         发布小程序
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "ReleaseMNPVersion", data)
        return resp

    @staticmethod
    def describe_mnp(data):
        """
         查询小程序详情
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNP", data)
        return resp

    @staticmethod
    def configure_mnp_preview(data):
        """
         设置小程序体验版本
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "ConfigureMNPPreview", data)
        return resp

    @staticmethod
    def describe_mnp_preview(data):
        """
         查询小程序预览详情
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNPPreview", data)
        return resp

    @staticmethod
    def describe_mnp_offline_package_url(data):
        """
         查询小程序预览详情
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNPOfflinePackageURL", data)
        return resp

    @staticmethod
    def describe_mnp_released_version_history(data):
        """
         查询小程序发布版本历史列表
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNPReleasedVersionHistory", data)
        return resp

    @staticmethod
    def modify_mnp(data):
        """
         修改小程序信息
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "ModifyMNP", data)
        return resp

    @staticmethod
    def remove_mnp(data):
        """
         下架小程序
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "RemoveMNP", data)
        return resp

    @staticmethod
    def rollback_mnp_version(data):
        """
         回滚小程序线上版本
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "RollbackMNPVersion", data)
        return resp

    @staticmethod
    def describe_mnp_category(data):
        """
         查询小程序分类
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNPCategory", data)
        return resp

    @staticmethod
    def delete_mnp(data):
        """
         删除小程序
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DeleteMNP", data)
        return resp

    @staticmethod
    def describe_temp_secret_4_upload_file_2_cos(data):
        """
         openapi获取上传文件到cos的临时秘钥
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeTempSecret4UploadFile2Cos", data)
        return resp

    @staticmethod
    def modify_mnp_domain(data):
        """
        小程序OpenApi接口-域名管理：修改小程序服务域名白名单或黑名单列表中的域名
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "ModifyMNPDomain", data)
        return resp

    @staticmethod
    def create_mnp_domain_acl(data):
        """
        小程序OpenApi接口-域名管理：创建小程序服务域名白名单或黑名单列表
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "CreateMNPDomainACL", data)
        return resp

    @staticmethod
    def describe_mnp_domain_acl(data):
        """
        小程序OpenApi接口-域名管理：查询小程序服务域名白名单或黑名单列表详情
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNPDomainACL", data)
        return resp

    @staticmethod
    def create_mnp_app_secret(data):
        """
        生成小程序密钥
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "CreateMNPAppSecret", data)
        return resp

    @staticmethod
    def describe_mnp_app_secret(data):
        """
        查询小程序密钥
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNPAppSecret", data)
        return resp

    @staticmethod
    def reset_mnp_app_secret(data):
        """
        重置小程序密钥
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "ResetMNPAppSecret", data)
        return resp

    @staticmethod
    def modify_mnp_app_secret_status(data):
        """
        修改小程序密钥状态：1.冻结 2.解冻
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "ModifyMNPAppSecretStatus", data)
        return resp

    @staticmethod
    def describe_mnp_subscribe_message_template_library_list(data):
        """
        OpenApi接口-订阅消息：查询小程序订阅消息模板库列表（公共模版库列表）
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNPSubscribeMessageTemplateLibraryList", data)
        return resp

    @staticmethod
    def describe_mnp_subscribe_message_template_library(data):
        """
        OpenApi接口-订阅消息：查询小程序订阅消息模板库详情（公共模版库详情）
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNPSubscribeMessageTemplateLibrary", data)
        return resp

    @staticmethod
    def create_mnp_subscribe_message_template(data):
        """
        OpenApi接口-订阅消息：新增小程序订阅消息模板（创建我的模版）
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "CreateMNPSubscribeMessageTemplate", data)
        return resp

    @staticmethod
    def describe_mnp_subscribe_message_template_list(data):
        """
        OpenApi接口-订阅消息：查询小程序订阅消息模板列表（我的模版列表）
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNPSubscribeMessageTemplateList", data)
        return resp

    @staticmethod
    def describe_mnp_subscribe_message_template(data):
        """
        OpenApi接口-订阅消息：查询小程序订阅消息模板详情（我的模版详情）
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNPSubscribeMessageTemplate", data)
        return resp

    @staticmethod
    def delete_mnp_subscribe_message_template(data):
        """
        OpenApi接口-订阅消息：删除小程序订阅消息模板（删除我的模版）
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DeleteMNPSubscribeMessageTemplate", data)
        return resp


class OpenApiMiniGame(TcmppSaaSAutotestTestCase):
    """
    OpenApi：小游戏管理相关接口封装
    """

    @staticmethod
    def create_mng(data):
        """
         创建小游戏OpenApi接口
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "CreateMNG", data)
        return resp

    @staticmethod
    def describe_mng_list(data):
        """
         查询小游戏列表
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNGList", data)
        return resp

    @staticmethod
    def describe_mng_all_stage_versions(data):
        """
         查询小游戏所有研发阶段版本
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNGAllStageVersions", data)
        return resp

    @staticmethod
    def create_mng_version(data):
        """
         创建小游戏版本(从控制台上传一个小游戏版本)
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "CreateMNGVersion", data)
        return resp

    @staticmethod
    def describe_mng_version(data):
        """
         查询小游戏版本创建结果
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNGVersion", data)
        return resp

    @staticmethod
    def create_mng_approval(data):
        """
         创建小游戏审核申请
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "CreateMNGApproval", data)
        return resp

    @staticmethod
    def release_mng_version(data):
        """
         发布小游戏
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "ReleaseMNGVersion", data)
        return resp

    @staticmethod
    def describe_mng(data):
        """
         查询小游戏详情
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNG", data)
        return resp

    @staticmethod
    def configure_mng_preview(data):
        """
         设置小游戏体验版本
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "ConfigureMNGPreview", data)
        return resp

    @staticmethod
    def describe_mng_preview(data):
        """
         查询小游戏预览详情
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNGPreview", data)
        return resp

    @staticmethod
    def describe_mng_offline_package_url(data):
        """
         查询小游戏预览详情
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNGOfflinePackageURL", data)
        return resp

    @staticmethod
    def describe_mng_released_version_history(data):
        """
         查询小游戏发布版本历史列表
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNGReleasedVersionHistory", data)
        return resp

    @staticmethod
    def modify_mng(data):
        """
         修改小游戏信息
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "ModifyMNG", data)
        return resp

    @staticmethod
    def remove_mng(data):
        """
         下架小游戏
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "RemoveMNG", data)
        return resp

    @staticmethod
    def rollback_mng_version(data):
        """
         回滚小游戏线上版本
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "RollbackMNGVersion", data)
        return resp

    @staticmethod
    def describe_mng_category(data):
        """
         查询小游戏分类
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNGCategory", data)
        return resp

    @staticmethod
    def delete_mng(data):
        """
         删除小游戏
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DeleteMNG", data)
        return resp

    @staticmethod
    def modify_mng_domain(data):
        """
        小游戏OpenApi接口-域名管理：修改小游戏服务域名白名单或黑名单列表中的域名
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "ModifyMNGDomain", data)
        return resp

    @staticmethod
    def create_mng_domain_acl(data):
        """
        小游戏OpenApi接口-域名管理：创建小游戏服务域名白名单或黑名单列表
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "CreateMNGDomainACL", data)
        return resp

    @staticmethod
    def describe_mng_domain_acl(data):
        """
        小游戏OpenApi接口-域名管理：查询小游戏服务域名白名单或黑名单列表详情
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNGDomainACL", data)
        return resp

    @staticmethod
    def create_mng_app_secret(data):
        """
        生成小游戏密钥
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "CreateMNGAppSecret", data)
        return resp

    @staticmethod
    def describe_mng_app_secret(data):
        """
        查询小游戏密钥
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNGAppSecret", data)
        return resp

    @staticmethod
    def reset_mng_app_secret(data):
        """
        重置小游戏密钥
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "ResetMNGAppSecret", data)
        return resp

    @staticmethod
    def modify_mng_app_secret_status(data):
        """
        修改小游戏密钥状态：1.冻结 2.解冻
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "ModifyMNGAppSecretStatus", data)
        return resp

    @staticmethod
    def describe_mng_subscribe_message_template_library_list(data):
        """
        OpenApi接口-订阅消息：查询小游戏订阅消息模板库列表（公共模版库列表）
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNGSubscribeMessageTemplateLibraryList", data)
        return resp

    @staticmethod
    def describe_mng_subscribe_message_template_library(data):
        """
        OpenApi接口-订阅消息：查询小游戏订阅消息模板库详情（公共模版库详情）
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNGSubscribeMessageTemplateLibrary", data)
        return resp

    @staticmethod
    def create_mng_subscribe_message_template(data):
        """
        OpenApi接口-订阅消息：新增小游戏订阅消息模板（创建我的模版）
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "CreateMNGSubscribeMessageTemplate", data)
        return resp

    @staticmethod
    def describe_mng_subscribe_message_template_list(data):
        """
        OpenApi接口-订阅消息：查询小游戏订阅消息模板列表（我的模版列表）
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNGSubscribeMessageTemplateList", data)
        return resp

    @staticmethod
    def describe_mng_subscribe_message_template(data):
        """
        OpenApi接口-订阅消息：查询小游戏订阅消息模板详情（我的模版详情）
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNGSubscribeMessageTemplate", data)
        return resp

    @staticmethod
    def delete_mng_subscribe_message_template(data):
        """
        OpenApi接口-订阅消息：删除小游戏订阅消息模板（删除我的模版）
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DeleteMNGSubscribeMessageTemplate", data)
        return resp


class OpenApiApplicationData(TcmppSaaSAutotestTestCase):
    """
    OpenApi 应用管理相关接口入参封装
    """

    create_application_data = {
        "ApplicationName": application_name,
        "Logo": "icon_url",
        "TeamId": "autotest_team",
        "Intro": "test",
        "Scheme": ""
    }

    describe_application_list_data = {
        "TeamId": "",
        "Limit": 1000,
        "Offset": 0,
        "Keyword": ""
    }

    describe_application_data = {
        "ApplicationId": ""
    }

    describe_application_config_file_data = {
        "ApplicationId": ""
    }

    delete_application_data = {
        "ApplicationId": ""
    }

    modify_application_data = {
        "ApplicationId": "application_id",
        "ApplicationName": application_name,
        "Logo": "icon_url",
        "Intro": "介绍信息",
        "Scheme": ""
    }

    create_application_config_data = {
        "ApplicationId": "ApplicationId",   # 应用ID
        "ApplicationType": 2,   # 包名类型  1-测试 2-正式
        "ApplicationPlatformType": 2,   # 应用平台类型 2-andorid 3-ios
        "AppKey": "com.suaas.yk.tdgame",  # 包名
        "AppURL": ""
    }

    describe_application_mnp_list_data = {
        "Offset": 0,            # 偏移量
        "Limit": 1000,            # 每页数据条数
        "ApplicationId": "",    # 应用id
        "OnlineStatus": 0,      # 上架状态 0-全部，1-线上，2-灰度
        "EngineTypeList": [],  # 类型 0-小程序，1-小游戏
        "SubCategory": "",      # 二级分类
        "PrimaryCategory": "",  # 一级分类
        "Keyword": ""         # 关键字
    }

    describe_mnp_approval_list_data = {
        "Limit": 30,
        "Offset": 0,
        "ApprovalStatusList": [0],     # 审批状态 1 审核中 2 不通过 3 通过 4 撤销
        "Keyword": "",  # 小程序名称关键字，可以通过关键字模糊搜索筛选
        "TeamId": "",  # 如果有需要，可以从用例中传入对应的团队id
        "ApplicationId": ""  # 如果有需要，可以从用例中传入对应的应用id
    }

    process_mnp_approval_data = {
        "ApprovalNo": "ApprovalNo",
        "ApprovalItems": [
            {
                "AppId": "AppId",
                "ApprovalResult": 3,    # 审批结果:  2-审核不通过; 3-审核通过
                "ApprovalNote": "autotest approval pass"
            }
        ]
    }


class OpenApiApplication(TcmppSaaSAutotestTestCase):
    """
    OpenApi：应用管理相关接口封装
    """

    @staticmethod
    def create_application(data):
        """
         创建应用OpenApi接口
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "CreateApplication", data)
        return resp

    @staticmethod
    def describe_application_list(data):
        """
        应用管理：获取应用列表数据
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeApplicationList", data)
        return resp

    @staticmethod
    def describe_application(data):
        """
        OpenApi接口-应用管理：查询应用详情
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeApplication", data)
        return resp

    @staticmethod
    def modify_application(data):
        """
        OpenApi接口-应用管理：查询应用详情
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "ModifyApplication", data)
        return resp

    @staticmethod
    def describe_application_config_file(data):
        """
        OpenApi接口-应用管理：查询应用配置文件
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeApplicationConfigFile", data)
        return resp

    @staticmethod
    def delete_application(data):
        """
        OpenApi接口-应用管理：删除应用
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DeleteApplication", data)
        return resp

    @staticmethod
    def create_application_config(data):
        """
        OpenApi接口-应用管理：创建应用配置包名
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "CreateApplicationConfig", data)
        return resp

    @staticmethod
    def describe_application_mnp_list(data):
        """
        OpenApi接口-应用管理：查询应用下小程序列表
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeApplicationMNPList", data)
        return resp

    @staticmethod
    def describe_mnp_approval_list(data):
        """
         OpenApi接口-应用管理：查询小程序审核申请列表
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNPApprovalList", data)
        return resp

    @staticmethod
    def process_mnp_approval(data):
        """
         OpenApi接口-应用管理：处理小程序审核申请
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "ProcessMNPApproval", data)
        return resp


class OpenApiDomainManageData(TcmppSaaSAutotestTestCase):
    """
    OpenApi 域名管理相关接口入参封装
    """

    create_global_domain_acl_data = {
        "DomainType": 1,    # 域名类型 1 白名单 2 黑名单
        "DomainUrlList": ["openapi.autotest.domain.com"]
    }

    describe_global_domain_acl_data = {
        "Offset": 0,
        "Limit": 20,
        "DomainTypes": [1],     # 域名类型 1 白名单 2 黑名单
        "Keyword": ""
    }

    modify_global_domain_data = {
        "DomainId": 0,  # 域名ID
        "DomainUrl": "openapi.autotest.domain.modify",
    }

    delete_global_domain_data = {
        "DomainId": 0
    }


class OpenApiDomainManage(TcmppSaaSAutotestTestCase):
    """
    OpenApi：域名管理管理相关接口封装
    """

    @staticmethod
    def create_global_domain_acl(data):
        """
        OpenApi接口-域名管理：创建全局域名白名单或黑名单列表
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "CreateGlobalDomainACL", data)
        return resp

    @staticmethod
    def describe_global_domain_acl(data):
        """
        OpenApi接口-域名管理：查询全局域名黑名单和白名单列表
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeGlobalDomainACL", data)
        return resp

    @staticmethod
    def modify_global_domain(data):
        """
        OpenApi接口-域名管理：修改全局域名白名单或黑名单
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "ModifyGlobalDomain", data)
        return resp

    @staticmethod
    def delete_global_domain(data):
        """
        OpenApi接口-域名管理：删除全局域名白名单或黑名单列表中的域名
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DeleteGlobalDomain", data)
        return resp


class OpenApiSensitiveApiData(TcmppSaaSAutotestTestCase):
    """
    OpenApi 敏感api管理相关接口入参封装
    """
    create_application_sensitive_api_data = {
        "ApplicationId": "",  # 如果有需要，可以从用例中传入对应的应用id
        "APIList": [
            {
                "APIDesc": "tcsasState",
                "APIName": "tcsasState",
                "APIType": 2,
                "UseScope": 100
            }
        ]
    }

    delete_application_sensitive_api_data = {
        "APIId": "0",
        # "GlobalTeamId": "-1"      # openAPI中没有该参数
    }

    describe_application_sensitive_api_list_data = {
        "Limit": 30,
        "Offset": 0,
        "Keyword": "tcsasState",
        "ApplicationId": "",  # 如果有需要，可以从用例中传入对应的应用id
        "TeamId": "",  # 如果有需要，可以从用例中传入对应的团队id
    }

    disable_application_sensitive_api_data = {
        "APIId": "0",
        # "GlobalTeamId": "-1"
    }

    enable_application_sensitive_api_data = {
        "APIId": "0",
        # "GlobalTeamId": "-1"
    }

    create_mnp_sensitive_api_permission_approval_data = {
        "APIId": "0",
        "ApplyReason": "We need it.",
        "MNPId": ""
    }

    # 查询小程序调用敏感API权限申请列表
    describe_mnp_sensitive_api_permission_approval_list_data = {
        # "MNPId": "autotest",
        "Limit": 10,
        "Offset": 0,
        "Keyword": "tcsasState",
        # "ApplicationId": "",
        # "GlobalTeamId": -1
    }

    # 查询小程序调用敏感API权限申请详情
    describe_mnp_sensitive_api_permission_approval_data = {
        "ApprovalNo": ""
    }

    process_mnp_sensitive_api_permission_approval_data = {
        "ApprovalNo": "",
        "ApprovalStatus": 30,
        "ApprovalNote": ""
    }

    describe_mnp_sensitive_api_permission_list_data = {
        "MNPId": "autotest",
        "Limit": 10,
        "Offset": 0,
        "Keyword": "tcsasState",
        "ApplicationId": ""
    }

    create_mng_sensitive_api_permission_approval_data = {
        "APIId": "0",
        "ApplyReason": "We need it.",
        "MNPId": ""
    }

    describe_mng_sensitive_api_permission_list_data = {
        "MNPId": "autotest",
        "Limit": 10,
        "Offset": 0,
        "Keyword": "tcsasState",
        "ApplicationId": ""
    }

    # 查询小游戏调用敏感API权限申请详情
    describe_mng_sensitive_api_permission_approval_data = {
        "ApprovalNo": ""
    }


class OpenApiSensitiveApi(TcmppSaaSAutotestTestCase):
    """
    OpenApi：敏感api管理管理相关接口封装
    """
    @staticmethod
    def create_application_sensitive_api(data):
        """
        创建应用敏感API
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "CreateApplicationSensitiveAPI", data)
        return resp

    @staticmethod
    def delete_application_sensitive_api(data):
        """
        删除应用敏感API
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DeleteApplicationSensitiveAPI", data)
        return resp

    @staticmethod
    def describe_application_sensitive_api_list(data):
        """
        查询应用敏感API列表
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeApplicationSensitiveAPIList", data)
        return resp

    @staticmethod
    def disable_application_sensitive_api(data):
        """
        设置应用敏感API为受限状态
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DisableApplicationSensitiveAPI", data)
        return resp

    @staticmethod
    def enable_application_sensitive_api(data):
        """
        设置应用敏感API为打开状态
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "EnableApplicationSensitiveAPI", data)
        return resp

    @staticmethod
    def create_mnp_sensitive_api_permission_approval(data):
        """
        创建小程序调用敏感API权限申请
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "CreateMNPSensitiveAPIPermissionApproval", data)
        return resp

    @staticmethod
    def describe_mnp_sensitive_api_permission_approval_list(data):
        """
        查询小程序调用敏感API权限申请列表
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNPSensitiveAPIPermissionApprovalList", data)
        return resp

    @staticmethod
    def describe_mnp_sensitive_api_permission_approval(data):
        """
        查询小程序调用敏感API权限申请详情
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNPSensitiveAPIPermissionApproval", data)
        return resp

    @staticmethod
    def process_mnp_sensitive_api_permission_approval(data):
        """
        处理小程序调用敏感API权限申请
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "ProcessMNPSensitiveAPIPermissionApproval", data)
        return resp

    @staticmethod
    def describe_mnp_sensitive_api_permission_list(data):
        """
        查询小程序可调用敏感API列表
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNPSensitiveAPIPermissionList", data)
        return resp

    @staticmethod
    def create_mng_sensitive_api_permission_approval(data):
        """
        创建小游戏调用敏感API权限申请
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "CreateMNGSensitiveAPIPermissionApproval", data)
        return resp

    @staticmethod
    def describe_mng_sensitive_api_permission_list(data):
        """
        查询小游戏可调用敏感API列表
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNGSensitiveAPIPermissionList", data)
        return resp

    @staticmethod
    def describe_mng_sensitive_api_permission_approval(data):
        """
        查询小游戏调用敏感API权限申请详情
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNGSensitiveAPIPermissionApproval", data)
        return resp


class OpenApiUserManageData(TcmppSaaSAutotestTestCase):
    """
    OpenApi 用户管理相关接口入参封装
    """

    create_preset_key_data = {

    }

    create_user_data = {
        "UserAccount": "autotest" + temp,
        "UserName": "autotest" + temp,
        "AccountType": 3,  # 账号类型：1 超管； 2 平台管理员； 3 普通用户
        "KeyId": "",  # KeyId通过调用创建预设秘钥获取对应RequestId
        "Password": ""
    }

    describe_user_list_data = {
        "Keyword": "",
        "Limit": 1000,
        "Offset": 0,
        "AccountType": 0,  # 账号类型：0 全部类型； 1 超管； 2 平台管理员； 3 普通用户;  4 注册用户
        "TeamId": "0",  # 团队id，如果输入0代表全部团队；如果输入具体团队id，代表按照所属团队筛选用户
    }

    delete_user_data = {
        "UserId": "autotest_userId"
    }

    describe_user_data = {
        "UserId": "autotest_userId"
    }

    modify_user_data = {
        "UserId": "UserId",
        "UserName": "ModifyUserName",
        "AccountType": 3    # 账号类型：0 全部类型； 1 超管； 2 平台管理员； 3 普通用户;  4 注册用户
    }


class OpenApiUserManage(TcmppSaaSAutotestTestCase):
    """
    OpenApi：用户管理管理相关接口封装
    """

    @staticmethod
    def create_preset_key(data):
        """
        获取加密秘钥
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "CreatePresetKey", data)
        return resp

    @staticmethod
    def create_user(data):
        """
        创建用户
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "CreateUser", data)
        return resp

    @staticmethod
    def describe_user_list(data):
        """
        查询用户列表
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeUserList", data)
        return resp

    @staticmethod
    def delete_user(data):
        """
        删除用户
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DeleteUser", data)
        return resp

    @staticmethod
    def describe_user(data):
        """
        查询用户详细信息
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeUser", data)
        return resp

    @staticmethod
    def modify_user(data):
        """
        修改用户信息
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "ModifyUser", data)
        return resp


class OpenApiTeamManagementData(TcmppSaaSAutotestTestCase):
    """
    OpenApi 团队管理相关接口入参封装
    """
    describe_team_list_data = {
        "Limit": 1000,
        "Offset": 0,
        "Keyword": ""
    }

    create_team_data = {
        "TeamName": "AT_team" + temp,
        "AdminUserId": "AdminUserId",  # 团队管理员的用户ID
        "TeamRoleTypeList": [2],  # 团队类型：1 小程序管理； 2 应用管理
    }

    delete_team_data = {
        "TeamId": "team_id"
    }

    modify_team_data = {
        "TeamName": "TeamName",  # 团队名称
        "AdminUserId": "AdminUserId",  # 团队管理员的用户id
        "TeamId": "TeamId"
    }

    describe_team_data = {
        "TeamId": "TeamId"
    }

    describe_role_list_data = {
        "Offset": 0,
        "Limit": 10,
        "Keyword": "",
        "TeamId": ""
    }

    add_team_member_data = {
        "TeamId": "TeamId",
        "MemberList": [
            {
                "UserId": "UserId",
                "UserRoleId": 0
            }
        ]
    }

    describe_team_member_list_data = {
        "Offset": 0,
        "Limit": 1000,
        "TeamId": "",   # 团队ID，可选输入项，输入后会根据团队来筛选成员
        "Keyword": "",  # 关键字，可选输入项，输入后会根据关键字来筛选成员
        "RoleIds": []   # 角色id，可选输入项，输入后会根据角色来筛选成员
    }

    modify_team_member_data = {
        "TeamId": "TeamId",
        "UserId": "UserId",
        "RoleId": 0
    }

    delete_team_member_data = {
        "TeamId": "TeamId",
        "UserId": "UserId"
    }


class OpenApiTeamManagement(TcmppSaaSAutotestTestCase):
    """
    OpenApi：团队管理管理相关接口封装
    """

    @staticmethod
    def describe_team_list(data):
        """
         查询团队列表
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeTeamList", data)
        return resp

    @staticmethod
    def create_team(data):
        """
         创建团队
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "CreateTeam", data)
        return resp

    @staticmethod
    def delete_team(data):
        """
         删除团队
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DeleteTeam", data)
        return resp

    @staticmethod
    def modify_team(data):
        """
         修改团队信息
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "ModifyTeam", data)
        return resp

    @staticmethod
    def describe_team(data):
        """
         查询团队详情
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeTeam", data)
        return resp

    @staticmethod
    def describe_role_list(data):
        """
         查询角色列表
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeRoleList", data)
        return resp

    @staticmethod
    def add_team_member(data):
        """
         添加团队成员
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "AddTeamMember", data)
        return resp

    @staticmethod
    def describe_team_member_list(data):
        """
         查询团队成员列表
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeTeamMemberList", data)
        return resp

    @staticmethod
    def modify_team_member(data):
        """
         修改团队成员信息
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "ModifyTeamMember", data)
        return resp

    @staticmethod
    def delete_team_member(data):
        """
         删除团队成员
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DeleteTeamMember", data)
        return resp


class OpenApiOperationManagementData(TcmppSaaSAutotestTestCase):
    """
    OpenApi：运营管理相关接口入参封装
    """

    describe_mng_active_user_real_time_statistics_data = {
        "MNPId": "MNPId",
        "ReportId": "mnp_data_analysis",    # 报表id
        "IndexId": "realtime_uv_num",   # 指标id
        "QueryData": ""     # 查询数据
    }

    describe_mnp_active_user_real_time_statistics_data = {
        "MNPId": "MNPId",
        "ReportId": "mnp_data_analysis",    # 报表id
        "IndexId": "realtime_uv_num",   # 指标id
        "QueryData": ""     # 查询数据
    }

    describe_mng_access_analysis_overview_data = {
        "TimeBegin": 20251128,  # 开始时间
        "MNPId": "MNPId",  # 小程序ID
        "TimeEnd": 20251204,  # 结束时间
        "ProdData": 1,  # 数据类型  1 生产数据，0非生产
        "Platform": 0  # 操作系统：0全部，2安卓，3iOS
    }

    describe_mnp_access_analysis_overview_data = {
        "TimeBegin": 20251128,  # 开始时间
        "MNPId": "MNPId",  # 小程序ID
        "TimeEnd": 20251204,  # 结束时间
        "ProdData": 1,  # 数据类型  1 生产数据，0非生产
        "Platform": 0   # 操作系统：0全部，2安卓，3iOS
    }

    describe_mng_access_analysis_detail_data = {
        "TimeBegin": 20251128,  # 开始时间
        "MNPId": "MNPId",  # 小程序ID
        "DataType": 1,  # 数据类型  1 生产数据，0非生产
        "Platform": 0,  # 操作系统：0全部，2安卓，3iOS
        "TimeEnd": 20251204  # 结束时间
    }

    describe_mnp_report_detail_data = {
        "TimeBegin": 20251128,   # 开始时间
        "MNPId": "MNPId",     # 小程序ID
        "DataType": 1,  # 数据类型  1 生产数据，0非生产
        "Platform": 0,  # 操作系统：0全部，2安卓，3iOS
        "TimeEnd": 20251204  # 结束时间
    }

    describe_mnp_report_data_line_chart_data = {
        "MNPId": "MNPId",     # 小程序ID
        "ReportId": "mnp_data_analysis",    # 报表id
        "IndexId": "active_device_num",  # 指标id
        "QueryData": ""     # 查询数据
    }

    describe_mnp_page_analysis_detail_data = {
        "DataType": 1,  # 数据类型  1 生产数据，0非生产
        "MNPId": "MNPId",     # 小程序ID
        "TimeBegin": "TimeBegin",  # 开始时间
        "TimeEnd": "TimeEnd",  # 结束时间
        "Platform": 0  # 操作系统：0全部，2安卓，3iOS
    }

    describe_advert_ising_overview_data = {
        "TimeBegin": "TimeBegin",
        "TimeEnd": "TimeEnd",
        "MNPId": "MNPId",
        "AdUnitType": "",
        "Platform": 0   # 操作系统：0-全部，2-安卓，3-IOS
    }

    describe_advert_ising_line_chart_data = {
        "TimeBegin": "TimeBegin",
        "TimeEnd": "TimeEnd",
        "MNPId": "MNPId",
        "AdUnitType": "",
        "Platform": 0   # 操作系统：0-全部，2-安卓，3-IOS
    }

    describe_mnp_advert_ising_detail_data = {
        "TimeBegin": "TimeBegin",
        "TimeEnd": "TimeEnd",
        "MNPId": "MNPId",
        "AdUnitType": "",
        "Platform": 0   # 操作系统：0-全部，2-安卓，3-IOS
    }

    describe_mng_advert_ising_overview_data = {
        "TimeBegin": "TimeBegin",
        "TimeEnd": "TimeEnd",
        "MNPId": "MNPId",
        "AdUnitType": "",
        "Platform": 0   # 操作系统：0-全部，2-安卓，3-IOS
    }

    describe_mng_advert_ising_line_chart_data = {
        "TimeBegin": "TimeBegin",
        "TimeEnd": "TimeEnd",
        "MNPId": "MNPId",
        "AdUnitType": "",
        "Platform": 0  # 操作系统：0-全部，2-安卓，3-IOS
    }

    describe_mng_advert_ising_detail_data = {
        "TimeBegin": "TimeBegin",
        "TimeEnd": "TimeEnd",
        "MNPId": "MNPId",
        "AdUnitType": "",
        "Platform": 0   # 操作系统：0-全部，2-安卓，3-IOS
    }
    
    describe_mng_access_analysis_line_chart_data = {
        "MNPId": "MNPId",
        "ReportId": "mnp_data_analysis",  # 报表id
        "IndexId": "active_device_num",  # 指标id
        "QueryData": ""  # 指标id
    }

    describe_mnp_retention_data_data = {
        "MNPId": "mppzh60a4ziqmc29",  # 小程序id
        "Platform": 0,   # 操作系统：0全部，2安卓，3iOS
        "TimeBegin": "20250630",
        "TimeEnd": "20250706",
        "DataType": 1  # 1-生产数据，0-非生产数据
    }

    describe_mng_retention_data_data = {
        "MNPId": "mppzh60a4ziqmc29",  # 小程序id
        "Platform": 0,  # 操作系统：0全部，2安卓，3iOS
        "TimeBegin": "20250630",
        "TimeEnd": "20250706",
        "DataType": 1  # 1-生产数据，0-非生产数据
    }

    describe_app_data_overview_data = {
        "DataTime": 20251205,
        "ApplicationIds": ["app-1ro3zp3nta"]
    }

    describe_app_data_detail_line_chart_data = {
        "ReportId": "mnp_data_analysis",    # 报表id
        "IndexIds": ["app_new_device_num"], # 指标id
        "QueryData": "",                    # 查询数据
        "ApplicationIds": ["app-1ro3zp3nta"]
    }

    describe_mng_mau_data_detail_data = {
        "ApplicationId": "",  # 应用id
        "DataType": 1,  # 数据类型，1=生产数据，0=非生产数据
        "MNPId": "",  # 小游戏id
        "MNPTeamId": ''  # 小程序团队id
    }

    describe_mnp_mau_data_detail_data = {
        "ApplicationId": "",  # 应用id
        "DataType": 1,  # 数据类型，1=生产数据，0=非生产数据
        "MNPId": "",  # 小游戏id
        "MNPTeamId": ''  # 小程序团队id
    }

    describe_mng_mau_monthly_comparison_metriccard_data = {
        "ApplicationId": "",  # 应用id
        "DataType": '',  # 数据类型，1=生产数据，0=非生产数据
        "MNPId": "",  # 小游戏id
        "MNPTeamId": '',  # 小程序团队id
        "SourceMonth": '',  # 对比月份，默认是上个月
        "TargetMonth": ''  # 目标月份，默认是当月
    }

    describe_mau_indicator_card_data = {
        "ApplicationId": "app-2jxgqq7gnp",  # 应用id
        "MNPId": "mppzh60a4ziqmc29",
        "MNPTeamId": "2115879789",  # 小程序团队id
        "DataType": 1,
        "SourceMonth": 202507,
        "TargetMonth": 202508
    }

    describe_global_overview_report_detail_data = {
        "IndexId": "index_id",  # 需替换参数值
        "ReportId": "report_id",  # 需替换参数值
        "QueryData": "query_data"  # 需替换参数值
    }

    describe_global_overview_data_summary_data = {
        #"ApplicationId": "",
        #"MNPId": "",  # 默认为空
        "DataTime": int(date_string.replace("-", '')),
        "DataType": "Overview"  # Overview-全局概览，BaseData-数据概览的基础数据
    }

    describe_mng_payment_overview_data = {
        "TimeBegin": 20251128,  # 开始时间
        "MNPId": "MNPId",  # 小程序ID
        "DataType": 1,  # 数据类型  1 生产数据，0非生产
        "Platform": 0,  # 操作系统：0全部，2安卓，3iOS
        "TimeEnd": 20251204  # 结束时间
    }

    describe_mng_payment_retention_analysis_data = {
        "TimeBegin": 20251128,  # 开始时间
        "MNPId": "MNPId",  # 小程序ID
        "DataType": 1,  # 数据类型  1 生产数据，0非生产
        "Platform": 0,  # 操作系统：0全部，2安卓，3iOS
        "TimeEnd": 20251204  # 结束时间
    }

    describe_mng_payment_report_data_data = {
        "ReportId": "payment_data_analysis",  #
        "IndexId": "mng_paid_amount",  #
        "QueryData": ""
    }

    describe_mng_payment_report_detail_data = {
        "TimeBegin": 20251128,  # 开始时间
        "MNPId": "MNPId",  # 小程序ID
        "DataType": 1,  # 数据类型  1 生产数据，0非生产
        "Platform": 0,  # 操作系统：0全部，2安卓，3iOS
        "TimeEnd": 20251204  # 结束时间
    }

    describe_payment_data_detail_data = {
        "TimeBegin": 20251128,  # 开始时间
        "MNPIds": "[]",  # 小程序ID
        "DataType": 1,  # 数据类型  1 生产数据，0非生产
        "Platform": 0,  # 操作系统：0全部，2安卓，3iOS
        "TimeEnd": 20251204  # 结束时间
    }

    describe_payment_data_overview_data = {
        "TimeBegin": 20251128,  # 开始时间
        "MNPIds": "[]",  # 小程序ID
        "DataType": 1,  # 数据类型  1 生产数据，0非生产
        "Platform": 0,  # 操作系统：0全部，2安卓，3iOS
        "TimeEnd": 20251204  # 结束时间
    }

    describe_payment_line_chart_data = {
        "ReportId": "payment_data_analysis",  #报表id
        "IndexId": "order_user_num",  #指标id
        "QueryData": ""
    }

    describe_payment_mng_line_chart_data = {
        "ReportId": "payment_data_analysis",  #报表id
        "IndexId": "mng_paid_amount",  #指标id
        "QueryData": ""
    }


class OpenApiOperationManagement(TcmppSaaSAutotestTestCase):
    """
    OpenApi：运营管理相关接口封装
    """

    @staticmethod
    def describe_mng_active_user_real_time_statistics(data):
        """
         小游戏活跃实时统计数据
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNGActiveUserRealTimeStatistics", data)
        return resp

    @staticmethod
    def describe_mnp_active_user_real_time_statistics(data):
        """
         小程序活跃实时统计数据
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNPActiveUserRealTimeStatistics", data)
        return resp

    @staticmethod
    def describe_mnp_access_analysis_overview(data):
        """
         小程序访问分析概览数据接口
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNPAccessAnalysisOverview", data)
        return resp

    @staticmethod
    def describe_mng_access_analysis_overview(data):
        """
         小游戏访问分析概览数据接口
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNGAccessAnalysisOverview", data)
        return resp

    @staticmethod
    def describe_mnp_report_detail(data):
        """
         小程序报表详细数据接口
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNPReportDetail", data)
        return resp

    @staticmethod
    def describe_mng_access_analysis_detail(data):
        """
         小游戏报表详细数据接口
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNGAccessAnalysisDetail", data)
        return resp

    @staticmethod
    def describe_mnp_report_data_line_chart(data):
        """
         小程序报表数据趋势图接口
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNPReportDataLineChart", data)
        return resp

    @staticmethod
    def describe_mnp_page_analysis_detail(data):
        """
         小程序页面分析详情接口
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNPPageAnalysisDetail", data)
        return resp

    @staticmethod
    def describe_advert_ising_overview(data):
        """
         小程序广告收益概览数据
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeAdvertisingOverview", data)
        return resp

    @staticmethod
    def describe_advert_ising_line_chart(data):
        """
         小程序广告收益趋势
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeAdvertisingLineChart", data)
        return resp

    @staticmethod
    def describe_mnp_advert_ising_detail(data):
        """
         小程序广告收益明细
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNPAdvertisingDetail", data)
        return resp

    @staticmethod
    def describe_mng_advert_ising_overview(data):
        """
         小游戏广告收益概览数据
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNGAdvertisingOverview", data)
        return resp

    @staticmethod
    def describe_mng_advert_ising_line_chart(data):
        """
         小游戏广告收益趋势
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNGAdvertisingLineChart", data)
        return resp

    @staticmethod
    def describe_mng_advert_ising_detail(data):
        """
         小游戏广告收益明细
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNGAdvertisingDetail", data)
        return resp

    def describe_mng_access_analysis_line_chart(data):
        """
         小游戏报表数据趋势图接口
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNGAccessAnalysisLineChart", data)
        return resp

    @staticmethod
    def describe_mnp_retention_data(data):
        """
         小程序留存数据接口
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNPRetentionData", data)
        return resp

    @staticmethod
    def describe_mng_retention_data(data):
        """
         小游戏留存数据接口
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNGRetentionData", data)
        return resp

    @staticmethod
    def describe_app_data_overview(data):
        """
         应用维度数据概览接口
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeAPPDataOverview", data)
        return resp

    @staticmethod
    def describe_app_data_detail_line_chart(data):
        """
         应用维度数据概览接口
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeAPPDataDetailLineChart", data)
        return resp

    @staticmethod
    def describe_mng_mau_data_detail_data(data):
        """
         小游戏MAU数据详情
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNGMAUDataDetail", data)
        return resp

    @staticmethod
    def describe_mng_mau_linechart(data):
        """
         小游戏MAU趋势
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNGMAULineChart", data)
        return resp

    @staticmethod
    def describe_mng_mau_monthly_comparison_metriccard(data):
        """
         小游戏MAU月份对比指标卡
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNGMAUMonthlyComparisonMetricCard", data)
        return resp

    @staticmethod
    def describe_mnp_mau_linechart(data):
        """
         小程序MAU趋势
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNPMAULineChart", data)
        return resp

    @staticmethod
    def describe_mnp_mau_data_detail_data(data):
        """
         小程序MAU数据详情
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNPMAUDataDetail", data)
        return resp

    @staticmethod
    def describe_mnp_mau_metric_card(data):
        """
         小程序MAU指标卡
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNPMAUMetricCard", data)
        return resp

    @staticmethod
    def describe_global_overview_report_detail(data):
        """
         全局概览-报表明细
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeGlobalOverviewReportDetail", data)
        return resp

    @staticmethod
    def describe_global_overview_data_summary(data):
        """
         全局概览-数据总览
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeGlobalOverviewDataSummary", data)
        return resp

    @staticmethod
    def describe_mng_payment_overview(data):
        """
         小游戏支付概览
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNGPaymentOverview", data)
        return resp

    @staticmethod
    def describe_mng_payment_retention_analysis(data):
        """
         小游戏支付留存分析
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNGPaymentRetentionAnalysis", data)
        return resp

    @staticmethod
    def describe_mng_payment_line_chart(data):
        """
         小游戏支付数据趋势图
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNGPaymentLineChart", data)
        return resp

    @staticmethod
    def describe_mng_payment_report_detail(data):
        """
         小游戏支付报表详情
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribeMNGPaymentReportDetail", data)
        return resp

    @staticmethod
    def describe_payment_data_detail(data):
        """
         小程序支付数据详情
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribePaymentDataDetail", data)
        return resp

    @staticmethod
    def describe_payment_data_overview(data):
        """
         小程序支付数据概览
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribePaymentDataOverview", data)
        return resp

    def describe_payment_data_line_chart(data):
        """
         小程序标准支付数据趋势图
        """
        resp = OpenApiUtils.cloud_api_request(common_client, "DescribePaymentDataLineChart", data)
        return resp


if __name__ == '__main__':
    pass