import cloudbypass

APIKEY = ""

if __name__ == '__main__':
    url = "https://core-api.dextools.io/pool/events/ether/0x5f8fd2d971378478c1230ed1affceec99aa76de3/newest?limit=100"
    sess = cloudbypass.Session(apikey=APIKEY)
    resp = sess.request("GET", url, headers={
        "referer": "https://www.dextools.io/",
        "origin": "https://www.dextools.io",
        "content-type": "application/json",
        "X-Api-Version": "1",
    })

    print(f"Status: {resp.status_code}")
    print(f"body: {resp.text}")

    for _ in resp.json()['data']['events']:
        print(_)
