```python
[x//2 for x in range(11) if x>2]
```




    [1, 2, 2, 3, 3, 4, 4, 5]




```python
x = 0

while x<10:
    print(" x is less than 10 ")
    print(f"Hence adding 1 to it -{x}")
    x = x + 1
    if x == 8:
        print("x has reached 8")
        break
```

     x is less than 10 
    Hence adding 1 to it -0
     x is less than 10 
    Hence adding 1 to it -1
     x is less than 10 
    Hence adding 1 to it -2
     x is less than 10 
    Hence adding 1 to it -3
     x is less than 10 
    Hence adding 1 to it -4
     x is less than 10 
    Hence adding 1 to it -5
     x is less than 10 
    Hence adding 1 to it -6
     x is less than 10 
    Hence adding 1 to it -7
    x has reached 8
    


```python
# need to follow identation and understand loop logic
```


```python
# newlist = [expression for item in iterable if condition == True]
```


```python
t = [x for x in range(0,24) if x%3 == 1]
```


```python
from random import shuffle
```


```python
shuffle(t)
```


```python
t
```




    [13, 7, 10, 16, 1, 19, 4, 22]




```python
list(enumerate('abcde'))
```




    [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')]




```python

```
