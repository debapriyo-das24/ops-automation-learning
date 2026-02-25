```python
print('Welcome back to python again!\nThis time I am going to learn it all')
```

    Welcome back to python again!
    This time I am going to learn it all
    


```python
mylist = [2,3,4,5,6,7,8,9,10]

for num in mylist:
    if num%2 == 0:
        print(num)
```

    2
    4
    6
    8
    10
    


```python
st = 'Print only the words that start with s in this sentence'
```


```python
p = st.split()

for num in p:
    if num[0] == 's':
        print(num)
```

    start
    s
    sentence
    


```python
st = 'Create a list of the first letters of every word in this string'
```


```python
[word[0] for word in st.split()]
```




    ['C', 'a', 'l', 'o', 't', 'f', 'l', 'o', 'e', 'w', 'i', 't', 's']




```python
x = 0

while x<10:
    print(f"X is lower than 10, i.e. {x}, hence we continue!")
    x=x+1
    if x==10:
        print(f"X is now 10, hence we stop")
```

    X is lower than 10, i.e. 0, hence we continue!
    X is lower than 10, i.e. 1, hence we continue!
    X is lower than 10, i.e. 2, hence we continue!
    X is lower than 10, i.e. 3, hence we continue!
    X is lower than 10, i.e. 4, hence we continue!
    X is lower than 10, i.e. 5, hence we continue!
    X is lower than 10, i.e. 6, hence we continue!
    X is lower than 10, i.e. 7, hence we continue!
    X is lower than 10, i.e. 8, hence we continue!
    X is lower than 10, i.e. 9, hence we continue!
    X is now 10, hence we stop
    


```python
st = 'a for aladdin, if a is an amazing consonant'
[word for word in st.split() if word[0]=='a']
```




    ['a', 'aladdin,', 'a', 'an', 'amazing']




```python
[x for x in range(1,24) if x%4==0]
```




    [4, 8, 12, 16, 20]




```python

```
