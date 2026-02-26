#!/usr/bin/env python
# coding: utf-8

# In[1]:


mylist = [0,4,56,3,2,6]


# In[5]:


help(mylist.sort)


# In[7]:


#can look for help in docs.python as it contains the readme on every single update


# In[14]:


from platform import python_version
print(python_version())


# In[18]:


print('hello')


# In[20]:


def add_function(num1,num2):
    return num1+num2


# In[22]:


result = add_function(1,2)
print(result)


# In[28]:


def greeting_name(name):
    print(f"Hello {name}!")


# In[30]:


greeting_name('Debapriyo')


# In[57]:


def say_hello(name):
    print('So that is your name.')
    print(f'Hello {name}')


# In[59]:


say_hello('Jose')


# In[61]:


def add_num(num1,num2,num3):
    return num1+num2+num3


# In[63]:


add_num(1,4,5)


# In[67]:


result = add_num(20,89,11)


# In[69]:


result


# In[73]:


def print_result(a,b):
    print(a+b)


# In[75]:


def return_result(a,b):
    return a+b


# In[77]:


print_result(1,3)


# In[79]:


return_result(1,3)


# In[81]:


result = return_result(1,4)


# In[83]:


result


# In[95]:


def sum_game(num1,num2):
    '''
It is to calculate the subtraction result between two numbers.
    '''
    return num2-num1


# In[97]:


sum_game(45,21)


# In[105]:


def sum_game(num1,num2):
    '''
It is to calculate the addition of two numbers.
    '''
    return num1+num2


# In[107]:


sum_game('kol','kata')


# In[109]:


# This is the fault of python as it is flexible with data types


# In[111]:


20 % 2 == 0


# In[113]:


def even_checker(a):
    if a % 2 == 0:
        print(f"{a} is Even!")
    else:
        print(f"{a} is ODD")


# In[115]:


even_checker(23)


# In[117]:


even_checker(1122233444)


# In[119]:


def even_checker(b):
    return b % 2 == 0


# In[121]:


even_checker(43)


# In[123]:


def check_even_list(numlist):

    for num in numlist:
        if num % 2 == 0:
            return True
        else:
            pass


# In[125]:


check_even_list([2,3,4,5,6,7])


# In[127]:


check_even_list([9,7,1,3,39])


# In[129]:


# It does not return anything as there is no even number in the list


# In[131]:


def check_even_list(numlist):

    for num in numlist:
        if num % 2 == 0:
            return True
        else:
            pass
    return False        


# In[133]:


check_even_list([1,3,13,11,19])


# In[135]:


# Here need to place the False return with the for loop statement, because if placed inside the indentation of if and else argument
# it will only look for the first number as return makes the code stop


# In[137]:


# now I will return all the even numbers in a list


# In[145]:


def return_even_list(numlist):

    even_numbers = []

    for num in numlist:
        if num % 2 == 0:
            even_numbers.append(num)

        else:
            pass

    return even_numbers


# In[147]:


return_even_list([21,22,25,26,23,24,28,29,34,32,30,36,33])


# In[ ]:




