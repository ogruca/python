#!/usr/bin/python
import requests
from datetime import datetime as dt
from itertools import cycle
import traceback

url = "https://realpython.com/python-requests/"
#url = "https://trading.sharetrade.com.au/default.aspx?"
proxies = [ 
"https://username:password@10.139.219.51:8080",
"https://username:password@10.139.219.52:8080",
"https://username:password@10.137.219.53:8080",
"https://username:password@10.137.219.54:8080"]

proxy_pool = cycle(proxies)

with open("proxyresponse_realpython.txt", "a") as f:
    for i in range(1, 5): 
        proxy = next(proxy_pool)
        proxyredact = proxy.lstrip('username:password@')
        print('Requested Proxy is....' + proxyredact)
        now = dt.now()
        r = requests.get(url, proxies={"http": proxy, "https": proxy}, verify=False).elapsed.total_seconds()
        f.write(''.join(str(r) + ', ' + str(now) + ', ' + str(proxyredact) + "\n"))
