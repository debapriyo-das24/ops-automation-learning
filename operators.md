```python
for num in range(0,10):
    print(num)
```

    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    


```python
for num in range(0,101,15):
    print(num)
```

    0
    15
    30
    45
    60
    75
    90
    


```python
range(0,101,15)
```




    range(0, 101, 15)




```python
list(range(0,101,15))
```




    [0, 15, 30, 45, 60, 75, 90]




```python
index_count = 0
word = 'abcde'

for letter in word:
    print(word[index_count])
    index_count += 1
```

    a
    b
    c
    d
    e
    


```python
word = 'abcde'

for item in enumerate(word):
    print(item)
```

    (0, 'a')
    (1, 'b')
    (2, 'c')
    (3, 'd')
    (4, 'e')
    


```python
for index,item in enumerate(word):
    print(index)
    print(item)
    print('\n')
```

    0
    a
    
    
    1
    b
    
    
    2
    c
    
    
    3
    d
    
    
    4
    e
    
    
    


```python
# both the operators work in loops - range and enumerate.
```


```python
mylist1 = [1,2,3]
mylist2 = ['a','b','c']

for item,label in zip(mylist1,mylist2):
    print(item)
    print(label)
    print('\n')
```

    1
    a
    
    
    2
    b
    
    
    3
    c
    
    
    


```python
#zip works only when with even sets
```


```python
list(zip(mylist1,mylist2))
```




    [(1, 'a'), (2, 'b'), (3, 'c')]




```python
'x' in [1,2,3]
```




    False




```python
'x' in ['x','y','z']
```




    True




```python
'a' in 'a whole new world'
```




    True




```python
d = {'key1':1}

'key1' in d.keys()
```




    True




```python
mylist = [10,20,30,40,100]
min(mylist)
```




    10




```python
max(mylist)
```




    100




```python
from random import shuffle
```


```python
mylist = [1,2,3,4,5,6,7,8,9,10]

shuffle(mylist)
```


```python
mylist
```




    [6, 7, 10, 9, 8, 1, 2, 4, 5, 3]




```python
from random import randint
```


```python
mynum = randint(0,99)
```


```python
mynum
```




    69




```python
result = input("What is your age?")
```

    What is your age? 29
    


```python
result
```




    '29'




```python
int(result)
```




    29




```python

```
