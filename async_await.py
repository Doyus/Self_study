# python 为了将语义变得更加明确，就引入了async和wait关键词用于定义原生协程

async def downloader(url):
    return "bobby"

async def downloader_url(url):
    html = await downloader(url)

    return html

if __name__ == "__main__":
    coro = downloader_url("http://www.imooc.com")
    coro.send(None)