import cloudbypass

"""
安装依赖：
    pip install cloudbypass
    
填写以下3个参数即可运行
"""

APIKEY = ""
PROXY = ""  # 必须是时效IP代理
ADDRESS = ""

if __name__ == '__main__':
    resp = cloudbypass.post(
        f"https://artio-80085-faucet-api-cf.berachain.com/api/claim?address={ADDRESS}",
        headers={
            "X-Cb-Sitekey": "0x4AAAAAAARdAuciFArKhVwt",
            "Referer": "https://artio.faucet.berachain.com/",
            "Authorization": "Bearer [cf_token]"
        },
        json={"address": ADDRESS},
        apikey=APIKEY,
        proxy=PROXY,
        part="0"
    )

    print(f"Status code: {resp.status_code}")
    print(f"Result: {resp.text}")
