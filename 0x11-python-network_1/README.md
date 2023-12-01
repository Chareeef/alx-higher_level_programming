### Python - Network #1

Welcome to the Python - Network Project! 🚀 In this endeavor, we'll explore how to fetch internet resources using Python's `urllib` and `requests` packages. These fundamental skills are crucial for any aspiring full-stack developer.

#### Fetching Internet Resources with urllib

**How to fetch internet resources with the Python package urllib:**

To fetch resources using `urllib`, we can leverage the `urllib.request` module. Here's a basic example:

```python
import urllib.request

url = 'https://www.example.com'
response = urllib.request.urlopen(url)
data = response.read()
print(data)
```

**How to decode urllib body response:**

The response obtained from `urllib` can be decoded using the `decode()` method. For instance:

```python
decoded_data = data.decode('utf-8')
print(decoded_data)
```

### Using the Python package requests

**How to make HTTP GET request:**

The `requests` package simplifies making HTTP requests. To perform a GET request:

```python
import requests

url = 'https://www.example.com'
response = requests.get(url)
print(response.text)
```

**How to make HTTP POST/PUT/etc. request:**

For different types of requests like POST, PUT, DELETE, etc., we can use the corresponding methods provided by `requests`. For example:

```python
payload = {'key1': 'value1', 'key2': 'value2'}

# POST request
response_post = requests.post(url, data=payload)

# PUT request
response_put = requests.put(url, data=payload)
```

**How to fetch JSON resources:**

To fetch JSON resources, we can use `requests` and then access the JSON data directly:

```python
response_json = requests.get('https://jsonplaceholder.typicode.com/posts/1')
data_json = response_json.json()
print(data_json)
```

**How to manipulate data from an external service:**

Once we've obtained data from an external service, we can manipulate it based on our requirements. For instance, if we fetched JSON data, we can extract and manipulate specific fields using Python's dictionary operations or other data manipulation techniques.


Happy coding! If you have any questions or want to explore more, feel free to dive deeper into each concept. Keep coding, and letsenjoy our journey to becoming a full-stack developer! 🚀✨
