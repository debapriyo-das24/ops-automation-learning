```python
my_dict = {'apple':50, 'orange':40, 'pineapple':80, 'sugar':69}
my_dict['apple']
```




    50




```python
my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2'], 'key4': {"col1" : "Red", "col2" : "Green", "col3" : "Orange" }}
my_dict['key4']
```




    {'col1': 'Red', 'col2': 'Green', 'col3': 'Orange'}




```python
my_dict['key2'][2]
```




    33




```python
my_dict.pop('key4')
```




    {'col1': 'Red', 'col2': 'Green', 'col3': 'Orange'}




```python
my_dict['key4']= 'zebra'
my_dict
```




    {'key1': 123,
     'key2': [12, 23, 33],
     'key3': ['item0', 'item1', 'item2'],
     'key4': 'zebra'}




```python
my_dict['key4'].upper()
```




    'ZEBRA'




```python
my_dict.keys()
```




    dict_keys(['key1', 'key2', 'key3', 'key4'])




```python
my_dict['key3']
```




    ['item0', 'item1', 'item2']




```python
my_dict['key2'][1:]
```




    [23, 33]




```python
my_dict.items()
```




    dict_items([('key1', -79507), ('key2', [12, 23, 33]), ('key3', ['item0', 'item1', 'item2']), ('key4', 'zebra')])




```python
my_dict['key1'] *= 43
my_dict['key1']
```




    -43.00000000000001




```python
#dictonaries are mutable and do not retain order or sequence
```


```python
#tuples are immutable
```


```python
t = (1,2,3, 'one')
t
```




    (1, 2, 3, 'one')




```python
#you cannot append or pop values as tuples are useful for data integrity, \ncause when you think of it, the flexibility of Python can result in mutability of values at any time. \nHence this is required, although it has very limited usablility.
```


```python
t = (1,1,1,2,3,3,3, 'three', 'four', 'three')
t
```




    (1, 1, 1, 2, 3, 3, 3, 'three', 'four', 'three')




```python
t.count(1)
```




    3




```python
t.index('three')
```




    7




```python

```
