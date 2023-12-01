import os

from common import CloudbypassSession

if __name__ == '__main__':
    with CloudbypassSession() as session:
        resp = session.get("https://etherscan.io/accounts/label/lido", headers={
            "x-cb-version": "2",
            "x-cb-part": "0",
            "x-cb-proxy": os.environ.get("PROXY"),
        })
        print(resp.status_code, resp.headers.get("x-cb-status"))
        print(resp.text)
