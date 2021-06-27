#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3

# Baseball.dbを作成
# すでに存在していれば、それにアスセス
dbname = 'Baseball.db'
conn = sqlite3.connect(dbname)

# データベースへのコネクションを閉じる
conn.close()


# In[ ]:




