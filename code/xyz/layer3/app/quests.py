import json
import cloudbypass

APIKEY = ""
PROXY = ""  # Optional

if __name__ == '__main__':
    url = "https://app.layer3.xyz/quests"
    sess = cloudbypass.Session(apikey=APIKEY, proxy=PROXY)
    resp = sess.get(url)

    print(f"Status: {resp.status_code}")
    print(f"body: {resp.text}")
