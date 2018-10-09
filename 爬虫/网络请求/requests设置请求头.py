# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-10-05 16:42:59
# @Last Modified by:   Marte
# @Last Modified time: 2018-10-05 16:44:06
# requests发送前修改请求信息
# requests可以再发送请求前，修改请求信息，见Prepared Requests

# 例如发送前手动修改请求头Content-Length


from requests import Request, Session

s = Session()
req = Request('POST', url, data=data, headers=headers)
prepped = req.prepare()

# do something with prepped.headers
prepped.headers['Content-Length'] = your_custom_content_length_calculation()
# prepped.headers['Content-Length'] = '1000000000'

resp = s.send(prepped)
# 如果session有自己的配置，如cookie等，应该使用s.prepare_request(req), 而不是req.prepare()