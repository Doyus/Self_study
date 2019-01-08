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
    task_uid = 247155
    clue_uid = 405907
    company_id = 220140
    clue_name = u'咪咕阅读-热门小说电子书阅读器'
    header = {"Host": "wap.cmread.com",
              "Connection": "keep-alive",
              "Content-Length": "458",
              "Pragma": "no-cache",
              "Cache-Control": "no-cache",
              "Accept": "*/*",
              "Origin": "http://wap.cmread.com",
              "X-Requested-With": "XMLHttpRequest",
              "User-Agent": "CMREADBC_Android_720*1184_V7.98(720*1184;HUAWEI;HUAWEI TIT-AL00;Android 5.1;cn;JSBridge=1.0); AndroidAmberV2.5.0",
              "Content-Type": "application/x-www-form-urlencoded",
              "Referer": "http://wap.cmread.com/nap/p/cbfl_dzxx.jsp?z=1&ln=2444_2457_3801_1_380_L2&cm=M80100GH&vt=3",
              "Accept-Encoding": "gzip, deflate",
              "Accept-Language": "zh-CN,en-US;q=0.8",
              "Cookie": "JSESSIONID=874CC77B8EA31731964C9CEAE4849805; WT_FPC=id=23958ddac63b41c355c1545620110354:lv=1545622888900:ss=1545620110354; _clientid=666b010c8a683500240cf563dd8d5118"
              }

    for i in range(1, 4):
        time.sleep(2)
        print('第' + str(i) + "次")

        url = 'http://wap.cmread.com/nap/f/ms.navigation.navigationService/searchBookActionUrl.json?z=1&ln=4439_4573_3801_1_380_L1&bookClassId=2_1223_%E5%85%9A%E6%94%BF%E5%AD%A6%E4%B9%A0&pageNo={i}&pageSize=10&cm=M80100GH&vt=3'.format(
            i=i)
        data = {
            "isMarginBottom": 0,
            "bookClassId": "2_1223_党政学习",
            "ln": "4439_4573_3801_1_380",
            "componentId": 100208,
            "isPaddingTop": 0,
            "pluginCode": "select_booklist",
            "pageSize": 10,
            "cm": "M80100GH",
            "isMarginTop": 0,
            "pageId": 4439,
            "freeSystemAbilityKey": "android=and_freeSystem;ios=ios_freeSystem",
            "instanceId": 4573,
            "isShowRank": 0,
            "isShowLine": 0,
            "z": 1,
            "componentName": "select_booklist",
            "isNewSearch": 1,
            "vt": 3,
            "bookStats": 0,
            "wordCount": 0,
            "userLevel": 0,
            "chargeMode": 0,
            "searchSequenceRule": 15,
            "searchBookSort": "",

        }

        r = requests.post(url, data=json.dumps(data), headers=header)
        res = r.json()['data']['bookInfoList']
        for i in res:

            src = "http:" + i['bookCoverLogo']
            t = i['bookUpdateTime']

            data = {
                "pid": str(time.time()).split('.')[0] + str(random.randint(10000, 99999)),
                "task_id": task_uid,
                "clue_id": clue_uid,
                "clue_name": clue_name,
                "company_id": company_id,
                "url": url,
                "pic_url": src,
                "client_date": t,
                "url_article_title": "",
                "url_article": "",
                "is_cover": 0,
            }
            aa = {'resource': data}
            d = json.dumps(aa)
            url = 'http://shijue.qingapi.cn/task_python/start'
            # r = requests.post(url, data={"data": d})
            # print r.text
            print(data)


if __name__ == '__main__':
    spider()

