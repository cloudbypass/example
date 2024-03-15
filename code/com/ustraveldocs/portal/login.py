import bs4
import cloudbypass
import re
from bs4 import BeautifulSoup

"""
需要安装requests和beautifulsoup4,执行以下命令安装
pip install requests beautifulsoup4
"""

APIKEY = ""
PROXY = ""  # Must be a fixed IP proxy
USERNAME = ""
PASSWORD = ""
PART = "0"

session = cloudbypass.Session(apikey=APIKEY, proxy=PROXY)


def login():
    print(f"[login] {USERNAME}")
    print(f"[login] 获取登录页面表单...")
    resp_001 = session.request(
        "GET",
        f"https://portal.ustraveldocs.com/SiteLogin?refURL=http%3A%2F%2Fportal.ustraveldocs.com%2F",
        part=PART
    )

    assert resp_001.status_code == 200

    html = BeautifulSoup(resp_001.text, "html.parser")
    form_dict = {
        _.get("name"): _.get("value") for _ in html.select("input")
    }
    form_dict['loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:username'] = USERNAME
    form_dict['loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:password'] = PASSWORD
    form_dict['loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:j_id167'] = 'on'

    print(f"[login] 提交登录页面表单...")
    resp_002 = session.request(
        "POST",
        f"https://portal.ustraveldocs.com/SiteLogin?refURL=https://portal.ustraveldocs.com/applicanthome",
        part=PART,
        data=form_dict,
        headers={
            "Origin": "https://portal.ustraveldocs.com",
            "Referer": "https://portal.ustraveldocs.com/SiteLogin?refURL=https%3A%2F%2Fportal.ustraveldocs.com%2Fapplicanthome",
            "Content-Type": "application/x-www-form-urlencoded"
        }
    )
    assert resp_002.status_code == 200

    print(f"[login] 获取用户Cookie...")
    frontdoor_jsp = re.search(r"window.location.replace\('(.*?)'\)", resp_002.text).group(1)
    resp_003 = session.request(
        "GET",
        frontdoor_jsp,
        part=PART,
        headers={
            "Cookie": "; ".join([f"{cookie.name}={cookie.value}" for cookie in resp_002.cookies]),
            "Referer": "https://portal.ustraveldocs.com/Unauthorized?startURL=%2Fapplicanthome&refURL=http%3A%2F%2Fportal.ustraveldocs.com%2Fapplicanthome",
        }
    )

    assert resp_003.status_code == 200

    print("完成登录操作")


if __name__ == '__main__':
    login()

    # 输出cookie(js代码)
    cookie_js = "\n".join([f"await cookieStore.set('{cookie.name}', '{cookie.value}');" for cookie in session.cookies])
    print(cookie_js)
