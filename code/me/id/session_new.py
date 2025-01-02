import cloudbypass

"""
请先安装依赖：
    pip install cloudbypass
"""

APIKEY = ""
PROXY = ""

sess = cloudbypass.Session(
    apikey=APIKEY,
    proxy=PROXY,
    part="0"
)

if __name__ == '__main__':
    resp = sess.request(
        "GET",
        "https://www.id.me/session/new",
    )

    assert resp.status_code == 200, f"Response Error: {resp.status_code}"

    print(f"重定向到：{resp.request.url}")

    resp = sess.request(
        "GET",
        "https://api.id.me/en/session/new"
    )

    print(f"Status: {resp.status_code}")
    print(f"Headers: {resp.headers}")
    print(f"Body: {resp.text}")
