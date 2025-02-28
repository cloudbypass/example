import cloudbypass

"""
安装依赖：
    pip install cloudbypass

填写以下参数即可运行
"""

APIKEY = ""
EMAIL = ""
PROXY = ""

if __name__ == '__main__':
    url = "https://www.cityline.com/api/otp.do"
    sess = cloudbypass.SessionV2(apikey=APIKEY, proxy=PROXY)
    resp = sess.request("POST", url, headers={
        "x-cb-sitekey": "0x4AAAAAAAVyjzMBC6Sst-qW",
        "referer": "https://www.cityline.com/zh_HK/Login.html",
        "origin": "https://www.cityline.com",
    }, json={
            "accessToken": "[cf_token]",
        "email": EMAIL,
        "locale": "zh_HK"
    })

    print(f"Status: {resp.status_code}")
    print(f"body: {resp.text}")
