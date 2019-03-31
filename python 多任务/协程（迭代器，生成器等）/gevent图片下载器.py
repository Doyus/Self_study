# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-10-01 14:39:12
# @Last Modified by:   Marte
# @Last Modified time: 2018-10-01 14:54:52
import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()

def downloader(img_name, img_url):
    req = urllib.request.urlopen(img_url)

    img_content = req.read()

    with open(img_name, "wb") as f:
        f.write(img_content)

def main():
    gevent.joinall([
        gevent.spawn(downloader, '3.jpg','url')
        gevent.spawn(downloader, '4.jpg','url')


        ])
