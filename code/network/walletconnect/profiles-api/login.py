import json
import cloudbypass
from datetime import datetime, timezone
from eth_account.messages import encode_defunct
from eth_account.signers.local import LocalAccount
from web3 import Web3

"""
请先安装依赖：
    pip install cloudbypass web3
"""

APIKEY = ""
PROXY = ""  # IP必须固定不然会返回403
PRIVATE_KEY = ""  # 钱包私钥

sess = cloudbypass.Session(
    apikey=APIKEY,
    proxy=PROXY
)

if __name__ == '__main__':
    resp_token = sess.request(
        "GET",
        "https://profiles-api.walletconnect.network/auth/v1/nonce?projectId=380bc865991c240077e38ea3dd9d6fef&st=w3m&sv=5.0.0",
        headers={
            "origin": "https://airdrop.walletconnect.network",
            "referer": "https://airdrop.walletconnect.network/",
            "x-cb-ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
        }
    )
    data = resp_token.json()
    token = data['token']
    nonce = data['nonce']
    print(f"token: {token}")
    print(f"nonce: {nonce}")

    # 初始化 Web3
    web3 = Web3()

    account: LocalAccount = web3.eth.account.from_key(PRIVATE_KEY)
    address = account.address

    dt = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    message = f"airdrop.walletconnect.network wants you to sign in with your Ethereum account:\n{address}\n\nThis won't perform any transactions on your behalf and won't cost any gas fees. Please sign the following message with your account.\n\nURI: https://airdrop.walletconnect.network\nVersion: 1\nChain ID: 10\nNonce: {nonce}\nIssued At: {dt}"
    message_hash = web3.keccak(text=message)
    encode_defunct(text=message)

    signature = "0x" + account.sign_message(encode_defunct(text=message)).signature.hex()

    print(f"signature: {signature}")
    resp = sess.request(
        "POST",
        "https://profiles-api.walletconnect.network/auth/v1/authenticate?projectId=380bc865991c240077e38ea3dd9d6fef&st=w3m&sv=5.0.0",
        headers={
            "accept": "*/*",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "authorization": f"Bearer {token}",
            "content-type": "text/plain;charset=UTF-8",
            "origin": "https://airdrop.walletconnect.network",
            "referer": "https://airdrop.walletconnect.network/",
            "x-cb-ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
        },
        data=json.dumps({"message": message, "signature": signature})
    )

    print(f"Status: {resp.status_code}")
    print(f"Headers: {resp.headers}")
    print(f"body: {resp.text}")
