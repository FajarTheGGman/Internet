import requests as req

class Whois:
    def main():
        user = str(input("[Input Website] (Without http / https) >_ "))
        s = req.get("https://api.hackertarget.com/whois/?q=" + user)
        print("\n+----[Result]----+")
        print(req.text)