# -*- coding: utf-8 -*-
import logging
import requests
import os
import time
result = b'success\n'
# url
url = "http://www.yecaibuluo.com/portal/api/checkIn"
# time
timenow = int(time.time())
# cookie
cookie = "guest_token=38451e2faf1542d39051c2529a361161; Hm_lvt_2951eff0d8a1ff6008f24d727c6fe8dd=1650446775; Hm_lpvt_2951eff0d8a1ff6008f24d727c6fe8dd="+str(timenow)

payload = "{\"code\":\"\",\"email\":\"825222733\"}"
headers = {
  'accept': 'application/json, text/plain, */*',
  'dnt': '1',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36',
  'content-type': 'application/json;charset=UTF-8',
  'origin': 'http://www.yecaibuluo.com',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'http://www.yecaibuluo.com/',
  'accept-language': 'zh-CN,zh;q=0.9',
  'cookie': cookie
}
def do_action():
    logger = logging.getLogger()
    response = requests.request("POST", url, headers=headers, data = payload)
    result = response.text.encode('utf8')
    logger.info(result)
    print(result)
    return result


if __name__ == '__main__':
    do_action()
