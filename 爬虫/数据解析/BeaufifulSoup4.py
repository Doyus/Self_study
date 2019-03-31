# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-10-05 15:36:18
# @Last Modified by:   Marte
# @Last Modified time: 2018-10-05 16:55:43
from bs4 import BeautifulSoup
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
bs = BeautifulSoup(html,'lxml')#lxml是指定解释器意思，bs底层需要一个解析引擎，依赖于第三解释器
print(bs.prettify())