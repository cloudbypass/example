import cloudbypass

"""
请先安装依赖：
    pip install cloudbypass
"""

APIKEY = ""
PROXY = ""

sess = cloudbypass.Session(
    apikey=APIKEY,
    proxy=PROXY
)

if __name__ == '__main__':
    resp = sess.request(
        "GET",
        "https://gmgn.ai/vas/api/v1/token_holders/sol/EV89We3N4ELQbNAeHwBmkVSCDtesKKq8HYvG2X2xXZhy?device_id=b6622a0f-824b-4e9d-8d59-72ee337d84ce&client_id=gmgn_web_20250627-462-10272bf&from_app=gmgn&app_ver=20250627-462-10272bf&tz_name=Asia%2FTokyo&tz_offset=32400&app_lang=zh-CN&fp_did=fb32e7e8861693529ceb6dd211929447&os=web&limit=100&cost=20&orderby=amount_percentage&direction=desc",
        headers={
            "origin": "https://www.dextools.io",
            "referer": "https://www.dextools.io/"
        }
    )

    print(f"Status: {resp.status_code}")
    print(f"Headers: {resp.headers}")
    print(f"body: {resp.text}")
