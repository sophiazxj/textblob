# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup as bs
import json
import pandas as pd

df = pd.DataFrame()
url = 'https://rate.tmall.com/listTryReport.htm?itemId=545135822523&pageSize=75&currentPage=1&_ksTS=1519889611274_700&callback=jsonp701'

content = requests.get(url).text
content.find('"tryReportList"')
content = eval(content[73:][17:][:-4])

json_str = json.dumps(content)
data = json.loads(json_str)
for d in data:
    df = df.append(pd.DataFrame(d))
df['url'] = url
df.to_excel('TryReport.xlsx',sheet_name='TryReport',index= False)
