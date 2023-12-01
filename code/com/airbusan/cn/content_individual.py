import os

from common import CloudbypassSession

if __name__ == '__main__':
    with CloudbypassSession() as session:
        resp = session.get("https://cn.airbusan.com/content/individual/?", headers={
            "x-cb-version": "2",
            "x-cb-part": "0",
            "x-cb-proxy": os.environ.get("PROXY"),  # 部分IP禁止访问
        })
        print(resp.status_code, resp.headers.get("x-cb-status"))
        print(resp.text)
