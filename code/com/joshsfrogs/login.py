import cloudbypass

"""
安装依赖：
    pip install cloudbypass

填写以下参数即可运行
"""

APIKEY = ""
PROXY = ""  # 必须是固定IP的代理，否则cf_token会生成超时
EMAIL = ""
PASSWORD = ""

session = cloudbypass.Session(apikey=APIKEY, proxy=PROXY)

if __name__ == '__main__':
    resp = session.post(
        "https://joshsfrogs.com/login",
        headers={
            "X-Cb-Sitekey": "0x4AAAAAAAFbs7Y-lYoVcAK2",
            "Origin": "https://joshsfrogs.com",
            "Referer": "https://joshsfrogs.com/account/login",
            "X-Turnstile-Response": "[cf_token]",  # 此处是cf_token填充，勿动
            "Content-Type": "application/json"
        },
        json={
            "username": EMAIL,
            "password": PASSWORD
        },
        part="0"
    )

    print(f"Status Code: {resp.status_code}")
    print(f"Body: {resp.json()}")
