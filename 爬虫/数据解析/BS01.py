from bs4 import BeautifulSoup
"""
笔记：
* find_all的使用
1. 在提取标签时，第一个参数是标签的名字，然后如果在提取标签时想要用标签属性进行过滤，那么可以在这个方法中通过关键字参数的形式，将属性的名字对应的值放在一个字典中传给’attrs‘属性
2. 有些时候，在提取标签时，不想提取那么多，那么可以使用limit参数来限制

** find与find_all的区别：
1. find: 找到第一个满足条件就返回，说白了，就是只会返回一个元素
2. find_all:将所有的满足条件的标签返回，说白了，会返回很多标签，以列表形式

** 使用find和find_all过滤条件：
1. 关键字参数：将属性条件放到一个字典中去，传给attrs参数
2. attrs参数：将属性条件放在一个字典中去，传给attrs参数

** 获取标签的属性：
1. 通过下表获取：
    href = a.attrs['href']
2. 通过attrs属性来获取：


** string,stripped_strings,string属性以及get_text方法
1. string: 获取某个标签下的非标签字符串
2. strings: 获取某个标签下的子孙非标签字符产
3. stripped_strings:
    获取某个标签下的子孙非标签字符串，会去掉空白字符。
4. get_text:
    获取某个标签下的子孙非标签字符串，不是以列表形式返回

"""
html = '''
<table class="tablelist" cellpadding="0" cellspacing="0">
                <tr class="h">
                    <td class="l" width="374">职位名称</td>
                    <td>职位类别</td>
                    <td>人数</td>
                    <td>地点</td>
                    <td>发布时间</td>
                </tr>
                                <tr class="even">
                    <td class="l square"><a target="_blank" href="position_detail.php?id=44592&keywords=&tid=87&lid=2156">PCG05-数据平台运维（北京）</a></td>
                    <td>技术类</td>
                    <td>1</td>
                    <td>北京</td>
                    <td>2018-10-05</td>
                </tr>
                                <tr class="odd">
                    <td class="l square"><a target="_blank" href="position_detail.php?id=44578&keywords=&tid=87&lid=2156">CSIG16-基础架构工程师（北京）</a><span class="hot">&nbsp;</span></td>
                    <td>技术类</td>
                    <td>2</td>
                    <td>北京</td>
                    <td>2018-10-05</td>
                </tr>
                                <tr class="even">
                    <td class="l square"><a target="_blank" href="position_detail.php?id=44568&keywords=&tid=87&lid=2156">CSIG16-地图数据Web前端研发工程师</a></td>
                    <td>技术类</td>
                    <td>1</td>
                    <td>北京</td>
                    <td>2018-10-05</td>
                </tr>
                                <tr class="odd">
                    <td class="l square"><a target="_blank" href="position_detail.php?id=44547&keywords=&tid=87&lid=2156">PCG10-NLP算法工程师</a></td>
                    <td>技术类</td>
                    <td>1</td>
                    <td>北京</td>
                    <td>2018-10-05</td>
                </tr>
                                <tr class="even">
                    <td class="l square"><a target="_blank" href="position_detail.php?id=44503&keywords=&tid=87&lid=2156">CSIG16-腾讯地图高级研发工程师</a></td>
                    <td>技术类</td>
                    <td>1</td>
                    <td>北京</td>
                    <td>2018-10-05</td>
                </tr>
                                <tr class="odd">
                    <td class="l square"><a target="_blank" href="position_detail.php?id=44493&keywords=&tid=87&lid=2156">PCG05-腾讯汽车测试工程师（北京）</a><span class="hot">&nbsp;</span></td>
                    <td>技术类</td>
                    <td>1</td>
                    <td>北京</td>
                    <td>2018-10-05</td>
                </tr>
                                <tr class="even">
                    <td class="l square"><a target="_blank" href="position_detail.php?id=44480&keywords=&tid=87&lid=2156">CSIG16-车联网web前端开发（北京）</a></td>
                    <td>技术类</td>
                    <td>1</td>
                    <td>北京</td>
                    <td>2018-10-05</td>
                </tr>
                                <tr class="odd">
                    <td class="l square"><a target="_blank" href="position_detail.php?id=44460&keywords=&tid=87&lid=2156">CSIG16-地图数据Web前端研发工程师</a></td>
                    <td>技术类</td>
                    <td>1</td>
                    <td>北京</td>
                    <td>2018-10-05</td>
                </tr>
                                <tr class="even">
                    <td class="l square"><a target="_blank" href="position_detail.php?id=44465&keywords=&tid=87&lid=2156">CSIG16-自动驾驶系统工程师</a></td>
                    <td>技术类</td>
                    <td>1</td>
                    <td>北京</td>
                    <td>2018-10-05</td>
                </tr>
                                <tr class="odd">
                    <td class="l square"><a target="_blank" href="position_detail.php?id=44456&keywords=&tid=87&lid=2156">CSIG16-车联网售前方案经理</a></td>
                    <td>技术类</td>
                    <td>1</td>
                    <td>北京</td>
                    <td>2018-10-05</td>
                </tr>
                                <tr class="f">
                    <td colspan="5">
                        <div class="left">共<span class="lightblue total">215</span>个职位</div>
                        <div class="right"><div class="pagenav"><a href="javascript:;" class="noactive" id="prev">上一页</a><a class="active" href="javascript:;">1</a><a href="position.php?lid=2156&tid=87&keywords=请输入关键词&start=10#a">2</a><a href="position.php?lid=2156&tid=87&keywords=请输入关键词&start=20#a">3</a><a href="position.php?lid=2156&tid=87&keywords=请输入关键词&start=30#a">4</a><a href="position.php?lid=2156&tid=87&keywords=请输入关键词&start=40#a">5</a><a href="position.php?lid=2156&tid=87&keywords=请输入关键词&start=50#a">6</a><a href="position.php?lid=2156&tid=87&keywords=请输入关键词&start=60#a">7</a><a href="position.php?lid=2156&tid=87&keywords=请输入关键词&start=70#a">...</a><a href="position.php?lid=2156&tid=87&keywords=请输入关键词&start=210#a">22</a><a href="position.php?lid=2156&tid=87&keywords=请输入关键词&start=10#a" id="next">下一页</a><div class="clr"></div></div></div>
                        <div class="clr"></div>
                    </td>
                </tr>
            </table>
'''
#1. 获取所有tr标签
#2. 获取第二个tr标签
#3. 获取所有class等于event的tr标签
#4. 将所有id等于test，class也等于test的a标签提取出来
#5. 获取所有a标签的href属性
#6. 获取所有的职位信息(纯文本)
#
soup = BeautifulSoup(html,'lxml')

