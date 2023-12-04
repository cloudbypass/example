from bs4 import BeautifulSoup

from common import CloudbypassLocalProxySession

if __name__ == '__main__':
    APIKEY = ""  # 环境变量 CB_APIKEY
    PROXY = ""  # 时效代理IP
    USERNAME = ""
    PASSWORD = r""

    session = CloudbypassLocalProxySession(apikey=APIKEY, proxy=PROXY)

    # 先请求一次首页 获取到XSRF-TOKEN
    home_page_resp = session.get("https://visas-fr.tlscontact.com/visa/gb/gbMNC2fr/home")

    assert home_page_resp.status_code == 200

    # 获取登录页面
    login_page_resp = session.get("https://visas-fr.tlscontact.com/oauth2/authorization/oidc")

    assert login_page_resp.status_code == 200

    # 解析登录页面 form#kc-form-login
    login_page_soup = BeautifulSoup(login_page_resp.text, "html.parser")
    login_form = login_page_soup.select_one("form#kc-form-login")
    login_url = login_form.attrs.get("action")

    # 发起登录请求
    login_resp = session.post(login_url, headers={
        "Content-Type": "application/x-www-form-urlencoded",
    }, data={
        "username": USERNAME,
        "password": PASSWORD,
    })

    print(f"login_resp: {login_resp.status_code}")

    account_resp = session.get("https://visas-fr.tlscontact.com/api/account", )

    print(f"account_resp: {account_resp.status_code}")
    print(account_resp.json())
