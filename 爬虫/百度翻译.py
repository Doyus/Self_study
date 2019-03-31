import re, random, time, json, datetime, requests
from pyquery import PyQuery as pq
import urllib.parse
import multiprocessing
from multiprocessing import queues
import requests
import logging
logging.captureWarnings(True)


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


def spider(a):
    head = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "BAIDUID=733CCA8C2B8A53B097A4BF5ABD09677D:FG=1; PSTM=1535426415; BIDUPSID=4552A497251A78CBD632BEDD5AE5540F; BDUSS=VE5STJhcUFSajVGd3VtSjhwY09taHZCTnZad3lRdXZmU3JHa35JTnhKeUdneE5jQVFBQUFBJCQAAAAAAAAAAAEAAABYuWY9aG91c2W0873hvtYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIb261uG9utbc; MCITY=-131%3A; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1545731436",
        "Host": "fanyi-app.baidu.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
    }
    task_uid = 255954
    clue_uid = 360830
    company_id = 228116
    clue_name = u'百度翻译'
    res = requests.get(a, headers=head, verify=False)
    # print(res.json())
    req = res.json()['data']
    riqi = res.json()["next_date"]
    print(riqi)
    for i in req:
        if i.get('url') and 'passage' in i.get('url'):
            urla = i['url']
            #print(url)
            time.sleep(3)
            res2 = requests.get(urla)
            text = res2.text
            reg_date = re.compile(r'em><em class="rich_media_meta rich_media_meta_text">.+?<')

            data1 = reg_date.findall(text)
            if len(data1) == 0:
                data1 = ''
            else:
                data1 = reg_date.findall(text)[0]
            #print(data1[52:-1])
            date1 = data1[52:-1]
            reg = re.compile(r'src="./image/.+?"')
            res3 = reg.findall(text)
            reg_title = re.compile(r'<title>.+?/title>')
            title1 = reg_title.findall(text)
            for j in res3:
                a = urla.replace('index.html','')
                #print(a + j[7:-1])
                src1 = a + j[7:-1]
                print(src1)
                data = {
                    "pid": str(time.time()).split('.')[0] + str(random.randint(10000, 99999)),
                    "task_id": 255954,
                    "clue_id": 360830,
                    "clue_name": '百度翻译',
                    "company_id": 228116,
                    "url": urla,
                    "pic_url": src1,
                    "client_date": date1,
                    "url_article_title": title1,
                    "url_article": '',
                    "is_cover": 0,
                }
                aa = {'resource': data}
                d = json.dumps(aa)
                url = 'http://shijue.qingapi.cn/task_python/start'
                try:
                    r = requests.post(url, data={"data": d})
                except:
                    print('####################')
                    print(riqi)
                    print('*********************')
                    pass
                else:
                    print(r.text)
                    print(data)


    next_url = 'https://fanyi-app.baidu.com/transapp/flowdata?&syslan=zh&sign=5ae14fd969208f54bdb8640f37f15324&reqdate={qqq}&timestamp=1545803444240&reqcount=0&os_lang=zh&dvw=720&dvh=1184&plat=android&sysmodel=HUAWEI_HUAWEI TIT-AL00&mnc=-1&systemVersion=5.1&appVersion=7.11.1&cuid=7AA7F85A7D6AE319D2DB43EF47543B7E|64CDE2E500000A&imei=A000005E2EDC46&version=92&netterm=WIFI&cdate=2018-12-26 13:50:44&mcc=-1&channel=baiduas&vendor=HUAWEI&product=transapp'.format(
        qqq=str(riqi))

    spider(next_url)



if __name__ == '__main__':
    spider('https://fanyi-app.baidu.com/transapp/flowdata?&syslan=zh&sign=5ae14fd969208f54bdb8640f37f15324&reqdate=2016-01-30 00:00:00&timestamp=1545803444240&reqcount=0&os_lang=zh&dvw=720&dvh=1184&plat=android&sysmodel=HUAWEI_HUAWEI%20TIT-AL00&mnc=-1&systemVersion=5.1&appVersion=7.11.1&cuid=7AA7F85A7D6AE319D2DB43EF47543B7E|64CDE2E500000A&imei=A000005E2EDC46&version=92&netterm=WIFI&cdate=2018-12-26%2013:50:44&mcc=-1&channel=baiduas&vendor=HUAWEI&product=transapp')

