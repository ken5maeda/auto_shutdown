import datetime
import requests
import os
import sys


today = datetime.date.today()

# 土日は停止しない
if today.weekday() == 5 or today.weekday() == 6:
    sys.exit()

# お盆は停止しない
if datetime.date(today.year, 8, 13) <= today and today <= datetime.date(today.year, 8, 16):
    sys.exit()

# 年末年始は停止しない
if datetime.date(today.year, 12, 28) <= today or today <= datetime.date(today.year, 1, 5):
    sys.exit()

# 内閣府のホームページから祝日を取得
url = 'https://www8.cao.go.jp/chosei/shukujitsu/syukujitsu.csv'
res = requests.get(url)
holidays = res.text.splitlines()

# 祝日は停止しない
for holiday in holidays:
    if f"{today:%Y}/{today.month}/{today.day}" == holiday.split(",")[0]:
        sys.exit()

os.system('shutdown -s')
