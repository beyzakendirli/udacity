#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1 Popular times of travel (i.e., occurs most often in the start time)
most common month
most common day of week
most common hour of day

#2 Popular stations and trip
most common start station
most common end station
most common trip from start to end (i.e., most frequent combination of start station and end station)

#3 Trip duration
total travel time
average travel time

#4 User info
counts of each user type
counts of each gender (only available for NYC and Chicago)
earliest, most recent, most common year of birth (only available for NYC and Chicago)


# In[1]:


import pandas as pd
import numpy as np
import datetime as dt

filename_1 = 'C:/Users/admKendirliB/chicago.csv'
filename_2 = 'C:/Users/admKendirliB/new_york_city.csv'
filename_3 = 'C:/Users/admKendirliB/washington.csv'

chi = pd.read_csv(filename_1)
nyc = pd.read_csv(filename_2)
was = pd.read_csv(filename_3)


# In[3]:


merge = pd.concat([chi,nyc,was],axis=0)


# In[4]:


merge.head()


# In[11]:


merge['Month'] = pd.DatetimeIndex(merge['Start Time']).month


# In[12]:


merge['Year'] = pd.DatetimeIndex(merge['Start Time']).year


# In[13]:


#most common month
print(merge.groupby(['Month'])['Month'].count().sort_values(ascending=False).index[0])


# In[18]:


merge['Week'] = pd.DatetimeIndex(merge['Start Time']).week


# In[20]:


#most common day of week
print(merge.groupby(['Week'])['Week'].count().sort_values(ascending=False).index[0])


# In[21]:


merge['Hour'] = pd.DatetimeIndex(merge['Start Time']).hour


# In[22]:


#most common hour of day
print(merge.groupby(['Hour'])['Hour'].count().sort_values(ascending=False).index[0])


# In[23]:


#most common start station
print(merge.groupby(['Start Station'])['Start Station'].count().sort_values(ascending=False).index[0])


# In[24]:


#most common end station
print(merge.groupby(['End Station'])['End Station'].count().sort_values(ascending=False).index[0])


# In[35]:


#total travel time
sum = merge['Trip Duration'].sum()
print("Sum:", '{:.2f}'.format(sum))


# In[36]:


#average travel time
print(merge['Trip Duration'].mean())


# In[37]:


#counts of each user type
print(merge.groupby(['User Type'])['User Type'].count().sort_values(ascending=False))


# In[38]:


#counts of each gender (only available for NYC and Chicago)
print(merge.groupby(['Gender'])['Gender'].count().sort_values(ascending=False))


# In[39]:


#Earliest, most recent, most common year of birth (only available for NYC and Chicago)
#Earliest: 
print("Earliest :", merge['Birth Year'].min())

#Most recent: 
print("Most recent :", merge['Birth Year'].max())

#Most common: 
print("Most common :", merge.groupby(['Birth Year'])['Birth Year'].count().sort_values(ascending=False).index[0])


# In[ ]:




