#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 本日時点の試合数で「m_games]を更新


# In[265]:


import datetime
import pandas as pd
import random
import pymysql


# In[266]:


conn = pymysql.connect(host='localhost',
                         user='root',
                         password='yuzumaru11',
                         db='bbdata',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
cursor = conn.cursor()


# In[267]:


def update_mGames(team_id):
    # 登録値
    year1 = datetime.date.today().year
    now1 = datetime.datetime.now().strftime("%Y-%m-%d")
    baseball = 'baseball'
    teams = team_id

    sql = "select games from t_cranks where day1 = '" + str(now1) + "' and team = '" + teams + "';"
    cursor.execute(sql)
    result = cursor.fetchone()
    
    if result is None:
        sql = "select games from t_pranks where day1 = '" + str(now1) + "' and team = '" + teams + "';"
        cursor.execute(sql)
        result = cursor.fetchone()
        games = result['games']
    
    games = result['games']

    sql = "select count(*) count from m_games where year1 = '" + str(year1) + "' and teams = '" + teams + "';"
    cursor.execute(sql)
    result = cursor.fetchone()
    
    if(result['count'] < 1):
        sql = "insert into m_games(year1, teams, games, udate, uuser, rdate, ruser) values(             '" + str(year1) + "'             , '" + teams + "'             , '" + str(games) + "'             , '" + now1 + "'             , '" + baseball + "'             , '" + now1 + "'             , '" + baseball + "' )"
        print(sql)
        cursor.execute(sql)
        conn.commit()
        
    elif(result['count'] == 1):
        
        sql = "update m_games set             year1 = '" + str(year1) + "'             , teams = '" + teams + "'             , games = '" + str(games) + "'             , udate = '" + now1 + "'             , uuser = '" + baseball + "' where teams = '" + teams + "' and year1 = '" + str(year1) + "';"
        cursor.execute(sql)
        conn.commit()
    else:
        pass


# In[268]:


try:
    sql = "select * from m_teams"
    cursor.execute(sql)
    m_teams = cursor.fetchall()
    
    for team in m_teams:
        update_mGames(team['id']) 
        

except Exception as e:
    print(e)
finally:
    conn.close() 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




