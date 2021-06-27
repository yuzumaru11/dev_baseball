#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 選手CSVファイルをDBに登録


# In[2]:


from bs4 import BeautifulSoup
import urllib.request as req
import pandas as pd
import random
import time
import glob
import sqlite3


# In[3]:


# 選手が登録されているか確認し登録がない場合、登録
def insert_table(url, team, name):
    dbname = 'Baseball.db'
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    try:
        sql = "SELECT COUNT(*) FROM player WHERE url = '" + url + "' AND team = '" + team + "'"
        cur.execute(sql)
        result = cur.fetchone()

        if(result[0] < 1):
            sql = "INSERT INTO player(url, team, name) values('" + url + "', '" + team + "', '" + name + "')"
            print(sql)
            cur.execute(sql)
            conn.commit()
    except:
        cur.close()
        conn.close()
        exit()
    cur.close()
    conn.close()


# In[4]:


files = glob.glob('./data/*.csv')


# In[5]:


for file in files:
    file_name = file.replace('./data\\', '')
    team_name = ''
    if('dragons' in file_name): team_name = 'dragons'
    if('tigers' in file_name): team_name = 'tigers'
    if('carp' in file_name): team_name = 'carp'
    if('dena' in file_name): team_name = 'dena'
    if('giants' in file_name): team_name = 'giants'
    if('swallows' in file_name): team_name = 'swallows'

    try:    
        df = pd.read_csv('./data/' + file_name, header=None, names=['url', 'player'])
        for data in df.itertuples():        
            url = data[1].replace('.html', '')
            name = data[2]
            insert_table(url, team_name, name)
          
    except pd.errors.EmptyDataError:
      continue                 

