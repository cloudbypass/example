import cloudbypass

"""
请先安装依赖：
    pip install cloudbypass bs4 web3
"""

APIKEY = ""
PROXY = ""

sess = cloudbypass.SessionV2(
    apikey=APIKEY,
    proxy=PROXY
)

if __name__ == '__main__':
    resp = sess.request(
        "POST",
        "https://multichain-api.birdeye.so/multichain/v2/gems/new_listing",
        headers={
            "Agent-Id": "6cb7aad5-d0de-4153-b606-54de23e967cc",
            "Origin": "https://birdeye.so",
            "Referer": "https://birdeye.so/",
        },
        json={
            "sort_by": "createdAt",
            "sort_type": "desc",
            "offset": 0,
            "limit": 10,
            "filters": [
                {
                    "field": "createdAt",
                    "operator": "gte",
                    "value": "now-7d/s"
                }
            ]
        }
    )

    print(f"Status: {resp.status_code}")
    print(f"Headers: {resp.headers}")
    print(f"body: {resp.text}")