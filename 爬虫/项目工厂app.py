import re, random, time, json, datetime, requests
from pyquery import PyQuery as pq
import urllib.parse
import multiprocessing
from multiprocessing import queues

def get_date(content):
    pattern = r'(20\d{2})年(\d{1,2})月(\d{1,2})日'
    m = bool(re.search(pattern, content))
    if m:
        result = list(re.findall(pattern, content)[0])
        # print(result)
        for a in range(1, 3):
            if len(result[a]) == 1:
                result[a] = '0' + result[a]

        result_str = '-'.join(result)
        # print(result_str)
        clien_date = result_str
        return result_str
    # 匹配2017-6-20
    pattern = r'(20\d{2})-(\d{1,2})-(\d{1,2})'
    m = bool(re.search(pattern, content))
    if m:
        result = list(re.findall(pattern, content)[0])
        # print(result)
        for a in range(1, 3):
            if len(result[a]) == 1:
                result[a] = '0' + result[a]

        result_str = '-'.join(result)
        # print(result_str)
        return result_str
    # 匹配2017.6.20
    pattern = r'(20\d{2})\.(\d{1,2})\.(\d{1,2})'
    m = bool(re.search(pattern, content))
    if m:
        result = list(re.findall(pattern, content)[0])
        # print(result)
        for a in range(1, 3):
            if len(result[a]) == 1:
                result[a] = '0' + result[a]

        result_str = '-'.join(result)
        # print(result_str)
        return result_str
    # 匹配2017/6/20
    pattern = r'(20\d{2})/(\d{1,2})/(\d{1,2})'
    m = bool(re.search(pattern, content))
    if m:
        result = list(re.findall(pattern, content)[0])
        # print(result)
        for a in range(1, 3):
            if len(result[a]) == 1:
                result[a] = '0' + result[a]

        result_str = '-'.join(result)
        # print(result_str)
        return result_str
    # 匹配6月20日
    pattern = r'(\d{1,2})月(\d{1,2})日'
    m = bool(re.search(pattern, content))
    if m:
        result = list(re.findall(pattern, content)[0])
        # print(result)
        for a in range(0, 2):
            if len(result[a]) == 1:
                result[a] = '0' + result[a]

        result_str = '2018-' + '-'.join(result)
        # print(result_str)
        return result_str
    pattern = r'(\d{1,2})-(\d{1,2})'
    m = bool(re.search(pattern, content))
    if m:
        result = list(re.findall(pattern, content)[0])
        # print(result)
        for a in range(0, 2):
            if len(result[a]) == 1:
                result[a] = '0' + result[a]

        result_str = '2018-' + '-'.join(result)
        # print(result_str)
        return result_str
    return u''

def get_date2(timestamp):
    timestamp = str(timestamp)
    timestamp = int(timestamp[:10])
    date = datetime.datetime.utcfromtimestamp(timestamp)
    return get_date(str(date))

def spider():
    task_uid = 255059
    clue_uid = 352373
    company_id = 219043
    clue_name = u'项目工厂'
    headers = {
        "access_token": "",
        "devicetype": "android",
        "Content-Type": "application/json; charset=utf-8",
        "Content-Length": "78",
        "Host": "pemarket.com.cn",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/3.3.1",

    }

    headers1 = {
        "Host": "www.pemarket.com.cn",
        "Connection": "keep-alive",
        "Content-Length": "33",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "Accept": "application/json, text/plain, */*",
        "Origin": "http://www.pemarket.com.cn",
        "User-Agent": "Mozilla/5.0 (Linux; Android 5.1; HUAWEI TIT-AL00 Build/HUAWEITIT-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36xiangmugongchang:Android",
        "Content-Type": "application/json",
        "Referer": "http://www.pemarket.com.cn/finance-new-detail?id=5c1b0aa90b3c3ef83c535a9f",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,en-US;q=0.8",
        "X-Requested-With": "com.pemv2",

    }
    for i in range(1, 710):
        time.sleep(2)
        print('第' + str(i) + "次")

        url = 'http://pemarket.com.cn/api/index/getTopNewsList#%d' % (i)
        payload = {"isfirst": "", "lasttime": "2018-12-20 10:34", "pageSize": "10", "currentPage": str(i)}

        ret1 = requests.post(url, data=json.dumps(payload), headers=headers)
        # print(ret1.json()['resultList'])
        res = ret1.json()['resultList']
        for i in res:
            # print(i['id'])
            d_url = 'http://www.pemarket.com.cn/wap/index/getTopNewsDetail#%s' % (i['id'])
            data1 = {"id": i['id']}
            ret2 = requests.post(d_url, data=json.dumps(data1), headers=headers1)
            text = ret2.json()['contents']

            reg = re.compile(r'<img alt=".+?" src=".+?"')
            res = reg.findall(text)
            # print(res)
            if res is not None:
                for i in res:
                    # print(i)
                    reg3 = re.compile(r'src=".+?"')
                    res = reg3.findall(i)
                    print(res[0][5:-1])
                    src = res[0][5:-1]
                    date = ret2.json()['date']
                    print(date)
                    data = {
                        "pid": str(time.time()).split('.')[0] + str(random.randint(10000, 99999)),
                        "task_id": task_uid,
                        "clue_id": clue_uid,
                        "clue_name": clue_name,
                        "company_id": company_id,
                        "url": 'http://www.pemarket.com.cn/wap/index/getTopNewsDetail',
                        "pic_url": src,
                        "client_date": date,
                        "url_article_title": "",
                        "url_article": "",
                        "is_cover": 0,
                    }
                    aa = {'resource': data}
                    d = json.dumps(aa)
                    url = 'http://shijue.qingapi.cn/task_python/start'
                    r = requests.post(url, data={"data": d})
                    # print r.text


if __name__ == '__main__':
    spider()

