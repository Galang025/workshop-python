#!/usr/bin/env python
# coding: utf-8

# 8.1.

# In[1]:


while True print('Hello world')


# 8.2.

# In[2]:


10 * (1/0)


# In[2]:


4 + spam*3


# In[3]:


'2' + 2


# 8.3.

# In[4]:


while True:
    try:
        x = int(input("Please enter a number : "))
        break
    except ValueError:
            print("Oops! That was no Valid number.   Try Again...")


# In[5]:


class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")


# In[6]:


try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))
    print(inst.args)
    x, y = inst.args
    print('x =', x)
    print('y =', y)


# In[7]:


def this_fails():
    x = 1/0


# In[8]:


try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)


# 8.4.
# 

# In[9]:


raise NameError('HiThere')


# In[10]:


try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')


# In[11]:


try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise


# 8.6.

# In[12]:


try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')


# In[13]:


def bool_return():
    try:
        return True
    finally:
        return False
bool_return()


# In[14]:


def divide(x, y):
    try:
         result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


# In[15]:


divide(2, 1)


# In[16]:


def divide(x, y):
    try:
         result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


# In[17]:


divide(2, 0)


# In[18]:


def divide(x, y):
    try:
         result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


# In[19]:


divide("2", "1")

