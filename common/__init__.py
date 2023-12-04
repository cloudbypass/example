import os

import requests
from urllib.parse import urlparse

ENV_APIKEY = os.environ.get("CB_APIKEY", "")
ENV_LOCAL_PROXY = os.environ.get("CB_LOCAL_PROXY", "127.0.0.1:1087")


class CloudbypassSession(requests.Session):
    def __init__(self, apikey=None,proxy=None):
        super().__init__()
        apikey = apikey or ENV_APIKEY
        assert apikey
        self.headers.update({
            "x-cb-apikey": apikey,
            "x-cb-proxy": proxy
        })

    def request(self, method, url, **kwargs):
        print(f"[{method}] {url}")
        url = urlparse(url)

        allow_redirects = kwargs.get("allow_redirects", True)
        options = set(kwargs.get("headers", {}).get("x-cb-options", "").split(","))
        if not allow_redirects:
            options.add("disable-redirect")

        headers = {
            "x-cb-host": url.hostname,
            "x-cb-protocol": url.scheme,
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


class CloudbypassLocalProxySession(requests.Session):
    def __init__(self, apikey=None, proxy=None):
        super().__init__()
        apikey = apikey or ENV_APIKEY
        assert apikey
        self.headers.update({
            "x-cb-apikey": apikey,
            "x-cb-proxy": proxy
        })

    def request(self, method, url, **kwargs):
        kwargs['proxies'] = {
            "http": ENV_LOCAL_PROXY,
            "https": ENV_LOCAL_PROXY,
        }
        return super().request(method, url, **kwargs)
