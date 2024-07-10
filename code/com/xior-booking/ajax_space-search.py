import json
import re
import cloudbypass

APIKEY = ""
PROXY = ""  # Must be a fixed IP proxy

if __name__ == '__main__':
    url = "https://www.xior-booking.com/ajax/space-search"
    sess = cloudbypass.Session(apikey=APIKEY, proxy=PROXY)
    # 先访问 https://www.xior-booking.com/ 拿到csrf-token
    page_resp = sess.v2("GET", "https://www.xior-booking.com/")
    csrf_token = re.search(r'<meta\sname="csrf-token"\scontent="(.*?)">', page_resp.text)[1]
    print(f"csrf_token: {csrf_token}")

    resp = sess.v2("POST", url, headers={
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://www.xior-booking.com",
        "referer": "https://www.xior-booking.com/",
        "X-Csrf-Token": csrf_token
    }, data={
        "country": "276",
        "city": "32",
        "location": "54",
        "space_type": "",
        "min_price": "0",
        "max_price": "1555",
        "min_surface": "10",
        "max_surface": "116",
        "order": "",
        "unlock_key": "",
        "page": "1",
        "pagination": "true",
    })

    print(f"Status: {resp.status_code}")
    print(f"body: {resp.text}")

    print(json.dumps(resp.json(), indent=4))
