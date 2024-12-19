import bs4
import cloudbypass
from eth_account.messages import encode_defunct
from eth_account.signers.local import LocalAccount
from web3 import Web3

"""
请先安装依赖：
    pip install cloudbypass bs4 web3
"""

APIKEY = ""
PROXY = ""
# 用户的以太坊私钥（注意不要公开私钥）
PRIVATE_KEY = ""

sess = cloudbypass.Session(
    apikey=APIKEY,
    proxy=PROXY
)

if __name__ == '__main__':
    # 请求 https://genesis.alignedfoundation.org/terms-conditions 获取 Cookie
    print("访问 https://genesis.alignedfoundation.org/terms-conditions 获取Cookie")
    resp_001 = sess.request("GET", "https://genesis.alignedfoundation.org/terms-conditions")
    assert resp_001.status_code == 200, f"Response Error: {resp_001.status_code} {resp_001.text}"

    # 获取 csrf nonce
    print("访问 https://genesis.alignedfoundation.org/eligible 获取csrf nonce")
    resp_002 = sess.request("GET", "https://genesis.alignedfoundation.org/eligible")
    assert resp_002.status_code == 200, f"Response Error: {resp_002.status_code} {resp_002.text}"

    # 解析HTML数据
    html = bs4.BeautifulSoup(resp_002.text, "html.parser")
    csrf = html.select_one("meta[name=csrf-token]").get("content")
    nonce = html.select_one("#nonce").get("value")
    print(f"获取到csrf: {csrf} nonce:{nonce}")

    # 初始化 Web3
    web3 = Web3()
    account: LocalAccount = web3.eth.account.from_key(PRIVATE_KEY)
    address = account.address

    # 签名
    message = f"AlignedNonce:{nonce}"
    signature = "0x" + account.sign_message(encode_defunct(text=message)).signature.hex()
    print(f"签名: {signature}")

    resp = sess.request(
        "POST",
        "https://genesis.alignedfoundation.org/eligible",
        headers={
            "origin": "https://genesis.alignedfoundation.org",
            "referer": "https://genesis.alignedfoundation.org/eligible",
            "content-type": "application/x-www-form-urlencoded"
        },
        data={
            "_csrf_token": csrf,
            "address": address,
            "network": "ethereum",
            "signature": signature,
        }
    )

    print(f"Status: {resp.status_code}")
    print(f"Headers: {resp.headers}")
    print(f"body: {resp.text}")
