#!/usr/bin/env python
# coding: utf-8

# # assingment of data wrangeling where we have to solve numpy qutions

# In[44]:


#Use numpy to generate array of 25 random numbers sampled 
#from a standard normal distribution.
import numpy as np

mat = np.random.randn(3,4)
print('random values ,matrix\n%s\n'%mat)


# In[47]:


#Create a random vector of size 30 and find the mean value.
from numpy import random

a=random.randint(1000,size=(30))
b=a.mean()
print("mean of a is",b)


# In[54]:


#Insert 1 to 100 numbers in a numpy array and reshape it to 
import numpy as np
from numpy import random

mat = random.randint(100,size=(10,10))
print('random values ,matrix\n%s\n'%mat)


# In[57]:


# Create a 10x10 array with random values and find the minimum and maximum values.
import numpy as np
from numpy import random

mat = np.random.randn(3,4)


print('random values ,matrix\n%s\n'%mat)
print ('Overall min of matrix is %s\n'%np.min(mat))
print ('Overall max of matrix is %s\n'%np.max(mat))


# In[58]:


#Find Dot product of two arrays

#f = np.array([1,2])

#g = np.array([4,5])

import numpy as np

f = np.array([1,2]) 
g = np.array([4,5])
print(f)
print(g)
a=np.dot(f,g)
print("The Dot Product is: ",a)


# In[64]:


#Concatenate following arrays along axis=0
import numpy as np

x=np.array([[1,2],[3,4]])
y=np.array([[5,6]])
print('Array 1 :','\n',x)
print('Array 2 :','\n',y)
print('Concatenate along row :','\n',np.concatenate((x,y),axis=0))


# In[68]:


#How to get the common items between two python numpy arrays?
import numpy as np

a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
print("The common items are: ",np.intersect1d(a,b))


# In[69]:


#Sort the numpy array:
array = np.array([10,5,8,4,7,2,3,1])
print("the sorted iteam are:"',',np.sort(array))

