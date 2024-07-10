import json
import cloudbypass

APIKEY = ""

if __name__ == '__main__':
    url = "https://www.dextools.io/shared/data/pair?address=0x5f8fd2d971378478c1230ed1affceec99aa76de3&chain=ether&audit=true&locks=true"
    sess = cloudbypass.Session(apikey=APIKEY)
    resp = sess.request("GET", url, headers={
        "referer": "https://www.dextools.io/app/cn/ether/pair-explorer/0x5f8fd2d971378478c1230ed1affceec99aa76de3?t=1720514005411",
        "content-type": "application/json"
    })

    print(f"Status: {resp.status_code}")
    print(f"body: {resp.text}")

    print(json.dumps(resp.json()['data'], indent=4))
