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
        "POST",
        "https://multichain-api.birdeye.so/solana/amm/v2/txs/token",
        headers={
            "Agent-Id": "6cb7aad5-d0de-4153-b606-54de23e967cc",
            "Origin": "https://birdeye.so",
            "Referer": "https://birdeye.so/",
        },
        json={
            "offset": 0,
            "limit": 15,
            "export": False,
            "query": [
                {
                    "keyword": "volumeUSD",
                    "operator": "lt", "value": 1000
                }
            ],
            "sort_by": "",
            "sort_type": ""
        }
    )

    print(f"Status: {resp.status_code}")
    print(f"Headers: {resp.headers}")
    print(f"body: {resp.text}")
