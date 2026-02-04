```python
st = 'Print only the words that start with s in this sentence'

for letter in st.split():
    if letter[0] == 's':
        print(letter)
```

    start
    s
    sentence
    


```python
lst = [x for x in range(0,23) if x%2 == 0 and x%3 == 0]
lst
```




    [0, 6, 12, 18]




```python
j = 0
for x in lst:
    j = j + x

print(j)
```

    36
    


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
    


```python
lst = range(0,100)

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
    


```python
st = 'Create a list of the first letters of every word in this string'

[word[0] for word in st.split()]
```




    ['C', 'a', 'l', 'o', 't', 'f', 'l', 'o', 'e', 'w', 'i', 't', 's']




```python
juj = 'love makes life worthy'

[word[2] for word in juj.split()]
```




    ['v', 'k', 'f', 'r']




```python
[x for x in range(11)]
```




    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]




```python
[x-2 for x in range(11)]
```




    [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]




```python
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]

thislist.extend(tropical)
```


```python
thislist
```




    ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']




```python
t = [x/2 for x in range(0,23)]
```


```python
[ x**2 for x in t]
```




    [0.0,
     0.25,
     1.0,
     2.25,
     4.0,
     6.25,
     9.0,
     12.25,
     16.0,
     20.25,
     25.0,
     30.25,
     36.0,
     42.25,
     49.0,
     56.25,
     64.0,
     72.25,
     81.0,
     90.25,
     100.0,
     110.25,
     121.0]




```python

```
