{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c6105e07",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "After local assignment: test spam\n",
      "After nonlocal assignment: nonlocal spam\n",
      "After global assignment: nonlocal spam\n",
      "In global scope: global spam\n"
     ]
    }
   ],
   "source": [
    "def scope_test():\n",
    "    def do_local():\n",
    "        spam = \"local spam\"\n",
    "\n",
    "    def do_nonlocal():\n",
    "        nonlocal spam\n",
    "        spam = \"nonlocal spam\"\n",
    "\n",
    "    def do_global():\n",
    "        global spam\n",
    "        spam = \"global spam\"\n",
    "\n",
    "    spam = \"test spam\"\n",
    "    do_local()\n",
    "    print(\"After local assignment:\", spam)\n",
    "    do_nonlocal()\n",
    "    print(\"After nonlocal assignment:\", spam)\n",
    "    do_global()\n",
    "    print(\"After global assignment:\", spam)\n",
    "\n",
    "scope_test()\n",
    "print(\"In global scope:\", spam)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "eaba4e09",
   "metadata": {},
   "outputs": [],
   "source": [
    "class MyClass:\n",
    "    \"\"\"A simple example class\"\"\"\n",
    "    i = 12345\n",
    "\n",
    "    def f(self):\n",
    "        return 'hello world'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "1c215d53",
   "metadata": {},
   "outputs": [],
   "source": [
    "x = MyClass()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "9df82350",
   "metadata": {},
   "outputs": [],
   "source": [
    "def __init__(self):\n",
    "    self.data = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "7a0ec264",
   "metadata": {},
   "outputs": [],
   "source": [
    "x = MyClass()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "36024299",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(3.0, -4.5)"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "class Complex:\n",
    "    def __init__(self, realpart, imagpart):\n",
    "        self.r = realpart\n",
    "        self.i = imagpart\n",
    "\n",
    "x = Complex(3.0, -4.5)\n",
    "x.r, x.i"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "0f037c1d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "16\n"
     ]
    }
   ],
   "source": [
    "x.counter = 1\n",
    "while x.counter < 10:\n",
    "    x.counter = x.counter * 2\n",
    "print(x.counter)\n",
    "del x.counter"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "603ae529",
   "metadata": {},
   "outputs": [],
   "source": [
    "x.f()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9fcb6a3a",
   "metadata": {},
   "outputs": [],
   "source": [
    "xf = x.f\n",
    "while True:\n",
    "    print(xf())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "f033f622",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (Temp/ipykernel_7280/3718359173.py, line 7)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"C:\\Users\\MICROS~1\\AppData\\Local\\Temp/ipykernel_7280/3718359173.py\"\u001b[1;36m, line \u001b[1;32m7\u001b[0m\n\u001b[1;33m    >>> d = Dog('Fido')\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "class Dog:\n",
    "\n",
    "    kind = 'canine'         \n",
    "    def __init__(self, name):\n",
    "        self.name = name    \n",
    "\n",
    ">>> d = Dog('Fido')\n",
    ">>> e = Dog('Buddy')\n",
    ">>> d.kind                  \n",
    ">>> e.kind                  \n",
    "'canine'\n",
    ">>> d.name                 \n",
    "'Fido'\n",
    ">>> e.name                 \n",
    "'Buddy'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "38557d71",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (Temp/ipykernel_7280/2554956307.py, line 11)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"C:\\Users\\MICROS~1\\AppData\\Local\\Temp/ipykernel_7280/2554956307.py\"\u001b[1;36m, line \u001b[1;32m11\u001b[0m\n\u001b[1;33m    >>> d = Dog('Fido')\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "class Dog:\n",
    "\n",
    "    tricks = []            \n",
    "\n",
    "    def __init__(self, name):\n",
    "        self.name = name\n",
    "\n",
    "    def add_trick(self, trick):\n",
    "        self.tricks.append(trick)\n",
    "\n",
    ">>> d = Dog('Fido')\n",
    ">>> e = Dog('Buddy')\n",
    ">>> d.add_trick('roll over')\n",
    ">>> e.add_trick('play dead')\n",
    ">>> d.tricks\n",
    "['roll over', 'play dead']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "f86afb0f",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (Temp/ipykernel_7280/809809327.py, line 10)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"C:\\Users\\MICROS~1\\AppData\\Local\\Temp/ipykernel_7280/809809327.py\"\u001b[1;36m, line \u001b[1;32m10\u001b[0m\n\u001b[1;33m    >>> d = Dog('Fido')\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "class Dog:\n",
    "\n",
    "    def __init__(self, name):\n",
    "        self.name = name\n",
    "        self.tricks = []    \n",
    "\n",
    "    def add_trick(self, trick):\n",
    "        self.tricks.append(trick)\n",
    "\n",
    ">>> d = Dog('Fido')\n",
    ">>> e = Dog('Buddy')\n",
    ">>> d.add_trick('roll over')\n",
    ">>> e.add_trick('play dead')\n",
    ">>> d.tricks\n",
    "['roll over']\n",
    ">>> e.tricks\n",
    "['play dead']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "82083002",
   "metadata": {},
   "outputs": [],
   "source": [
    ">>> class Warehouse:\n",
    "        purpose = 'storage'\n",
    "        region = 'west'\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "fd14b44a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "storage west\n"
     ]
    }
   ],
   "source": [
    "w1 = Warehouse()\n",
    "print(w1.purpose, w1.region)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "853112ed",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "storage east\n"
     ]
    }
   ],
   "source": [
    "w2 = Warehouse()\n",
    "w2.region = 'east'\n",
    "print(w2.purpose, w2.region)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "5abfdcef",
   "metadata": {},
   "outputs": [],
   "source": [
    "def f1(self, x, y):\n",
    "    return min(x, x+y)\n",
    "\n",
    "class C:\n",
    "    f = f1\n",
    "\n",
    "    def g(self):\n",
    "        return 'hello world'\n",
    "\n",
    "    h = g"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "db485cbf",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Mapping:\n",
    "    def __init__(self, iterable):\n",
    "        self.items_list = []\n",
    "        self.__update(iterable)\n",
    "\n",
    "    def update(self, iterable):\n",
    "        for item in iterable:\n",
    "            self.items_list.append(item)\n",
    "\n",
    "    __update = update   \n",
    "\n",
    "class MappingSubclass(Mapping):\n",
    "\n",
    "    def update(self, keys, values):\n",
    "        # provides new signature for update()\n",
    "        # but does not break __init__()\n",
    "        for item in zip(keys, values):\n",
    "            self.items_list.append(item)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "57cd3c90",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Employee:\n",
    "    pass\n",
    "\n",
    "john = Employee()  \n",
    "\n",
    "\n",
    "john.name = 'John Doe'\n",
    "john.dept = 'computer lab'\n",
    "john.salary = 1000"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "1265d53a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "1\n",
      "2\n",
      "3\n",
      "one\n",
      "two\n",
      "1\n",
      "2\n",
      "3\n"
     ]
    },
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'myfile.txt'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32mC:\\Users\\MICROS~1\\AppData\\Local\\Temp/ipykernel_7280/2624536843.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      7\u001b[0m \u001b[1;32mfor\u001b[0m \u001b[0mchar\u001b[0m \u001b[1;32min\u001b[0m \u001b[1;34m\"123\"\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      8\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mchar\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 9\u001b[1;33m \u001b[1;32mfor\u001b[0m \u001b[0mline\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mopen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"myfile.txt\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     10\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mline\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mend\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m''\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'myfile.txt'"
     ]
    }
   ],
   "source": [
    "for element in [1, 2, 3]:\n",
    "    print(element)\n",
    "for element in (1, 2, 3):\n",
    "    print(element)\n",
    "for key in {'one':1, 'two':2}:\n",
    "    print(key)\n",
    "for char in \"123\":\n",
    "    print(char)\n",
    "for line in open(\"myfile.txt\"):\n",
    "    print(line, end='')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "4f2335ce",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<str_iterator at 0x2c52beaf460>"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s = 'abc'\n",
    "it = iter(s)\n",
    "it"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "33531150",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'a'"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "next(it)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "609d766b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'b'"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "next(it)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "4b4f957a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'c'"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "next(it)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "2a533f2d",
   "metadata": {},
   "outputs": [
    {
     "ename": "StopIteration",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mStopIteration\u001b[0m                             Traceback (most recent call last)",
      "\u001b[1;32mC:\\Users\\MICROS~1\\AppData\\Local\\Temp/ipykernel_7280/600241529.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mnext\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mit\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mStopIteration\u001b[0m: "
     ]
    }
   ],
   "source": [
    "next(it)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "cb12ea83",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Reverse:\n",
    "    \"\"\"Iterator for looping over a sequence backwards.\"\"\"\n",
    "    def __init__(self, data):\n",
    "        self.data = data\n",
    "        self.index = len(data)\n",
    "\n",
    "    def __iter__(self):\n",
    "        return self\n",
    "\n",
    "    def __next__(self):\n",
    "        if self.index == 0:\n",
    "            raise StopIteration\n",
    "        self.index = self.index - 1\n",
    "        return self.data[self.index]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "28f6d7c4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<__main__.Reverse at 0x2c52bfb82b0>"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rev = Reverse('spam')\n",
    "iter(rev)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "2a3d385d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "m\n",
      "a\n",
      "p\n",
      "s\n"
     ]
    }
   ],
   "source": [
    "for char in rev:\n",
    "    print(char)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "a509bb9e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def reverse(data):\n",
    "    for index in range(len(data)-1, -1, -1):\n",
    "        yield data[index]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "5f0fd80b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "f\n",
      "l\n",
      "o\n",
      "g\n"
     ]
    }
   ],
   "source": [
    "for char in reverse('golf'):\n",
    "    print(char)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "ca0939f3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "285"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sum(i*i for i in range(10))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "efff9d87",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "260"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "xvec = [10, 20, 30]\n",
    "yvec = [7, 5, 3]\n",
    "sum(x*y for x,y in zip(xvec, yvec))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "ba0df605",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'page' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32mC:\\Users\\MICROS~1\\AppData\\Local\\Temp/ipykernel_7280/2101593324.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0munique_words\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mset\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mword\u001b[0m \u001b[1;32mfor\u001b[0m \u001b[0mline\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mpage\u001b[0m  \u001b[1;32mfor\u001b[0m \u001b[0mword\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mline\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msplit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'page' is not defined"
     ]
    }
   ],
   "source": [
    "unique_words = set(word for line in page  for word in line.split())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "46441cde",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'graduates' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32mC:\\Users\\MICROS~1\\AppData\\Local\\Temp/ipykernel_7280/1749153666.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mvaledictorian\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mmax\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mstudent\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mgpa\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mstudent\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mname\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mfor\u001b[0m \u001b[0mstudent\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mgraduates\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'graduates' is not defined"
     ]
    }
   ],
   "source": [
    "valedictorian = max((student.gpa, student.name) for student in graduates)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "6423444c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['f', 'l', 'o', 'g']"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data = 'golf'\n",
    "list(data[i] for i in range(len(data)-1, -1, -1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4f2ac340",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
