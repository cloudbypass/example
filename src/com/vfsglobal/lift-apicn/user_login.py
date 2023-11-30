import os

from common import CloudbypassSession

if __name__ == '__main__':
    with CloudbypassSession() as session:
        resp = session.post("https://lift-apicn.vfsglobal.com/user/login", headers={
            "Content-Type": r"application/x-www-form-urlencoded",
        }, data={
            "username": r"123456789@gmail.com",
            "password": r"bar aGeuD9BRJFyzzCm5H0RbrEqdU9WJnUvXvcmKkVhpfmEn5ScHs01ZdzG4xePfN1ofFSdEPIKLrA73RdzkSiwis  mKDa481k8SiRVbTQLI5ccdOdhDON4HO01qjJr3tGpQ6GOTZelHnX0DDIaY5kuDZkxWJGB/ uHzcfqF4E=",
            "missioncode": r"deu",
            "countrycode": r"chn",
        })
        print(resp.status_code, resp.headers.get("x-cb-status"))
        print(resp.text)
