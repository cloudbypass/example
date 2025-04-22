import time

import cloudbypass

"""
请先安装依赖：
    pip install cloudbypass
"""

APIKEY = ""
PROXY = ""  # 时效地址
ADDRESS = ""  # 领水地址

sess = cloudbypass.SessionV2(
    apikey=APIKEY,
    proxy=PROXY
)

if __name__ == '__main__':
    resp = sess.request(
        "GET",
        "https://testnet.monad.xyz/",
        headers={
            "x-cb-fp": "edge133-win"
        }
    )
    assert resp.status_code == 200, f"Page Response {resp.status_code}"

    resp = sess.request(
        "POST",
        "https://faucet-claim.molandak.org/",
        headers={
            "x-cb-fp": "edge133-win",
            "x-cb-sitekey": "0x4AAAAAAA-3X4Nd7hf3mNGx",
            "origin": "https://testnet.monad.xyz",
            "referer": "https://testnet.monad.xyz/",
        },
        json={
            "address": ADDRESS,
            "visitorId": "10e2c513898abfe8303e3973b0f0eb99",
            "cloudFlareResponseToken": "[cf_token]"
        }
    )

    print(f"Status: {resp.status_code}")
    print(f"Headers: {resp.headers}")
    print(f"Body: {resp.text}")
