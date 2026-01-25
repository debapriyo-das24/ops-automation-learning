```python
%%writefile myfile.txt
Hello this is a text file.
There are not a whole of words here.
This is the last line.
```

    Writing myfile.txt
    


```python
myfile = open('myfile.txt')
```


```python
pwd
```




    'C:\\Users\\deb11'




```python
content = myfile.read()
```


```python
myfile.read()
```




    ''




```python
#this is because the cursor at the end is blinking
```


```python
myfile.read(0)
```




    ''




```python
myfile.read()
```




    ''




```python
myfile.seek(0)
```




    0




```python
contents = myfile.read()
```


```python
myfile.seek(0)
```




    0




```python
content= myfile.read()
```


```python
content
```




    'Hello this is a text file.\nThere are not a whole of words here.\nThis is the last line.\n'




```python
myfile.seek(0)
```




    0




```python
myfile.readlines()
```




    ['Hello this is a text file.\n',
     'There are not a whole of words here.\n',
     'This is the last line.\n']




```python
myfile.close()
```


```python
with open('myfile.txt') as my_new_file:
    contents = my_new_file.read()
```


```python
contents
```




    'Hello this is a text file.\nThere are not a whole of words here.\nThis is the last line.\n'




```python
contents
```




    'Hello this is a text file.\nThere are not a whole of words here.\nThis is the last line.\n'




```python
with open('myfile.txt',mode='r') as myfile:
    contents = myfile.read()
```


```python
contents
```




    'Hello this is a text file.\nThere are not a whole of words here.\nThis is the last line.\n'




```python
%%writefile my_new_file.txt
One line
Two lines
Three lines
```

    Writing my_new_file.txt
    


```python
with open('my_new_file.txt', mode='r') as f:
    print(f.read())
```

    One line
    Two lines
    Three lines
    
    


```python
with open('my_new_file.txt', mode = 'a') as f:
    f.write('Four lines')
```


```python
with open('my_new_file.txt', mode='r') as f:
    print(f.read())
```

    One line
    Two lines
    Three lines
    
    Four linesFour lines
    


```python
with open('jujube.txt', mode='w' ) as f:
    f.write('I just created this file')
```


```python
with open('jujube.txt', mode='r' ) as f:
    print(f.read())
```

    I just created this file
    


```python

```