# 1. 获取所有tr标签
trs = soup.find_all('tr')
for tr in trs:
    print(tr)
    print('='*30)

# 2. 获取第二个tr标签
tr = soup.find_all('tr',limit=2)[1] #最多获取几个元素limit
print(tr)

#3. 获取所有class等于event的tr标签
#trs = soup.find_all('tr',attrs_='even')
trs = soup.find_all('tr',class_='even')
for i in trs:
    print(tr)
    print('='*30)

#4. 将所有id等于test，class也等于test的a标签提取出来
alist = soup.find_all('a', id='test', class_='test')
for i in alist:
    print(a)

#5. 获取所有a标签的href属性
alist = soup.find_all('a')
for href in hrefs:
    #获取属性1.下表，2.attrib
    href = a['href']
    print(href)
    href = a.attrs['href']
    print(href)

#6. 获取所有的职位信息（纯文本）

trs = soup.find_all('tr')[1:]
movies = []
for tr in trs:
    # movie = {}
    # tds = tr.find_all('td')
    # title = tds[0].string
    # category = tds[1].string
    # nums = tds[2].string
    # city = tds[3].string
    # pubtime = tds[4].string
    # movie['title'] = title
    # movie['title'] = title
    # movie['title'] = title
    # movie['title'] = title
    # movies.append(movie)
'''另一种更好的方式'''
infos = list(tr.strings)#可以直接获取非标签的内容，但是有一个缺点是，会把/n啥的也给你打印出来，因为也是非标签，然后引申出
infos = list(tr.stripped_strings)
# 可以获取非空白的内容














