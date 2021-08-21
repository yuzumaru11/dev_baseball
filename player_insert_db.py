#!/usr/bin/env python
# coding: utf-8

# In[134]:


# 選手CSVファイルをDBに登録


# In[135]:


from bs4 import BeautifulSoup
import urllib.request as req
import pandas as pd
import random
import time
import glob
import pymysql
import sys


# In[136]:


def connDb():
    conn = pymysql.connect(host='localhost',
                         user='root',
                         password='yuzumaru11',
                         db='bbdata',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    return conn


# In[137]:


# 選手が登録されているか確認し登録がない場合、登録
def insert_table(url, team, name):
    conn = connDb()
    cur = conn.cursor()
    try:
        sql = "select count(*) count from m_player_work WHERE url = '" + format(url, '0>8') + "'"
        cur.execute(sql)
        result = cur.fetchone()

        if(result['count'] < 1):            
            # idを取得
            sql = "select max(id) id from m_player_work"
            cur.execute(sql)
            result = cur.fetchone()
            if result['id'] is None:
                player_id = 1
            else:
                player_id = int(result['id']) + 1
            
            sql = "insert into m_player_work(player_id, url, teams, player_name, flg) values('" + str(player_id) + "', '" + format(url, '0>8') + "', '" + team + "', '" + name + "', '" + str(0) + "')"
            cur.execute(sql)
            conn.commit()
        else:
            sql = "update m_player_work set teams= '" + team + "', player_name = '" + name + "' WHERE url = '" + format(url, '0>8') + "'"

    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()


# In[138]:


files = glob.glob('./data/*.csv')


# In[139]:


for file in files:
    file_name = file.replace('./data\\', '')
    team_name = ''
    if('dragons' in file_name): team_name = 'dragons'
    if('tigers' in file_name): team_name = 'tigers'
    if('carp' in file_name): team_name = 'carp'
    if('baystars' in file_name): team_name = 'baystars'
    if('giants' in file_name): team_name = 'giants'
    if('swallows' in file_name): team_name = 'swallows'

    if('marines' in file_name): team_name = 'marines'
    if('fighters' in file_name): team_name = 'fighters'
    if('hawks' in file_name): team_name = 'fighters'
    if('buffaloes' in file_name): team_name = 'hawks'
    if('eagles' in file_name): team_name = 'hawks'
    if('lions' in file_name): team_name = 'buffaloes'

    try:    
        df = pd.read_csv('./data/' + file_name, header=None, names=['url', 'player'])
        for data in df.itertuples():
            url = data[1].replace('.html', '')
            name = data[2]
            insert_table(url, team_name, name)
          
    except pd.errors.EmptyDataError:
      continue                 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




