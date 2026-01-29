```python
from platform import python_version
print(python_version())
```

    3.12.7
    


```python
x = 0
```


```python
while x < 10:
    print(f"This is the value {x}")
    x = x + 1
    
```


```python
x = 0

while x<10:
    print("The value of x is less than 10, adding 1 to x")
    print(f"The value is then {x}")
    x +=1
else:
    print("X is not less than 10")
```

    The value of x is less than 10, adding 1 to x
    The value is then 0
    The value of x is less than 10, adding 1 to x
    The value is then 1
    The value of x is less than 10, adding 1 to x
    The value is then 2
    The value of x is less than 10, adding 1 to x
    The value is then 3
    The value of x is less than 10, adding 1 to x
    The value is then 4
    The value of x is less than 10, adding 1 to x
    The value is then 5
    The value of x is less than 10, adding 1 to x
    The value is then 6
    The value of x is less than 10, adding 1 to x
    The value is then 7
    The value of x is less than 10, adding 1 to x
    The value is then 8
    The value of x is less than 10, adding 1 to x
    The value is then 9
    X is not less than 10
    


```python
# while some_boolean_condition:
    # do_something
#else some_boolean_condition:
    # do_something_else
```


```python
#break , continue, pass
# pass = does nothing at all, used as a placeholder.
# continue = goes to the top of the closest enclosing loop.
# break = breaks out of the closest enclosing loop
```


```python
x = [1,2,3]

for num in x:
    pass

else: 
    print("Nothing in my mind")
```

    Nothing in my mind
    


```python
x = "sammy"

for item in x:
    print(item)
```

    s
    a
    m
    m
    y
    


```python
x = "sammy"

for item in x:
    if item == 'a':
        continue
    print(item)
```

    s
    m
    m
    y
    


```python
x = "sammy"

for item in x:
    if item == 'a':
        break
    print(item)
```

    s
    


```python
x = 0

while x < 5:
    if x == 3:
        break
    print(x)   
    x +=1
```

    0
    1
    2
    


```python

```
