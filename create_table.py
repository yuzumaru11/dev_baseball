#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sqlite3

dbname = 'Baseball.db'
conn = sqlite3.connect(dbname)
# sqliteを操作するカーソルオブジェクトを作成
cur = conn.cursor()

# playerテーブル作成
cur.execute(
    'CREATE TABLE player(id INTEGER PRIMARY KEY AUTOINCREMENT, url STRING, team STRING, name STRING)')
cur.execute(
    'CREATE UNIQUE INDEX nameindex on player(url, team)')



# データベースへコミット
conn.commit()
conn.close()


# In[ ]:




