#!/usr/bin/env python
# coding: utf-8

# In[43]:


from bs4 import BeautifulSoup
import urllib.request as req
from selenium import webdriver
import time
import pandas as pd
import random
import sqlite3


# In[44]:


# 選手が登録されているか確認し登録がない場合、登録
def read_player():
    dbname = 'Baseball.db'
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    try:
        sql = "SELECT * FROM player"

        df = pd.read_sql(sql, conn)
    except:
        cur.close()
        conn.close()
        exit()
    cur.close()
    conn.close()
    return df


# In[45]:


df = read_player()


# In[46]:


for data in df.itertuples():
    url = str(data[2]) + '.html'
    
    #ランダム時間でURLを生成する
    time.sleep(random.randrange(1, 30))
    player_url = "https://npb.jp/bis/players/" + url
    print(player_url)
    response = req.urlopen(player_url)
    parse_html = BeautifulSoup(response, 'html.parser')
    
    # テーブルを指定
    pc_stats_wrapper = parse_html.findAll("div", {"id":"pc_stats_wrapper"})[0]

    table = pc_stats_wrapper.findAll("table", {"id":"tablefix_b"})[0]
    rows = table.findAll("tr")
    columns = [v.text.replace('\n', '').replace('\r', '') for v in rows[0].find_all('th')]
    df = pd.DataFrame(columns=columns)
    
    # 全行のうちのある行成分について
    for i in range(len(rows)):
        tds_tmp = rows[i].find_all('td')
        tds = [ tds.text.replace('\n', '').replace('\r', ' ').replace('\u3000', ' ').replace(' ','') for tds in tds_tmp ]
        
        if len(tds) == len(columns):
            # テーブルに登録
            

#             values = [ tds ]
#             df = df.append(pd.Series(values[0], index=columns), ignore_index= True)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




