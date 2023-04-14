# -*- coding:utf-8 -*-

import slackweb
import datetime
import os

url = 'xxx'
slack = slackweb.Slack(url=url)

path = 'xxx'
d_today = str(datetime.date.today())
fileList = [
    d_today + 'xxx',
    d_today + 'xxx',
    d_today + 'xxx'
]

flg = True
for file in fileList:
    if not os.path.exists(path + file):
        flg = False

if flg:
    message = '正常に実行されました'
else:
    message = '実行時にエラーが発生しました'

slack.notify(text=message)
