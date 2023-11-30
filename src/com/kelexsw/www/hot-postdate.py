from common import CloudbypassSession

if __name__ == '__main__':
    with CloudbypassSession() as session:
        resp = session.get("https://www.kelexsw.com/hot-postdate.html")
        print(resp.status_code, resp.headers.get("x-cb-status"))
        print(resp.text)
