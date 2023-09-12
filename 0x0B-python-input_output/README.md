# Python Input/Output Project README

## Table of Contents
1. [Opening a File](#opening-a-file)
2. [Writing Text to a File](#writing-text-to-a-file)
3. [Reading the Full Content of a File](#reading-the-full-content-of-a-file)
4. [Reading a File Line by Line](#reading-a-file-line-by-line)
5. [Moving the Cursor in a File](#moving-the-cursor-in-a-file)
6. [Ensuring File Closure](#ensuring-file-closure)
7. [Using the "with" Statement](#using-the-with-statement)
8. [Understanding JSON](#understanding-json)
9. [Serialization](#serialization)
10. [Deserialization](#deserialization)
11. [Converting Python Data to JSON](#converting-python-data-to-json)
12. [Converting JSON to Python Data](#converting-json-to-python-data)

---

### 1. Opening a File <a name="opening-a-file"></a>
To open a file in Python, you can use the `open()` function. For example:

```python
file = open('filename.txt', 'r')  # Opens 'filename.txt' for reading ('r' mode)
```

### 2. Writing Text to a File <a name="writing-text-to-a-file"></a>
To write text to a file, open it in write mode ('w') and use the `write()` method:

```python
with open('output.txt', 'w') as file:
    file.write('Hello, World!')
```

### 3. Reading the Full Content of a File <a name="reading-the-full-content-of-a-file"></a>
To read the entire content of a file, use the `read()` method:

```python
with open('filename.txt', 'r') as file:
    content = file.read()
    print(content)
```

### 4. Reading a File Line by Line <a name="reading-a-file-line-by-line"></a>
To read a file line by line, use a `for` loop:

```python
with open('filename.txt', 'r') as file:
    for line in file:
        print(line)
```

### 5. Moving the Cursor in a File <a name="moving-the-cursor-in-a-file"></a>
You can move the cursor within a file using the `seek()` method. For example:

```python
with open('filename.txt', 'r') as file:
    file.seek(10)  # Moves to the 11th byte in the file
    data = file.read()
```

### 6. Ensuring File Closure <a name="ensuring-file-closure"></a>
Python's `with` statement automatically closes files when you're done with them. No need to explicitly call `close()`.

### 7. Using the "with" Statement <a name="using-the-with-statement"></a>
The `with` statement is used to ensure proper resource management. It automatically closes files when the block is exited.

### 8. Understanding JSON <a name="understanding-json"></a>
JSON (JavaScript Object Notation) is a lightweight data interchange format. It's easy for both humans and machines to read and write.

### 9. Serialization <a name="serialization"></a>
Serialization is the process of converting Python data into a JSON string. You can use the `json.dumps()` function.

### 10. Deserialization <a name="deserialization"></a>
Deserialization is the reverse process, converting a JSON string back into a Python data structure using `json.loads()`.

### 11. Converting Python Data to JSON <a name="converting-python-data-to-json"></a>
```python
import json

data = {'name': 'John', 'age': 30}
json_str = json.dumps(data)
```

### 12. Converting JSON to Python Data <a name="converting-json-to-python-data"></a>
```python
import json

json_str = '{"name": "Jane", "age": 25}'
data = json.loads(json_str)
```
