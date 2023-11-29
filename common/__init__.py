import os

import requests
from urllib.parse import urlparse

ENV_APIKEY = os.environ.get("CB_APIKEY", "")


class CloudbypassSession(requests.Session):
    def __init__(self, apikey=None):
        super().__init__()
        apikey = apikey or ENV_APIKEY
        assert apikey
        self.headers.update({
            "x-cb-apikey": apikey
        })

    def request(self, method, url, proxy=None, **kwargs):
        print(f"[{method}] {url}")
        url = urlparse(url)

        allow_redirects = kwargs.get("allow_redirects", True)
        options = set(kwargs.get("headers", {}).get("x-cb-options", "").split(","))
        if not allow_redirects:
            options.add("disable-redirect")

        headers = {
            "x-cb-apikey": APIKEY,
            "x-cb-host": url.hostname,
            "x-cb-protocol": url.scheme,
            "x-cb-proxy": proxy,
            "x-cb-options": ",".join(options)
        }
        if kwargs.get("headers"):
            kwargs['headers'].update(headers)
        else:
            kwargs['headers'] = headers

        return super().request(
            method,
            f"https://api.cloudbypass.com{url.path}" + (f"?{url.query}" if url.query else ""),
            **kwargs
        )
