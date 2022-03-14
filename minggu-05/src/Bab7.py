#!/usr/bin/env python
# coding: utf-8

# Contoh Program 7.1.

# In[1]:


s = "Hello, world." 
str(s)


# In[2]:


repr(s)


# In[3]:


str(1/7)


# In[4]:


x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'


# In[5]:


print(s)


# In[6]:


hello = 'hello, world\n'
hellos = repr(hello)


# In[7]:


print(hellos)


# In[8]:


repr((x, y, ('spam', 'eggs')))


# Contoh Program 7.1.1.

# In[9]:


import math 
print(f'The value of pi is approximately {math.pi:.3f}.')


# In[10]:


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')


# In[11]:


animals = 'eels'
print(f'My hovercraft is full of {animals}.')


# In[12]:


print(f'My hovercraft is full of {animals!r}.')


# Contoh Program 7.1.2.

# In[13]:


for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))


# Contoh Program 7.2.2.

# In[14]:


import json
x = [1, 'simple', 'list']


# In[15]:


json.dumps(x)


# In[ ]:




