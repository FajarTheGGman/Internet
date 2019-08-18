import os
import time as delay
from pyquery import PyQuery as pq
import urllib3 as url
import requests as req

class Search:
    def net():
        user = str(input("[?] >_ "))
        print("\n[/] Please Wait....\n")
        setupNet = url.PoolManager()
        reqData = setupNet.request("GET", "http://www1.search-results.com/web?q=" + user)
        parsing = pq(reqData.data)
        title = parsing(".algo-title").text()
        a = parsing("cite.algo-display-url").text()
        print("\n[!] Here's The Result \n")
        print(a)

    def userAgent():
        user = str(input("[?] >_ "))
        print("\n[/] Please Wait....\n")
        setupNet = url.PoolManager(header="Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36")
        reqData = setupNet.request("GET", "http://www1.search-results.com/web?q=" + user)
        parsing = pq(reqData.data)
        title = parsing(".algo-title").text()
        a = parsing("cite.algo-display-url").text()
        print("\n[!] Here's The Result \n")
        print(a)

s = Search