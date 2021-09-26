#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request as req
import urllib.request as req_error
import time
import pandas as pd
import random
import sqlite3
import pymysql
import datetime


# In[2]:


conn = pymysql.connect(host='localhost',
                         user='root',
                         password='yuzumaru11',
                         db='bbdata',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
cursor = conn.cursor()


# In[3]:


year1 = datetime.date.today().year


# In[4]:


# bstatsテーブルに追加
def insert_stats(url, tds):
 
    cursor = conn.cursor()
    
    sql = "SELECT COUNT(*) count FROM t_stats WHERE url = '" + format(url, '0>8') + "' AND year1 = '" + tds[0] + "'"
    cursor.execute(sql)
    result = cursor.fetchone()

    if(result['count'] < 1):
        sql = "SELECT * FROM m_player WHERE url = '" + format(url, '0>8') + "'"
        cursor.execute(sql)
        mPlayer = cursor.fetchone()
        
        player_id = mPlayer['player_id'] 
        
        sql = "INSERT INTO t_stats(               player_id               , url               , year1               , team               , games               , at_bat1               , at_bat2               , score               , hit               , double1               , triple               , homerun               , basehit               , rbi               , steal               , steal_dead               , sacrifice               , sacrifice_fly               , walks               , hit_by_pitch               , strikeout               , double_out               , hit_rate               , slugging               , on_base ) values(            '" + player_id + "'         ,  '" + format(url, '0>8') + "'         , '" + tds[0] + "'         , '" + tds[1] + "'         , '" + tds[2] + "'         , '" + tds[3] + "'         , '" + tds[4] + "'         , '" + tds[5] + "'         , '" + tds[6] + "'         , '" + tds[7] + "'         , '" + tds[8] + "'         , '" + tds[9] + "'         , '" + tds[10] + "'         , '" + tds[11] + "'         , '" + tds[12] + "'         , '" + tds[13] + "'         , '" + tds[14] + "'         , '" + tds[15] + "'         , '" + tds[16] + "'         , '" + tds[17] + "'         , '" + tds[18] + "'         , '" + tds[19] + "'         , '" + tds[20] + "'         , '" + tds[21] + "'         , '" + tds[22] + "' )"
        cursor.execute(sql)
        conn.commit()
    else:
#       最新年の場合のみ更新
        if str(tds[0]) == str(year1):
            sql = "update t_stats set team = '" + tds[1] + "', games = '" + tds[2] + "', at_bat1 = '" + tds[3] + "', at_bat2 = '" + tds[4] + "', score = '" + tds[5] + "'             , hit = '" + tds[6] + "', double1 = '" + tds[7] + "', triple = '" + tds[8] + "', homerun = '" + tds[9] + "' , basehit = '" + tds[10] + "'             , rbi = '" + tds[11] + "', steal = '" + tds[12] + "' , steal_dead = '" + tds[13] + "' , sacrifice = '" + tds[14] + "', sacrifice_fly = '" + tds[15] + "'             , walks = '" + tds[16] + "', hit_by_pitch = '" + tds[17] + "' , strikeout = '" + tds[18] + "' , double_out = '" + tds[19] + "' , hit_rate = '" + tds[20] + "'             , slugging = '" + tds[21] + "' , on_base = '" + tds[22] + "' where year1 = '" + str(year1) + "' and url = '" + str(url) + "'"
            cursor.execute(sql)
            conn.commit()


# In[5]:


# playerテーブルを読込
def read_player():

    sql = "SELECT * FROM m_active_player where year = '" + str(year1) + "'"
    df = pd.read_sql(sql, conn)

    return df


# In[6]:


def active_bstats_update(df):

    for data in df.itertuples():
        
        try:
            url = str(data[5])
            #ランダム時間でURLを生成する
            time.sleep(random.randrange(2, 5))
            player_url = "https://npb.jp/bis/players/" + format(url, '0>8') + '.html'
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
                    insert_stats(url, tds)
                    
        except req_error.HTTPError as e:
            print(e.reason)
        except IndexError as e:
            print(e)
        except Exception as e:
            print(e)


# In[7]:


try:
  
    df = read_player()
    active_bstats_update(df)    
    
except req_error.HTTPError as e:
    print(e.reason)
except IndexError as e:
    print(e)
except Exception as e:
    print(e)
finally:
    if cursor is not None:
        cursor.close()
    if conn is not None:
        conn.close()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




