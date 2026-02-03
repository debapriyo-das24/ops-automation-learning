___

<a href='https://www.udemy.com/user/joseportilla/'><img src='../Pierian_Data_Logo.png'/></a>
___
<center><em>Content Copyright by Pierian Data</em></center>
# Objects and Data Structures Assessment Test

## Test your knowledge. 

** Answer the following questions **

Write (or just say out loud to yourself) a brief description of all the following Object Types and Data Structures we've learned about. You can edit the cell below by double clicking on it. Really this is just to test if you know the difference between these, so feel free to just think about it, since your answers are self-graded.

Double-click HERE to edit this markdown cell and write answers.

Numbers: Stores numerical information, which can be integers or floating decimal points.

Strings: An ordered sequence of letters within single or double quotes, and has immutability. 

Lists: An ordered sequence of mutable objects. Delimiters - [] 

Tuples: An ordered sequence of immutable objects. Delimiters - ()

Dictionaries: Key-value pairings that are not ordered. Delimiters - {}


## Numbers

Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.

Hint: This is just to test your memory of the basic arithmetic commands, work backwards from 100.25


```python
(40*5)/(6+4) + (2**5) + 50-2 + 1/4
```




    100.25



Answer these 3 questions without typing code. Then type code to check your answer.

    What is the value of the expression 4 * (6 + 5) = 44
    
    What is the value of the expression 4 * 6 + 5 = 29
    
    What is the value of the expression 4 + 6 * 5 = 34


```python
4 * (6 + 5)
```




    44




```python
4 * 6 + 5
```




    29




```python
4 + 6 * 5
```




    34



What is the *type* of the result of the expression 3 + 1.5 + 4?<br><br>

- Floating Point number as shown below


```python
type(3 + 1.5 + 4)
```




    float



What would you use to find a number’s square root, as well as its square? 


```python
# Square root:
2**.5
```




    1.4142135623730951




```python
# Square:
2**2
```




    4



## Strings

Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:


```python
s = 'hello'
# Print out 'e' using indexing

s[1]
```




    'e'



Reverse the string 'hello' using slicing:


```python
s ='hello'
# Reverse the string using slicing

s[::-1]
```




    'olleh'



Given the string hello, give two methods of producing the letter 'o' using indexing.


```python
s ='hello'
# Print out the 'o'

# Method 1:
s[4]

```




    'o'




```python
# Method 2:

s[-1]
```




    'o'



## Lists

Build this list [0,0,0] two separate ways.


```python
# Method 1:
list1= [0,0,0]
list1
```




    [0, 0, 0]




```python
# Method 2:
list2 = [0]
list2 * 3
```




    [0, 0, 0]



Reassign 'hello' in this nested list to say 'goodbye' instead:


```python
list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
list3
```




    [1, 2, [3, 4, 'goodbye']]



Sort the list below:


```python
list4 = [5,3,4,6,1]
list4.sort()
```


```python
list4
```




    [1, 3, 4, 5, 6]



## Dictionaries

Using keys and indexing, grab the 'hello' from the following dictionaries:


```python
d = {'simple_key':'hello'}
# Grab 'hello'
d['simple_key']
```




    'hello'




```python
d = {'k1':{'k2':'hello'}}
# Grab 'hello'
d['k1']['k2']
```




    'hello'




```python
# Getting a little tricker
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

#Grab hello
d['k1'][0]['nest_key'][1][0]
```




    'hello'




```python
# This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}

d['k1'][2]['k2'][1]['tough'][2][0]
```




    'hello'



Can you sort a dictionary? Why or why not?<br><br>
No we cannot as it is dictated by key-value pairings i.e. mappings, which can be any type of object.

## Tuples

What is the major difference between tuples and lists?<br><br>
Tuples are immutable and help in maintaining data integrity.

How do you create a tuple?<br><br> 


```python
t = (1,2,3)
t
```




    (1, 2, 3)



## Sets 

What is unique about a set?<br><br>

Sets do not allow duplicate values to be included.

Use a set to find the unique values of the list below:


```python
list5 = [1,2,2,33,4,4,11,22,3,3,2]

x = set(list5)
x
```




    {1, 2, 3, 4, 11, 22, 33}



## Booleans

For the following quiz questions, we will get a preview of comparison operators. In the table below, a=3 and b=4.

<table class="table table-bordered">
<tr>
<th style="width:10%">Operator</th><th style="width:45%">Description</th><th>Example</th>
</tr>
<tr>
<td>==</td>
<td>If the values of two operands are equal, then the condition becomes true.</td>
<td> (a == b) is not true.</td>
</tr>
<tr>
<td>!=</td>
<td>If values of two operands are not equal, then condition becomes true.</td>
<td> (a != b) is true.</td>
</tr>
<tr>
<td>&gt;</td>
<td>If the value of left operand is greater than the value of right operand, then condition becomes true.</td>
<td> (a &gt; b) is not true.</td>
</tr>
<tr>
<td>&lt;</td>
<td>If the value of left operand is less than the value of right operand, then condition becomes true.</td>
<td> (a &lt; b) is true.</td>
</tr>
<tr>
<td>&gt;=</td>
<td>If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.</td>
<td> (a &gt;= b) is not true. </td>
</tr>
<tr>
<td>&lt;=</td>
<td>If the value of left operand is less than or equal to the value of right operand, then condition becomes true.</td>
<td> (a &lt;= b) is true. </td>
</tr>
</table>

What will be the resulting Boolean of the following pieces of code (answer fist then check by typing it in!)


```python
# Answer before running cell
2 > 3
```




    False




```python
# Answer before running cell
3 <= 2
```




    False




```python
# Answer before running cell
3 == 2.0
```




    False




```python
# Answer before running cell
3.0 == 3
```




    True




```python
# Answer before running cell
4**0.5 != 2
```




    False



Final Question: What is the boolean output of the cell block below?


```python
# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?
l_one[2][0] >= l_two[2]['k1'] #false
```




    False



## Great Job on your first assessment! 
