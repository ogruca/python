#!/usr/bin/python
import requests
from datetime import datetime as dt
from itertools import cycle
import traceback

url = "https://realpython.com/python-requests/"
url2 = "https://trading.sharetrade.com.au/default.aspx?"
url3 = "https://github.com"
proxies = [
"https://s34866:xxxxx@10.139.219.51:8080",
"https://s34866:xxxxx@10.139.219.52:8080",
"https://s34866:xxxxx@10.137.219.53:8080",
"https://s34866:xxxxx@10.137.219.54:8080"]

proxy_pool = cycle(proxies)

# open the file realpython as append and cycle through the proxies
with open("proxyresponse_realpython.txt", "a") as f:
    for i in range(1, 5):
        proxy = next(proxy_pool)
        proxyredact = proxy.lstrip('https://s34866:Home4504@')
        print('Requested Proxy is....' + proxyredact)
        now = dt.now()
        r = requests.get(url, proxies={"http": proxy, "https": proxy}, verify=False).elapsed.total_seconds()
        f.write(''.join(str(r) + ',' + str(now) + ',' + str(proxyredact) + ',' + url + "\n"))

with open("proxyresponse_suncorpsharetrade.txt", "a") as f:
     for i in range(1, 5):
         proxy = next(proxy_pool)
         proxyredact = proxy.lstrip('https://s34866:Home4504@')
         print('Requested Proxy is....' + proxyredact)
         now = dt.now()
         r = requests.get(url2, proxies={"http": proxy, "https": proxy}, verify=False).elapsed.total_seconds()
         f.write(''.join(str(r) + ',' + str(now) + ',' + str(proxyredact) + ',' + url2 + "\n"))

with open("proxyresponse_github.txt", "a") as f:
     for i in range(1, 5):
         proxy = next(proxy_pool)
         proxyredact = proxy.lstrip('https://s34866:Home4504@')
         print('Requested Proxy is....' + proxyredact)
         now = dt.now()
         r = requests.get(url3, proxies={"http": proxy, "https": proxy}, verify=False).elapsed.total_seconds()
         f.write(''.join(str(r) + ',' + str(now) + ',' + str(proxyredact) + ',' + url3 + "\n"))
