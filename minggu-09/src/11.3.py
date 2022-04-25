#!/usr/bin/env python
# coding: utf-8

# In[1]:


import struct
with open('myfile.zip', 'rb') as f:
    data = f.read() #untuk membaca file mydile.zip
    
start = 0
for i in range(3): #menampilkan 3 file pertama
    start += 14
    fields = struct.unpact('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields
    
    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)
    
    start += extra_size + comp_size #melanjutkan ke header berikutnya


# In[ ]:




