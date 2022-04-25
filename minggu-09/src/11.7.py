#!/usr/bin/env python
# coding: utf-8

# In[1]:


from array import array
a = array('H', [4000, 10, 700, 22222])
sum(a)


# In[2]:


from array import array
a = array('H', [4000, 10, 700, 22222])
sum(a)

a[1:3]


# In[3]:


from collections import deque
d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())


# In[4]:


import bisect
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
scores


# In[5]:


from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)                      
heappush(data, -5)                 
[heappop(data) for i in range(3)]


# In[ ]:




