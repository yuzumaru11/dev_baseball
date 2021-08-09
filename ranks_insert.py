#!/usr/bin/env python
# coding: utf-8

# In[205]:


from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request as req
import urllib.request as req_error
import datetime
import pandas as pd
import random
import sqlite3
import pymysql


# In[206]:


def delete_ranks(table_name):
    conn = pymysql.connect(host='localhost',
                             user='root',
                             password='yuzumaru11',
                             db='bbdata',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    
    try:
        cursor = conn.cursor()
        sql = "delete from " + table_name + " where day1 = '" + now + "';"
        
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()
    


# In[207]:


def insert_ranks(tds, table_name):
    
    conn = pymysql.connect(host='localhost',
                             user='root',
                             password='yuzumaru11',
                             db='bbdata',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    now1 = str(datetime.datetime.now())
    baseball = 'baseball' 
    
    try:
        cursor = conn.cursor()

        sql = "INSERT INTO " + table_name + " (day1 ,ranks1 ,team, games, win, lose, draw ,winrate ,diff ,remine_games ,score ,runs_allowed ,homerun ,steal ,hit, pitch, udate, uuser, rdate, ruser)             values(              '" + now + "'             , '" + tds[0] + "'             , '" + tds[1] + "'             , '" + tds[2] + "'             , '" + tds[3] + "'             , '" + tds[4] + "'             , '" + tds[5] + "'             , '" + tds[6] + "'             , '" + tds[7] + "'             , '" + tds[8] + "'             , '" + tds[9] + "'             , '" + tds[10] + "'             , '" + tds[11] + "'             , '" + tds[12] + "'             , '" + tds[13] + "'             , '" + tds[14] + "'             , '" + now1 + "'             , '" + baseball + "'             , '" + now1 + "'             , '" + baseball + "' )"

        print(sql)
        cursor.execute(sql)
        conn.commit()
      
    except Exception as e:
        print(e)
    finally:
        conn.close()


# In[ ]:





# In[208]:


url = "https://baseball.yahoo.co.jp/npb/standings/"
response = req.urlopen(url)
parse_html = BeautifulSoup(response, 'html.parser')

#セ・リーグ用処理
rankTable = parse_html.findAll("table", {"class":"bb-rankTable"})[0]
rows = rankTable.findAll("tr")
table_name ='t_cranks'
delete_ranks(table_name)
for i in range(len(rows)):
    tds_tmp = rows[i].find_all('td')
    tds = [ tds.text.replace('\n', '').replace('\r', ' ').replace('\u3000', ' ').replace(' ','') for tds in tds_tmp ]
    
    if len(tds) > 0:
        insert_ranks(tds, table_name)

        
#パ・リーグ用処理
rankTable = parse_html.findAll("table", {"class":"bb-rankTable"})[1]
rows = rankTable.findAll("tr")
table_name ='t_pranks'
delete_ranks(table_name)
for i in range(len(rows)):
    tds_tmp = rows[i].find_all('td')
    tds = [ tds.text.replace('\n', '').replace('\r', ' ').replace('\u3000', ' ').replace(' ','') for tds in tds_tmp ]
    
    if len(tds) > 0:
        insert_ranks(tds, table_name)
       


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




