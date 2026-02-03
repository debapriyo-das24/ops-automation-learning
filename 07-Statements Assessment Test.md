___

<a href='https://www.udemy.com/user/joseportilla/'><img src='../Pierian_Data_Logo.png'/></a>
___
<center><em>Content Copyright by Pierian Data</em></center>

# Statements Assessment Test
Let's test your knowledge!

_____
**Use <code>for</code>, .split(), and <code>if</code> to create a Statement that will print out words that start with 's':**


```python
st = 'Print only the words that start with s in this sentence'
```


```python
st = 'Print only the words that start with s in this sentence'
for letter in st.split():
    if letter[0] == 's':
        print(letter)
```

    start
    s
    sentence
    

______
**Use range() to print all the even numbers from 0 to 10.**


```python
lst = [x for x in range(0,11) if x%2 == 0]
lst
```




    [0, 2, 4, 6, 8, 10]



___
**Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.**


```python
lst = [x for x in range(0,50) if x % 3 == 0]
lst
```




    [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]



_____
**Go through the string below and if the length of a word is even print "even!"**


```python
st = 'Print every word in this sentence that has an even number of letters'
```


```python
st = 'Print every word in this sentence that has an even number of letters'
for letter in st.split():
    if len(letter)%2 ==0:
        print("even!")
    else:
        print(letter)
```

    Print
    every
    even!
    even!
    even!
    even!
    even!
    has
    even!
    even!
    even!
    even!
    letters
    

____
**Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".**


```python
lst = range(0,101)

for x in lst:
    if x%3 == 0 and x%5 == 0:
        print("FizzBuzz")
    elif x%3 == 0:
        print("Fizz")
    elif x%5 == 0:
        print("Buzz")
    else:
        print(x)
```

    FizzBuzz
    1
    2
    Fizz
    4
    Buzz
    Fizz
    7
    8
    Fizz
    Buzz
    11
    Fizz
    13
    14
    FizzBuzz
    16
    17
    Fizz
    19
    Buzz
    Fizz
    22
    23
    Fizz
    Buzz
    26
    Fizz
    28
    29
    FizzBuzz
    31
    32
    Fizz
    34
    Buzz
    Fizz
    37
    38
    Fizz
    Buzz
    41
    Fizz
    43
    44
    FizzBuzz
    46
    47
    Fizz
    49
    Buzz
    Fizz
    52
    53
    Fizz
    Buzz
    56
    Fizz
    58
    59
    FizzBuzz
    61
    62
    Fizz
    64
    Buzz
    Fizz
    67
    68
    Fizz
    Buzz
    71
    Fizz
    73
    74
    FizzBuzz
    76
    77
    Fizz
    79
    Buzz
    Fizz
    82
    83
    Fizz
    Buzz
    86
    Fizz
    88
    89
    FizzBuzz
    91
    92
    Fizz
    94
    Buzz
    Fizz
    97
    98
    Fizz
    Buzz
    

____
**Use List Comprehension to create a list of the first letters of every word in the string below:**


```python
st = 'Create a list of the first letters of every word in this string'
```


```python
st = 'Create a list of the first letters of every word in this string'

[word[0] for word in st.split()]
```




    ['C', 'a', 'l', 'o', 't', 'f', 'l', 'o', 'e', 'w', 'i', 't', 's']



### Great Job!
