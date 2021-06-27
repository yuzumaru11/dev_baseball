#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3

dbname = 'Baseball.db'
conn = sqlite3.connect(dbname)
# sqliteを操作するカーソルオブジェクトを作成
cur = conn.cursor()

# playerテーブル作成
cur.execute('drop table player')

# データベースへコミット
conn.commit()
conn.close()


# In[ ]:





# In[ ]:




