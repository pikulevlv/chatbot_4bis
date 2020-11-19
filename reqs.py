import requests
import sys
import locale
from requests_toolbelt import MultipartEncoder
from requests_toolbelt import user_agent
import requests
import aiohttp
import asyncio #  [1]

arg = '000032398'
u = 'Интеграция'
p = 'q12345'
url = 'http://37.19.1.247/4bis_itilium_dev3/ru_RU/hs/Telegram/info/order?order='


def func1():
    r = requests.get(url + arg, auth=(u.encode('utf-8').decode('latin1'), p))  # .json()

    r.encoding = 'utf-8-sig'
    print(type(r.status_code), r.status_code)
    print(type(r.content), r.content)
    print(type(r.headers), r.headers)
    print(type(r.text), r.text)
    raw = r.text.split(', ')
    print(raw)
    d = {}
    for r in raw:
        kv = r.split(' : ')
        d[kv[0]] = kv[1]
    print(d)


async def func2(u, p, url, arg):
    async with aiohttp.ClientSession() as session:
        async with session.get(url + arg, auth=aiohttp.BasicAuth(u.encode('utf-8').decode('latin1'), p)) as resp:
            raw = await resp.text()
            raw = raw.split(', ')
            d = {}
            for r in raw:
                kv = r.split(' : ')
                d[kv[0]] = kv[1]
            print(d)
            return d

if __name__ == '__main__':
    func1()
    asyncio.run(func2(u, p, url, arg))




