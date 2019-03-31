import requests
from urllib.parse import urlencode
from requests.exceptions import ConnectionError
from pyquery import PyQuery as pq

base_url = 'https://weixin.sogou.com/weixin?'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'CXID=495FEB2962486D895535550C25FE27C9; SUID=524F45794B238B0A5BED37070000E903; wuid=AAEeFhYUJAAAAAqLE2NdfQ0AGwY=; SUV=00C9314079454F525C23460088FB6675; GOTO=Af22644-4372; IPLOC=CN1100; ad=OQpmvZllll2bEFt4lllllVe4MBllllllWUq5UkllllylllllVZlll5@@@@@@@@@@; ABTEST=4|1548469013|v1; weixinIndexVisited=1; JSESSIONID=aaakN4SXB03YxcureO5Hw; sct=3; ppinf=5|1548470016|1549679616|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo3MjolRTglQUUlQTklRUElQUYlQUQlRTUlQUQlOTAlRUElQUYlQUQlRTUlQkMlQjklRUElQUYlQUQlRTglQkYlQkQlRUElQUYlQUR8Y3J0OjEwOjE1NDg0NzAwMTZ8cmVmbmljazo3MjolRTglQUUlQTklRUElQUYlQUQlRTUlQUQlOTAlRUElQUYlQUQlRTUlQkMlQjklRUElQUYlQUQlRTglQkYlQkQlRUElQUYlQUR8dXNlcmlkOjQ0Om85dDJsdUNseUpuTlpRdnc4bVktRFZsa0trMk1Ad2VpeGluLnNvaHUuY29tfA; pprdig=xJV5XtA2ga3uGfuQVj5osWbDsLeBTjqWpY7gbEa1_JqR_E-0W70O4yCa0idgCX6j3j_FLOVfoLf6QG3TPr6woGjsAmwmAMrPGI9O58eV-9fhld9YV7L5tRDmfrsXZkQbmJsmeU_QkS0eBHMBe6Lwy9V8PNiSbk6kDveUKuXGMp4; sgid=24-38946982-AVxLxwAPstEcgicwxhXwYY1o; ppmdig=154847001600000074272742c62a3cbe9653c36024cb3ad3; PHPSESSID=h1d063llm81uatv9epjae3ali7; SNUID=970F07ADC3C643909B928719C32C2F63; seccodeRight=success; successCount=1|Sat, 26 Jan 2019 02:44:11 GMT',
    'Host': 'weixin.sogou.com',
    'Referer': 'https://weixin.sogou.com/weixin?query=%E9%A3%8E%E6%99%AF&_sug_type_=&s_from=input&_sug_=n&type=2&page=10&ie=utf8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}
proxy = None
max_count = 1000
def get_html(url, count=1):
    print('Crawling', url)
    print('Trying Count', count)
    global proxy
    if count >= max_count:
        print('Tried Too Many Counts')
        return None
    try:
        if proxy:
            proxies = {
                'http': 'http://' + proxy
            }
            response = requests.get(url,allow_redirects=False, headers=headers, proxies=proxies)
        else:
            response = requests.get(url,allow_redirects=False, headers=headers)
        #response = requests.get(url, allow_redirects=False, headers=headers) #不让他自动处理redirect
        # 如果正常判断状态码并返回结果
        if response.status_code == 200:
            return response.text
        if response.status_code == 302:
            print('302')
            proxy = get_proxy()
            count += 1
            if proxy:
                print('Using proxy', proxy)
                count += 1
                return get_html(url,count)
            else:
                print('get proxy failed')
                #count += 1
                #return get_html(url, count)
                return None


    except ConnectionError:
        # 如果捕获异常则递归调用自己
        print('Error occurred', e.args)
        proxy = get_proxy()
        return get_html(url, count)


def get_proxy():
    try:
        response = requests.get('http://127.0.0.1:5000/get')
        if response.status_code == 200:
            print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',response.text)
            return response.text
        return None
    except ConnectionError:
        return None
def get_index(keyword, page):
    data = {
        'query': keyword,
        'type': 2,
        'page': page
    }
    queries = urlencode(data)
    url = base_url + queries
    print(url)
    html = get_html(url)
    return html

def parse_index(html):
    doc = pq(html)
    items = doc('.news-box .new-list li .txt-box h3 a').items()
    for item in items:
        yield item.attr('href')


def parse_detail(html):
    try:
        doc = pq(html)
        title = doc('.rich_media_title').text()
        content = doc('.rich_media_content').text()
        date = doc('').text()
        return {
            'title': title,
            'content': content,
            'date': date
        }
    except ConnectionError:
        return None
def save_to_mongo(data):
    if db['aritle'].update({'title': data['title']}, {'$set': data}, True):
        print('Save to mongo', data['title'])
    else:
        print('save to mongo failed', data['title'])


def main():
    for page in range(1,6):
        html = get_index('风景', page)
        print('第'+str(page)+'页最终的html返回值', str(html)[:100])
        if html:
            article_urls = parse_index(html)
            for article_url in article_urls:
                print(article_url)


if __name__ == '__main__':
    main()
