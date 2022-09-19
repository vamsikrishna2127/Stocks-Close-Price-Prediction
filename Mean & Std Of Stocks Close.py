#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np

import pandas as pd

from pandas import Series, DataFrame

import matplotlib.pyplot as plt

import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


df1 = pd.read_csv(r"C:\Users\99200\OneDrive\Pictures\Documents\HDFCBANK1.txt")


# In[4]:


df1.head(5)


# In[5]:


df1.drop(['Series','Date','Prev Close','High','Low','Last','VWAP','Volume','Turnover','Trades','Deliverable Volume','%Deliverble'],axis=1,inplace=True)


# In[6]:


df1.head(5)


# In[7]:


df1Mean = df1["Close"].mean()

print('Mean Of DataFrame1 :',df1Mean)


# In[8]:


df1Std = df1['Close'].std()

print('Standard Deviation Of DataFrame1 :',df1Std)


# In[9]:


df2 = pd.read_csv(r"C:\Users\99200\OneDrive\Pictures\Documents\KOTAKBANK1.txt")


# In[10]:


df2.head(5)


# In[11]:


df2.drop(['Series','Date','Prev Close','High','Low','Last','VWAP','Volume','Turnover','Trades','Deliverable Volume','%Deliverble'],axis=1,inplace=True)


# In[12]:


df2.head(5)


# In[13]:


df2Mean = df2["Close"].mean()

print('Mean Of DataFrame2 :',df2Mean)


# In[14]:


df2Std = df2['Close'].std()

print('Standard Deviation Of DataFrame2 :',df2Std)


# In[15]:


df3 = pd.read_csv(r"C:\Users\99200\OneDrive\Pictures\Documents\RELIANCE1.txt")


# In[16]:


df3.head(5)


# In[17]:


df3.drop(['Series','Date','Prev Close','High','Low','Last','VWAP','Volume','Turnover','Trades','Deliverable Volume','%Deliverble'],axis=1,inplace=True)


# In[18]:


df3.head(5)


# In[19]:


df3Mean = df3["Close"].mean()

print('Mean Of DataFrame3 :',df3Mean)


# In[20]:


df3Std = df3['Close'].std()

print('Standard Deviation Of DataFrame3 :',df3Std)


# In[21]:


frames1 = [df1, df2]
  
result1 = pd.concat(frames1)

display(result1)


# In[22]:


frames2 = [result1, df3]
  
result2 = pd.concat(frames2)

display(result2)


# In[23]:


dfMean = result2["Close"].mean()

print('Mean Of Total DataFrame :',dfMean)

dfStd = result2['Close'].std()

print('Standard Deviation Of Total DataFrame :',dfStd)


# In[27]:


import tkinter as tk  
from functools import partial  
   
   
def call_result(label_result1,label_result2):  
    result1 = dfMean
    result2 = dfStd
    label_result1.config(text="Mean Of All Three Stocks = %d" % result1)  
    label_result2.config(text="Std Of All Three Stocks = %d" % result2)
    return  
   
root = tk.Tk()  
root.geometry('400x200+100+200')  
  
root.title('Mean And Standard Deviation Of Close In Different Stocks')  
  
labelNum1 = tk.Label(root, text="HDFCBANK STOCKS").grid(row=1, column=0) 

#buttonCal1 = tk.Button(root, text="Click", command=call_result).grid(row=1, column=3) 
  
labelNum2 = tk.Label(root, text="KOTAKBANK STOCKS").grid(row=5, column=0)

#buttonCal2 = tk.Button(root, text="Click", command=call_result).grid(row=3, column=3) 

labelNum3 = tk.Label(root, text="RELIANCE STOCKS").grid(row=10, column=0)

#buttonCal3 = tk.Button(root, text="Click", command=call_result).grid(row=5, column=3) 

labelNum4 = tk.Label(root, text="All STOCKS").grid(row=12, column=0)

#buttonCal4 = tk.Button(root, text="Click", command=call_result).grid(row=7, column=3) 
  
labelResult1 = tk.Label(root)  
  
labelResult1.grid(row=11, column=3)

labelResult2 = tk.Label(root)  
  
labelResult2.grid(row=13, column=3)
  
call_result = partial(call_result, labelResult1, labelResult2)  
  
buttonCal = tk.Button(root, text="Click", command=call_result).grid(row=20, column=0)  
  
root.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


import tkinter as tk  
from functools import partial  
   
def call_result1(label_result1,label_result2):  
    result1 = df1Mean
    result2 = df1Std
    label_result1.config(text="Mean Of DataFrame1 = %d" % result1)  
    label_result2.config(text="Std Of DataFrame1 = %d" % result2)
    return 
   
root = tk.Tk()

root.geometry('400x200+100+200')  
  
root.title('Mean And Standard Deviation Of Close In Different Stocks')  
  
labelNum1 = tk.Label(root, text="HDFCBANK STOCKS").grid(row=1, column=0) 

buttonCal1 = tk.Button(root, text="Click", command=call_result1).grid(row=1, column=3) 
  
labelNum2 = tk.Label(root, text="KOTAKBANK STOCKS").grid(row=3, column=0)

buttonCal2 = tk.Button(root, text="Click", command=call_result2).grid(row=3, column=3) 

labelNum3 = tk.Label(root, text="RELIANCE STOCKS").grid(row=5, column=0)

buttonCal3 = tk.Button(root, text="Click", command=call_result3).grid(row=5, column=3) 

labelNum4 = tk.Label(root, text="All STOCKS").grid(row=7, column=0)

buttonCal4 = tk.Button(root, text="Click", command=call_result4).grid(row=7, column=3) 
  
labelResult1 = tk.Label(root)  
  
labelResult1.grid(row=11, column=2)

labelResult2 = tk.Label(root)  
  
labelResult2.grid(row=13, column=2)

call_result1 = partial(call_result1, labelResult1, labelResult2)  
  
buttonCal = tk.Button(root, text="Click", command=call_result1).grid(row=9, column=0)  
  
root.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:




