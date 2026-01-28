```python
if True:
    print("It's true")
```

    It's true
    


```python
hungry = False
if hungry:
    print("Feed me")
```


```python
if hungry:
    print("Feed me")
else:
    print("Im not hungry")
```

    Im not hungry
    


```python
loc = "bank"
if loc == "car shop":
    print("So many cars")
elif loc == "bank":
    print("Money is cool")
else:
    print("at that boring place")
```

    Money is cool
    


```python
mylist = [1,2,3,4,5,6,7,8,9,10]

for num in mylist:
    print(num)
```

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    


```python
for num in mylist:
    print("Hello")
```

    Hello
    Hello
    Hello
    Hello
    Hello
    Hello
    Hello
    Hello
    Hello
    Hello
    


```python
for num in mylist:
    #check for Even numbers
    if num%2 == 0:
        print(f"Even Number - {num}")
    else:
        print(f"Odd Number - {num}")
```

    Odd Number - 1
    Even Number - 2
    Odd Number - 3
    Even Number - 4
    Odd Number - 5
    Even Number - 6
    Odd Number - 7
    Even Number - 8
    Odd Number - 9
    Even Number - 10
    


```python
num_sum = 0

for num in mylist:
    num_sum = num_sum + num

print(num_sum)
```

    55
    


```python
num_sum = 0

for num in mylist:
    num_sum = num_sum + num
    print(num_sum)
```

    1
    3
    6
    10
    15
    21
    28
    36
    45
    55
    


```python

for cool in 'Hello World':
    print('cool')
```

    cool
    cool
    cool
    cool
    cool
    cool
    cool
    cool
    cool
    cool
    cool
    


```python
j = [(1,2),(3,4),(5,6),(7,8)]

for (a,b) in j:
    print(a)
    print(b)
```

    1
    2
    3
    4
    5
    6
    7
    8
    


```python
#this is called tuple unpacking
```


```python
for a,b in j:
    print(b)
```

    2
    4
    6
    8
    


```python
mylist = [(1,2,3),(4,5,6),(7,8,9)]

for item in mylist:
    print(item)
```

    (1, 2, 3)
    (4, 5, 6)
    (7, 8, 9)
    


```python
for a,b,c in mylist:
    print(a,b,c)
```

    1 2 3
    4 5 6
    7 8 9
    


```python
for a,b,c in mylist:
    print(a)
```

    1
    4
    7
    


```python
d = {'k1':1, 'k2':2, 'k3':3, 'k4':4}

for item,value in d.items():
    print(value)
```

    1
    2
    3
    4
    


```python
 e = 10, 20, 30, 40, 5, 6, 7, 8
num_e = 0
for num in e:
    num_e = num_e + num
    
print(f"The sum is = {num_e}")
```

    The sum is = 126
    


```python

```
