#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#2000-2021のNPB選手を年代別にCSVへ


# In[79]:


from bs4 import BeautifulSoup
import urllib.request as req
import pandas as pd
import random
import time


# In[80]:


teams = ['https://npb.jp/bis/players/search/yearly/@@@/1954001/'
        ,'https://npb.jp/bis/players/search/yearly/@@@/1961001/'
        ,'https://npb.jp/bis/players/search/yearly/@@@/1968001/'
        ,'https://npb.jp/bis/players/search/yearly/@@@/2012001/'
        ,'https://npb.jp/bis/players/search/yearly/@@@/1947001/'
        ,'https://npb.jp/bis/players/search/yearly/@@@/2006001/']


# In[81]:


def get_list(player, df):
    for i in range(len(player)):
        player_link = player[i].get('href').replace('/bis/players/', '')
        player_name_tmp = player[i].findAll("dd", {"class":"name"})
        player_name =  [ v.text.replace('\n', '').replace('\r', ' ').replace('\u3000', ' ').replace(' ','') for v in player_name_tmp]
        s = pd.Series([player_link, player_name[0]], index=["url", "player"])
        df = df.append(s, ignore_index=True)
    return df


# In[82]:


def write_csv(team):
    for num in range(2021, 2000, -1):
        df = pd.DataFrame({"url": [], "player": []})
        tmp_time = random.randrange(1, 30)
        time.sleep(tmp)
        year_url = team.replace('@@@', str(num))
        print(year_url)
        response = req.urlopen(year_url)
        parse_html = BeautifulSoup(response, 'html.parser')
        three_column_player = parse_html.findAll("div", {"class":"three_column_player"})[0]
        player = three_column_player.findAll("a")
        df = get_list(player, df)
        
#       チーム名
        team_name = ''
        if('1954001' in year_url): team_name = 'dragons'
        if('1961001' in year_url): team_name = 'tigers'
        if('1968001' in year_url): team_name = 'carp'
        if('2012001' in year_url): team_name = 'dena'
        if('1947001' in year_url): team_name = 'giants'
        if('2006001' in year_url): team_name = 'swallows'

        df.to_csv(str(num) + '_' + team_name + '_' + 'data.csv', encoding = 'utf8',  header=False, index=False)


# In[83]:


for team in teams:
    write_csv(team)


# In[84]:


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




