#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
df = pd.read_csv('netflix_titles.csv')


# In[4]:


df


# In[5]:


import sqlalchemy as sal
engine = sal.create_engine('mssql://DESKTOP-4HBM6FL\SQLEXPRESS/master?driver=ODBC+DRIVER+17+FOR+SQL+SERVER')
conn=engine.connect()


# In[6]:


df.to_sql('netflix_raw', con=conn, index=False, if_exists = 'append') 
conn.close()

# difference between replace and append is that - replace will create new table and decide datatypes but append 
# would load the data in the existing table (that we have created).


# In[77]:


#df[df.show_id=='s5023']


# In[78]:


# max(df.description.dropna().str.len()) # max(df.cast.dropna().str.len())

