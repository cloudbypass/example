import base64
import time
import cloudbypass
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA

"""
Credit consumption: 3
https://visa.vfsglobal.com/chn/zh/deu/login

Install dependencies:
    pip install pycryptodome cloudbypass
"""

PUBLIC_KEY = b"""-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCpigN3/5Ti/WJk51pbPQdpCe96
TPVoeMAk/cUlAPpYh8zGpr6zssbM11Je1SoQTiuipxIL+c0oGXti8vLzln3yfS+N
56wuSh0Hyt1Z+waSx6IDFlfzImEtq8m1osS32B83HRiFZbeKB8QIRJhZil1pJSzM
sg0Y0QmDyv1yR4FzIQIDAQAB
-----END PUBLIC KEY-----"""

APIKEY = ""
PROXY = ""  # Must be a fixed IP proxy
USERNAME = ""
PASSWORD = ""  # Password before encryption


def btoa(s):
    return base64.b64encode(s).decode()


def encriptionPassword(o):
    public_key = RSA.importKey(PUBLIC_KEY)
    cipher = PKCS1_v1_5.new(public_key, None)
    return btoa(cipher.encrypt(o.encode()))


if __name__ == '__main__':
    current_time = time.strftime("GA;%Y-%m-%dT%H:%M:%SZ", time.localtime())

    client_source = encriptionPassword(current_time)
    password_enc = encriptionPassword(PASSWORD)

    # login
    resp = cloudbypass.Session(apikey=APIKEY, proxy=PROXY).post(
        "https://lift-apicn.vfsglobal.com/user/login",
        headers={
            "Accept": r"application/json, text/plain, */*",
            "Accept-Language": r"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Content-Type": r"application/x-www-form-urlencoded",
            "Origin": r"https://visa.vfsglobal.com",
            "Referer": r"https://visa.vfsglobal.com/",
            "Route": r"chn/zh/deu",
            "x-cb-version": "2",
            "x-cb-sitekey": "0x4AAAAAAACYaM3U_Dz-4DN1",
            "Clientsource": client_source
        },
        data={
            "username": USERNAME,
            "password": password_enc,
            "missioncode": r"deu",
            "countrycode": r"chn",
            "captcha_version": "cloudflare-v1",
            "captcha_api_key": "[cf_token]"
        }
    )

    print(resp.status_code)
    print(resp.text)