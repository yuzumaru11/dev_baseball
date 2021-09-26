#!/usr/bin/env python
# coding: utf-8

# In[28]:


#2000-2021のNPB選手を年代別にDBへ


# In[29]:


from bs4 import BeautifulSoup
import urllib.request as req
import pandas as pd
import random
import time
import pymysql


# In[30]:


teams = [
         'https://npb.jp/bis/players/search/yearly/@@@/1954001/'
        ,'https://npb.jp/bis/players/search/yearly/@@@/1961001/'
        ,'https://npb.jp/bis/players/search/yearly/@@@/1968001/'
        ,'https://npb.jp/bis/players/search/yearly/@@@/2012001/'
        ,'https://npb.jp/bis/players/search/yearly/@@@/1993001/'
        ,'https://npb.jp/bis/players/search/yearly/@@@/1947001/'
        ,'https://npb.jp/bis/players/search/yearly/@@@/2006001/' 
        ,'https://npb.jp/bis/players/search/yearly/@@@/1974002/'         
        ,'https://npb.jp/bis/players/search/yearly/@@@/1992001/' 
    
#          'https://npb.jp/bis/players/search/yearly/@@@/2004001/'
#         ,'https://npb.jp/bis/players/search/yearly/@@@/1974001/'
#         ,'https://npb.jp/bis/players/search/yearly/@@@/2005001/'
#         ,'https://npb.jp/bis/players/search/yearly/@@@/1989001/'
#         ,'https://npb.jp/bis/players/search/yearly/@@@/2005002/'
#         ,'https://npb.jp/bis/players/search/yearly/@@@/1991001/'
#         ,'https://npb.jp/bis/players/search/yearly/@@@/2005003/'
#         ,'https://npb.jp/bis/players/search/yearly/@@@/2008001/'
#         ,'https://npb.jp/bis/players/search/yearly/@@@/1979001/'
        ]


# In[31]:


def conndb():
    conn = pymysql.connect(host='localhost',
                         user='root',
                         password='yuzumaru11',
                         db='bbdata',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    return conn


# In[32]:


def get_list(player, df):
    for i in range(len(player)):
        player_link = player[i].get('href').replace('/bis/players/', '')
        player_name_tmp = player[i].findAll("dd", {"class":"name"})
        player_name =  [ v.text.replace('\n', '').replace('\r', ' ').replace('\u3000', ' ').replace(' ','') for v in player_name_tmp]
        s = pd.Series([player_link, player_name[0]], index=["url", "player"])
        df = df.append(s, ignore_index=True)
    return df


# In[33]:


def insert_mPlayer(df, team):
    for i, d in df.iterrows():
        
        conn = conndb()
        cur = conn.cursor()
        
        
        
        try:

            url = str(d['url']).replace(".html", "")
            name = d['player']

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

                sql = "insert into m_player(player_id, teams, player_name, url) values('" + str(player_id) + "', '" + team + "', '" + name + "', '" + format(url, '0>8') + "')"
                cur.execute(sql)

                flg = 0
                sql1 = "insert into m_player_work(player_id, teams, player_name, url, flg, flg1)                         values('" + str(player_id) + "', '" + team + "', '" + name + "', '" + format(url, '0>8') + "', '" + str(flg) + "', '" + str(flg) + "')"
                cur.execute(sql1)
                conn.commit()

            else:
                sql = "update m_player_work set teams= '" + team + "', player_name = '" + name + "' WHERE url = '" + format(url, '0>8') + "'"
                cur.execute(sql)

                sql1 = "update m_player set teams= '" + team + "', player_name = '" + name + "' WHERE url = '" + format(url, '0>8') + "'"
                cur.execute(sql1)
                conn.commit()    
        
        except Exception as e: 
            print(e)
        finally:
            if cur is None:
                cur.close()
            if conn is None:
                conn.close()       


# In[34]:


def insert_player(team):
    for num in range(2000, 2021, 1):
        
        df = pd.DataFrame({"url": [], "player": []})
        tmp_time = random.randrange(1, 5)
        time.sleep(tmp_time)
        year_url = team.replace('@@@', str(num))
        response = req.urlopen(year_url)
        parse_html = BeautifulSoup(response, 'html.parser')
        three_column_player = parse_html.findAll("div", {"class":"three_column_player"})[0]
        player = three_column_player.findAll("a")
               
        df = get_list(player, df)

        if df.empty:
            continue
            
#       チーム名
        team_name = ''
        if('1954001' in year_url): team_name = 'dragons'
        if('1961001' in year_url): team_name = 'tigers'
        if('1968001' in year_url): team_name = 'carp'
        if('2012001' in year_url): team_name = 'baystars'
        if('1993001' in year_url): team_name = 'baystars'
        if('1947001' in year_url): team_name = 'giants'
        if('2006001' in year_url): team_name = 'swallows'
        if('1974002' in year_url): team_name = 'swallows'
        if('1992001' in year_url): team_name = 'marines'
        if('2004001' in year_url): team_name = 'fighters'
        if('1974001' in year_url): team_name = 'fighters'
        if('2005001' in year_url): team_name = 'hawks'
        if('1989001' in year_url): team_name = 'hawks'
        if('2005002' in year_url): team_name = 'buffaloes'
        if('1991001' in year_url): team_name = 'buffaloes'
        if('2005003' in year_url): team_name = 'eagles'
        if('2008001' in year_url): team_name = 'lions'            
        if('1979001' in year_url): team_name = 'lions'
        
        
        # 年毎に登録
        insert_mPlayer(df, team_name)


# In[35]:


for team in teams:
    insert_player(team)


# In[36]:


print('完了')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




