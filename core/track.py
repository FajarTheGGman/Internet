import os
import time as delay
from pyquery import PyQuery as pq
import urllib3 as url
import requests as req
import json

class Track:
    def main():
        ip = str(input("[Input IP] >_ "))
        s = req.get("http://ip-api.com/json/" + ip)
        a = json.loads(s.text)
        print("\n----[Result]----")
        print("[ISP] > " + str(a['isp']))
        print("[IP] > " + str(a['query']))
        print("[CITY] > " + str(a['city']))
        print("[MAPS] > " + "https://maps.google.com/" + str(a['lat']) + ", " + str(a['lon']))