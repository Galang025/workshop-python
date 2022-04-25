#!/usr/bin/env python
# coding: utf-8

# In[1]:


import weakref, gc
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)                  
d = weakref.WeakValueDictionary()
d['primary'] = a            
d['primary']                
10
del a                       
gc.collect()                
0
d['primary']                


# In[ ]:




