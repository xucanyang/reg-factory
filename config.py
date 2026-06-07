# -*- coding: utf-8 -*-
"""
config.py — 全局配置。

所有密钥/凭据都从环境变量读取（默认空），不在仓库里留明文。
支持把变量写进同目录的 .env 文件（见 .env.example）；.env 只在对应环境
变量尚未设置时生效，不会覆盖真实的进程环境变量。
"""

import os


# ---------------------------------------------------------------- .env 加载
def _load_dotenv(path=None):
    """零依赖 .env 读取器：解析 KEY=VALUE，忽略空行与 # 注释。
    只在 os.environ 里尚未设置该 KEY 时填入（真实环境变量优先）。"""
    if path is None:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
    if not os.path.isfile(path):
        return
    try:
        with open(path, encoding="utf-8") as f:
            for raw in f:
                line = raw.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, _, val = line.partition("=")
                key = key.strip()
                val = val.strip().strip('"').strip("'")
                if key and key not in os.environ:
                    os.environ[key] = val
    except Exception:
        pass


_load_dotenv()


def _env(name, default=""):
    return os.environ.get(name, default)


# ---------------------------------------------------------------- 本地基建
# BitBrowser 本地 API 地址
BITBROWSER_API = _env("BITBROWSER_API", "http://127.0.0.1:54345")

# Claude.ai 注册相关 URL
CLAUDE_LOGIN_URL = "https://claude.ai/login"

# Cookie 输出目录
COOKIE_OUTPUT_DIR = "cookies"

# ---------------------------------------------------------------- 域名邮箱（备用）
MAIL_DOMAIN = _env("MAIL_DOMAIN", "")
MAIL_API_BASE = _env("MAIL_API_BASE", "")
MAIL_ADMIN_USER = _env("MAIL_ADMIN_USER", "admin")
MAIL_ADMIN_PASS = _env("MAIL_ADMIN_PASS", "")
# JWT token（从浏览器抓取，可能会过期需要更新）
MAIL_AUTH_TOKEN = _env("MAIL_AUTH_TOKEN", "")
# 新建邮箱统一密码
MAIL_NEW_PASS = _env("MAIL_NEW_PASS", "")

# ---------------------------------------------------------------- Outlook 邮箱 API (闪客云邮箱)
OUTLOOK_API_BASE = _env("OUTLOOK_API_BASE", "http://api.shankeyun.com")
OUTLOOK_CARD = _env("OUTLOOK_CARD", "")  # 闪客云卡密
OUTLOOK_TYPE = _env("OUTLOOK_TYPE", "outlook")  # outlook / hotmail / any

# ---------------------------------------------------------------- 短信接码平台 (firefox.fun)
SMS_API_BASE = _env("SMS_API_BASE", "http://www.firefox.fun/yhapi.ashx")
SMS_TOKEN = _env("SMS_TOKEN", "")  # 接码平台 token
SMS_PROJECT_ID = _env("SMS_PROJECT_ID", "2313")  # claude 项目
# 优先国家列表，按顺序尝试，""=任意(排除黑名单)
SMS_COUNTRY_PREFER = ["60", "56", "57", "44", ""]  # 60=马来西亚 56=智利 57=哥伦比亚 44=英国 ""=任意
SMS_COUNTRY_BLACKLIST = ["63"]  # 菲律宾

# ---------------------------------------------------------------- 备用短信平台 (hero-sms.com)
HERO_SMS_API_BASE = _env("HERO_SMS_API_BASE", "https://hero-sms.com/stubs/handler_api.php")
HERO_SMS_API_KEY = _env("HERO_SMS_API_KEY", "")  # 备用接码 api_key
HERO_SMS_SERVICE = _env("HERO_SMS_SERVICE", "acz")  # Claude 专用服务
# 优先国家: 7=马来西亚 52=泰国 16=英国 56=西班牙 39=阿根廷 86=意大利 34=爱沙尼亚 49=立陶宛 36=中国
HERO_SMS_COUNTRY_PREFER = [7, 52, 16, 56, 39, 86, 34, 49, 36]

# ---------------------------------------------------------------- 打码平台
# CapSolver 验证码打码平台
CAPSOLVER_API_KEY = _env("CAPSOLVER_API_KEY", "")

# EZ-Captcha 验证码打码平台
EZCAPTCHA_API_KEY = _env("EZCAPTCHA_API_KEY", "")
EZCAPTCHA_API_BASE = _env("EZCAPTCHA_API_BASE", "https://api.ez-captcha.com")

# ---------------------------------------------------------------- 标准 token 导出/上传
# 注册成功后落地的标准格式 token 目录（CPA codex / SUB2API content / grok sso）
TOKEN_OUTPUT_DIR = _env("TOKEN_OUTPUT_DIR", "tokens")

# CPA 管理接口（ChatGPT codex 授权文件导入）
CPA_URL = _env("CPA_URL", "")
CPA_MGMT_KEY = _env("CPA_MGMT_KEY", "")

# SUB2API 管理接口（ChatGPT codex-session 导入）
SUB2API_URL = _env("SUB2API_URL", "")
SUB2API_EMAIL = _env("SUB2API_EMAIL", "")
SUB2API_PASSWORD = _env("SUB2API_PASSWORD", "")
SUB2API_GROUP = _env("SUB2API_GROUP", "codex")  # 目标分组名，需先在 SUB2API 后台建好

# webchat2api（Grok sso 注入）
WEBCHAT2API_URL = _env("WEBCHAT2API_URL", "")
WEBCHAT2API_KEY = _env("WEBCHAT2API_KEY", "")

# chatgpt2api（basketikun/chatgpt2api 普通网页号导入，POST <url>/api/accounts）
# register_chatgpt.py --import-c2a 注册成功后逐个上传时用
CHATGPT2API_URL = _env("CHATGPT2API_URL", "")  # 对端 host（见 .env）
CHATGPT2API_KEY = _env("CHATGPT2API_KEY", "")  # 对端 admin key（Authorization: Bearer）

# ---------------------------------------------------------------- 订阅授权入口
# Codex / ChatGPT Plus：baxigpt.com（卡密 + 账号 access_token → 开通 Plus）
BAXI_API = _env("BAXI_API", "https://baxigpt.com")
# 卡密池：一个或多个 BX-XXXXXXXX，逗号/换行/空格分隔，方便批量
BAXI_CARDS = [c.strip().upper() for c in _env("BAXI_CARDS", "").replace("\n", ",").replace(" ", ",").split(",") if c.strip()]

# Claude / SuperGrok 订阅入口（激活码 CDK 流程「敬请期待」，后续支持授权到 SUB2API / CPA）
CLAUDE_SUB_URL = _env("CLAUDE_SUB_URL", "https://6661231.xyz/#/claude")
GROK_SUB_URL = _env("GROK_SUB_URL", "https://6661231.xyz/#/grok")
# 激活码 CDK 池（预留，逗号/换行/空格分隔）
CLAUDE_SUB_CDK = [c.strip() for c in _env("CLAUDE_SUB_CDK", "").replace("\n", ",").replace(" ", ",").split(",") if c.strip()]
GROK_SUB_CDK = [c.strip() for c in _env("GROK_SUB_CDK", "").replace("\n", ",").replace(" ", ",").split(",") if c.strip()]

# ---------------------------------------------------------------- ChatGPT OAuth add-phone 接码
# OpenAI/ChatGPT 在接码平台的服务号（按平台分，跟 Claude 的不同）
SMS_PROJECT_ID_OPENAI = _env("SMS_PROJECT_ID_OPENAI", "")  # firefox.fun 的 ChatGPT 项目 iid（待填）
HERO_SMS_SERVICE_OPENAI = _env("HERO_SMS_SERVICE_OPENAI", "dr")  # hero-sms/sms-activate OpenAI 服务码默认 dr
# firefox.fun 价格上限：'0' 只取最便宜(垃圾号易被 OpenAI 拒)，给够才摸得到智利等好号
SMS_MAXPRICE_OPENAI = _env("SMS_MAXPRICE_OPENAI", "20")
# OpenAI add-phone 拉黑的号段(dialing code)：261 马达加斯加、63 菲律宾 等 OpenAI 常拒的
SMS_COUNTRY_BLACKLIST_OPENAI = [c.strip() for c in _env("SMS_COUNTRY_BLACKLIST_OPENAI", "261,63").split(",") if c.strip()]
