#!/usr/bin/env python
# coding: utf-8

# In[44]:


from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request as req
import urllib.request as req_error
import time
import pandas as pd
import random
import pymysql
import datetime


# In[45]:


conn = pymysql.connect(host='localhost',
                         user='root',
                         password='yuzumaru11',
                         db='bbdata',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
cursor = conn.cursor()


# In[46]:


year1 = datetime.date.today().year


# In[47]:


# bstatsテーブルに追加
def insert_pstats(url, tds):
 
    cursor = conn.cursor()
    
    sql = "SELECT COUNT(*) count FROM t_pstats WHERE url = '" + format(url, '0>8') + "' AND year1 = '" + tds[0] + "'"
    cursor.execute(sql)
    result = cursor.fetchone()

    if(result['count'] < 1):
        sql = "SELECT * FROM m_player WHERE url = '" + format(url, '0>8') + "'"
        cursor.execute(sql)
        mPlayer = cursor.fetchone()
        
        player_id = mPlayer['player_id'] 
        
        sql = "INSERT INTO t_pstats(               player_id               , team               , year1               , url               , games               , victory               , lose               , save1               , hold1               , holdp               , complete_pitch               , complete_game               , no_four_pitch               , victory_rate               , batter               , pitch_innings               , hit1               , homerun               , four_ball               , dead_ball               , strikeout               , wild_pitch               , balk               , runs_allowed               , earned_run               , era               ) values(            '" + player_id + "'          , '" + tds[1] + "'          , '" + tds[0] + "'         ,  '" + format(url, '0>8') + "'         , '" + tds[2] + "'         , '" + tds[3] + "'         , '" + tds[4] + "'         , '" + tds[5] + "'         , '" + tds[6] + "'         , '" + tds[7] + "'         , '" + tds[8] + "'         , '" + tds[9] + "'         , '" + tds[10] + "'         , '" + tds[11] + "'         , '" + tds[12] + "'         , '" + tds[13] + "'         , '" + tds[15] + "'         , '" + tds[16] + "'         , '" + tds[17] + "'         , '" + tds[18] + "'         , '" + tds[19] + "'         , '" + tds[20] + "'         , '" + tds[21] + "'         , '" + tds[22] + "'         , '" + tds[23] + "'         , '" + tds[24] + "' )"
        cursor.execute(sql)
        conn.commit()
    else:
#       最新年の場合のみ更新
        if str(tds[0]) == str(year1):
            sql = "update t_pstats set             team = '" + tds[1] + "'             , games = '" + tds[2] + "'             , victory = '" + tds[3] + "'             , lose = '" + tds[4] + "'             , save1 = '" + tds[5] + "'             , hold1 = '" + tds[6] + "'             , holdp = '" + tds[7] + "'             , complete_pitch = '" + tds[8] + "'             , complete_game = '" + tds[9] + "'              , no_four_pitch = '" + tds[10] + "'             , victory_rate = '" + tds[11] + "'            , batter = '" + tds[12] + "'             , pitch_innings = '" + tds[13] + "'             , hit1 = '" + tds[15] + "'            , homerun = '" + tds[16] + "'             , four_ball = '" + tds[17] + "'            , dead_ball = '" + tds[18] + "'             , strikeout = '" + tds[19] + "'             , wild_pitch = '" + tds[20] + "'             , balk = '" + tds[21] + "'             , runs_allowed = '" + tds[22] + "'             , earned_run = '" + tds[23] + "'             , era = '" + tds[24] + "'               where year1 = '" + str(year1) + "' and url = '" + str(url) + "'"
            cursor.execute(sql)
            conn.commit()


# In[48]:


# playerテーブルを読込
def read_player():

    sql = "SELECT * FROM m_active_player where year = '" + str(year1) + "'"
    df = pd.read_sql(sql, conn)

    return df


# In[49]:


def active_pstats_update(df):

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

            table = pc_stats_wrapper.findAll("table", {"id":"tablefix_p"})[0]
            rows = table.findAll("tr")
            columns = [v.text.replace('\n', '').replace('\r', '') for v in rows[0].find_all('th')]
            df = pd.DataFrame(columns=columns)

            # 全行のうちのある行成分について
            for i in range(len(rows)):
                tds_tmp = rows[i].find_all('td')
                tds = [ tds.text.replace('\n', '').replace('\r', ' ').replace('\u3000', ' ').replace(' ','') for tds in tds_tmp ]
                
                if (len(tds)-1) == len(columns):
                    insert_pstats(url, tds)       
                    
        except req_error.HTTPError as e:
            print(e.reason)
        except IndexError as e:
            print(e)
            tds = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
            insert_pstats(url, tds)
        except Exception as e:
            print(e)


# In[50]:


try:
  
    df = read_player()
    active_pstats_update(df)    
    
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




