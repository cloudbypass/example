import cloudbypass

"""
请先安装依赖：
    pip install cloudbypass
"""
APIKEY = ""  # 环境变量 CB_APIKEY
PROXY = ""  # 时效代理IP

sess = cloudbypass.Session(
    apikey=APIKEY,
    proxy=PROXY,
    part="1"
)

if __name__ == '__main__':
    resp = sess.request(
        "GET",
        f"https://fr.tlscontact.com/oauth2/authorization/oidc",
        headers={
            "x-cb-fp": "safari-ios",
            "issuer": "gbLON2fr",
        },
        # allow_redirects=False
    )

    print(f"Status: {resp.status_code}")
    print(f"Headers: {resp.headers}")
    print(f"body: {resp.text}")
