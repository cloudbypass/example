from common import CloudbypassSession
import base64
import random
from Crypto.Hash import MD5
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
from urllib.parse import urlparse

"""
Install dependencies: 
pip install requests
pip install pycryptodome
"""


def encrypt(plaintext, password):
    # generate a random salt
    salt = bytes([random.randint(0, 0xFF) for _ in range(8)])

    # derive a key and IV from the password and salt
    derived = b""
    while len(derived) < 48:  # "key size" + "iv size" (8 + 4 magical units = 12 * 4 = 48)
        hasher = MD5.new()
        hasher.update(derived[-16:] + password.encode('utf-8') + salt)
        derived += hasher.digest()

    # "8" key size = 32 actual bytes
    key = derived[0:32]
    iv = derived[32:48]

    # pad plaintext
    plaintext = plaintext.encode('utf-8')
    plaintext = pad(plaintext, 16)

    # encrypt
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(plaintext)

    # prepend the salt and return
    return base64.b64encode(b"Salted__" + salt + ciphertext)


if __name__ == '__main__':
    USERNAME = ""
    PASSWORD = r""
    with CloudbypassSession() as session:
        key_resp = session.get("https://shop.pockyt.io/v1/gc/account/8ILXWsvC/login/key")

        assert key_resp.status_code == 200
        data = key_resp.json()
        print(data)

        password_encrypted = encrypt(PASSWORD, data['result']['secret'])

        login_resp = session.post("https://shop.pockyt.io/v1/gc/account/8ILXWsvC/login",
                                  headers={
                                      "Content-Type": "application/json; charset=utf-8"
                                  },
                                  json={
                                      "key_id": data['result']['key_id'],
                                      "password": password_encrypted.decode('utf-8'),
                                      "email": USERNAME,
                                      "method": "password",
                                      "timezone_area": "Asia/Shanghai"
                                  })

        assert login_resp.status_code == 200
        print("Login success!")
        print(login_resp.json())
