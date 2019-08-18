import os
import time as delay
from pyquery import PyQuery as pq
import urllib3 as url
import requests as req

class Wiki:
    def main():
        user = str(input("[Search] >_ "))
        net = req.get("https://en.wikipedia.org/wiki/" + user)
        if net.status_code == 200:
            print("[V] Here's the result we found")
            data = pq(net.text)
            print(data("p").text())
        else:
            print("[!] No Result Found !")

# run = Wiki
# run = Wiki.main()