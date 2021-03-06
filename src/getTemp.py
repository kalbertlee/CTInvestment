#!/usr/bin/python3

import requests
import json
from config import TOKEN

zhishu_url = "https://open.lixinger.com/api/a/index/fundamental"

header = {
    "Content-Type": "application/json"
}

class Temperature:
    pass
    
def get(code, date):
    data = json.dumps({
        "token": TOKEN,
        "date": date,
        "stockCodes": code,
        "metricsList": ["pe_ttm.y10.mcw","pe_ttm.mcw","mc"]
    })
    res = requests.post(zhishu_url, headers=header, data=data, verify=False)
    if res.status_code == 200:
        res_array = json.loads(res.text)
        print(res_array)
    else:
        print("[-] Error {STATUS_CODE}".format(STATUS_CODE=res.status_code))
    
scode = ["000016"]
currtime = "2021-01-04"
get(scode, currtime)
    


