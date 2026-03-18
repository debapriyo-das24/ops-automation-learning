#!/usr/bin/env python
# coding: utf-8

# In[3]:


# lesser_of_two_evens(2,4) --> 2, if both are even, returning the minimum value
# lesser_of_two_evens(2,5) --> 5, if one is not even, returning the maximum value


# In[11]:


def lesser_of_two_evens(a,b):
    if a %2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)


# In[13]:


lesser_of_two_evens(4,5)


# In[15]:


lesser_of_two_evens(100,43)


# In[17]:


# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False


# In[19]:


def animal_crackers(text):
    k = text.split()

    if k[0][0] == k[1][0]:
        return True
    else:
        return False


# In[21]:


animal_crackers('Levelheaded Llama')


# In[23]:


animal_crackers('Crazy Kangaroo')


# In[28]:


#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
#makes_twenty(20,10) --> True
#makes_twenty(12,8) --> True
#makes_twenty(2,3) --> False


# In[30]:


def makes_twenty(a,b):
    if a+b==20 or a==20 or b==20:
        return True
    else:
        return False


# In[32]:


makes_twenty(20,9)


# In[34]:


makes_twenty(1,3)


# In[36]:


makes_twenty(10,10)


# In[38]:


#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
 
#old_macdonald('macdonald') --> MacDonald
#Note: 'macdonald'.capitalize() returns 'Macdonald'


# In[108]:


def old_macdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        print ("name is too short")


# In[110]:


old_macdonald('macdonald')


# In[112]:


old_macdonald('sweet')


# In[78]:


# MASTER YODA: Given a sentence, return a sentence with the words reversed
## master_yoda('I am home') --> 'home am I'
## master_yoda('We are ready') --> 'ready are We'


# In[104]:


def master_yoda(text):
    k = text.split()
    return " ".join(k[::-1])


# In[106]:


master_yoda('I am home')


# In[114]:


#ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
#almost_there(90) --> True
#almost_there(104) --> True
#almost_there(150) --> False
#almost_there(209) --> True


# In[118]:


def almost_there(n):
    if (abs(100-n) <= 10) or (abs(200-n) <= 10):
        return True
    else:   
        return False


# In[120]:


almost_there(150)


# In[122]:


almost_there(110)


# In[ ]:




