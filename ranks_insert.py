#!/usr/bin/env python
# coding: utf-8

# In[36]:


from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request as req
import urllib.request as req_error
import datetime
import pandas as pd
import random
import sqlite3
import pymysql


# In[37]:


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
    


# In[38]:


def get_team_id(team):
    
    team_id = ''
    
    if(team in '阪神') or (team in 'タイガース'):
        team_id = 'tigers'
        
    elif (team in '巨人') or (team in 'ジャイアンツ'):
        team_id = 'giants'
    
    elif(team in 'ヤクルト') or (team in 'スワローズ'):
        team_id = 'swallows'
    
    elif(team in '中日') or (team in 'ドラゴンズ'):
        team_id = 'dragons'
    
    elif(team in '広島') or (team in 'カープ'):
        team_id = 'carp'    
    
    elif(team in 'DeNA') or (team in 'ベイスターズ'):
        team_id = 'baystars'
    
    elif(team in 'オリックス') or (team in 'バファローズ'):
        team_id = 'buffaloes'    
    
    elif(team in '楽天') or (team in 'イーグルス'):
        team_id = 'eagles'
    
    elif(team in 'ロッテ') or (team in 'マリーンズ'):
        team_id = 'marines'

    elif(team in 'ソフトバンク') or (team in 'ホークス'):
        team_id = 'hawks'
    
    elif(team in '西武') or (team in 'ライオンズ'):
        team_id = 'lions'

    elif(team in '日本ハム') or (team in 'ファイターズ'):
        team_id = 'fighters'
    
    else:
        team_id = ''
    
    return team_id
    


# In[39]:


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
    team_id = get_team_id(tds[1])
        
    try:
        cursor = conn.cursor()

        sql = "INSERT INTO " + table_name + " (day1 ,ranks1 ,team, games, win, lose, draw ,winrate ,diff ,remine_games ,score ,runs_allowed ,homerun ,steal ,hit, pitch, udate, uuser, rdate, ruser)             values(              '" + now + "'             , '" + tds[0] + "'             , '" + team_id + "'             , '" + tds[2] + "'             , '" + tds[3] + "'             , '" + tds[4] + "'             , '" + tds[5] + "'             , '" + tds[6] + "'             , '" + tds[7] + "'             , '" + tds[8] + "'             , '" + tds[9] + "'             , '" + tds[10] + "'             , '" + tds[11] + "'             , '" + tds[12] + "'             , '" + tds[13] + "'             , '" + tds[14] + "'             , '" + now1 + "'             , '" + baseball + "'             , '" + now1 + "'             , '" + baseball + "' )"

        cursor.execute(sql)
        conn.commit()
      
    except Exception as e:
        print(e)
    finally:
        conn.close()


# In[40]:


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





# In[ ]:




