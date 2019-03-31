import aiohttp
import re
import aiomysql
import asyncio
from pyquery import PyQuery

start_url = 'http://www.jobbole.com/'
waitting_urls = []
seen_urls = set()
stopping = False

async def fetch(url, session):
    try:
        async with session.get(url) as resp:
            print("url status: {}".format(resp.status))
            if resp.status in [200, 201]:
                print(await resp.text())
                data = await resp.text()
                return data
    except Exception as e:
        print(e)


async def main(loop):
    pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                      user='root', password="",
                                      charset='utf8', autocommit=True)
def extrac_urls(html):
    urls = []
    pq = PyQuery(html)
    for link in pq.items("a"):
        url = link.attr("href")
        if url and url.startwidth("http") and url not in seen_urls:
            urls.append(url)
            waitting_urls.append(url)

        return urls

async def article_handler(url, session):
    # 获取文章详细并解析入库
    html = await fetch(url, session)
    extrac_urls(html)
    pq = PyQuery(html)
    title = pq("title")


async def init_urls():
    html = await fetch(start_url)
    extrac_urls(html)

async def consumer():
    async with aiohttp.ClientSession() as session:
        while not stopping:
            if len(waitting_urls) == 0:
                await asyncio.sleep(0.5)
            url = waitting_urls.pop()
            print("start get url: {}".format(url))
            if re.match('http://.*?jobbole.com/\d+/',url):
                if url not in seen_urls:
                    asyncio.ensure_future(article_handler(url,session))







