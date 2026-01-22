```python
p = 100/67
print(f"The result of the division -{p:0.2f}")
```

    The result of the division -1.49
    


```python
p = "ABCDEF\nGHIJKLM\nONP"
print(f"The sliced |letters |{p[2::2]}|")
```

    The sliced |letters |CE
    HJL
    N|
    


```python
my_list = ['One','two','three']
my_list
```




    ['One', 'two', 'three']




```python
my_list[0] = 'One more for you'
my_list
```




    ['One more for you', 'two', 'three']




```python
another_list = ['seven','eight','nine']
new_list=my_list + another_list
new_list
```




    ['One more for you', 'two', 'three', 'seven', 'eight', 'nine']




```python
new_list.append('rudimentary fault in counting')
new_list
```




    ['One more for you',
     'two',
     'three',
     'seven',
     'eight',
     'nine',
     'rudimentary fault in counting']




```python
new_list[::-1]
```




    ['rudimentary fault in counting',
     'nine',
     'eight',
     'seven',
     'three',
     'two',
     'One more for you']




```python
new_list[::1]
```




    ['One more for you',
     'two',
     'three',
     'seven',
     'eight',
     'nine',
     'rudimentary fault in counting']




```python
new_list.pop(2)
```




    'three'




```python
new_list
```




    ['One more for you', 'two', 'seven', 'eight', 'nine']




```python
new_list = ['a','c','w','h','r','t','b']
num_list = [1,2,67,90,5,34,56,23,78]
new_list.sort()
```


```python
new_list
```




    ['a', 'b', 'c', 'h', 'r', 't', 'w']




```python
num_list.sort()
```


```python
num_list
```




    [1, 2, 5, 23, 34, 56, 67, 78, 90]




```python
type(num_list)
```




    list




```python
num_list.reverse()
```


```python
num_list
```




    [90, 78, 67, 56, 34, 23, 5, 2, 1]




```python
num_list.sort()
```


```python
num_list
```




    [1, 2, 5, 23, 34, 56, 67, 78, 90]




```python
matrix = [new_list, num_list]
matrix
```




    [['a', 'b', 'c', 'h', 'r', 't', 'w'], [1, 2, 5, 23, 34, 56, 67, 78, 90]]




```python
matrix[0][0]
```




    'a'




```python
matrix[0]
```




    ['a', 'b', 'c', 'h', 'r', 't', 'w']




```python

```
