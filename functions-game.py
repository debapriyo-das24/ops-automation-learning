#!/usr/bin/env python
# coding: utf-8

# In[1]:


def check_even(mylist):
    for num in mylist:
        if num % 2 == 0:
            return True
        else:
            pass

    return False


# In[5]:


check_even([11,12,14,15,2,3,6,9,8,7])


# In[7]:


check_even([1,11,15,13,17,87,97,99,33])


# In[19]:


def check_even(mylist):
    #placeholder variables
    even_num = []
    
    for num in mylist:
        if num % 2 == 0:
            even_num.append(num)
        else:
            pass

    return even_num    


# In[21]:


check_even([1,2,3,5,66,76,78,8,9,5,4,3,5])


# In[35]:


work_hours = [('Abby',100), ('Toby',200), ('Lewis',150), ('Cole',490)]


# In[37]:


def employee_champ(work_hours):
    #placeholder variables
    current_max = 0
    employee_name = ''

    for employee,hours in work_hours:
        if hours > current_max:
            employee_name = employee
            current_max = hours
        else:
            pass

    return (employee_name, current_max)
    


# In[41]:


result = employee_champ(work_hours)


# In[43]:


result


# In[45]:


name,hours = employee_champ(work_hours)


# In[47]:


name


# In[49]:


hours


# In[51]:


#guessing game


# In[53]:


example_list = [1,2,3,4,5,6,7,8,9]


# In[55]:


from random import shuffle


# In[57]:


shuffle(example_list)


# In[59]:


example_list


# In[69]:


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


# In[71]:


shuffle_list([1,2,3,4,5,6,33,55])


# In[67]:


mylist = [' ', 'O', ' ']


# In[73]:


shuffle_list(mylist)


# In[79]:


def player_guess():
    
    guess = ''

    while guess not in ['0', '1', '2']:
        guess = input("Choose a number - 0, 1 or 2 -  ")

    return int(guess)


# In[81]:


player_guess()


# In[83]:


my_index = player_guess()


# In[85]:


my_index


# In[89]:


def check_guess(mylist, guess):

    if mylist[guess] == 'O':
        print("You are correct!")
    else:
        print("EHH. WRONGG. Try Again!")
        print(mylist)      


# In[91]:


#Initial List
mylist = [' ', 'O', ' ']

#Shuffle List
mixedup_list = shuffle_list(mylist)

# Guess by the user
guess = player_guess()

# result
check_guess(mixedup_list,guess)


# In[93]:


#Initial List
mylist = [' ', 'O', ' ']

#Shuffle List
mixedup_list = shuffle_list(mylist)

# Guess by the user
guess = player_guess()

# result
check_guess(mixedup_list,guess)


# In[103]:


#Initial List
mylist = [' ', 'O', ' ']

#Shuffle List
mixedup_list = shuffle_list(mylist)

# Guess by the user
guess = player_guess()

# result
check_guess(mixedup_list,guess)


# In[ ]:




