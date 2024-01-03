# Web Scraping with JavaScript

## Introduction
This project explores web scraping techniques using JavaScript. The goal is to retrieve and manipulate data from web pages using various methods, including JSON data manipulation, API requests with `request` and `fetch`, and file system operations using the `fs` module.

## JSON Data Manipulation
JavaScript provides robust support for JSON (JavaScript Object Notation) data. To manipulate JSON data:

1. **Parsing JSON**: Use `JSON.parse()` to convert JSON strings into JavaScript objects.
    ```javascript
    const jsonString = '{"name": "John", "age": 30}';
    const jsonObject = JSON.parse(jsonString);
    ```

2. **Stringifying JSON**: Use `JSON.stringify()` to convert JavaScript objects into JSON strings.
    ```javascript
    const object = { name: 'Jane', age: 25 };
    const jsonString = JSON.stringify(object);
    ```

## Using `request` and `fetch` API
### `request` Module (Node.js)
The `request` module simplifies HTTP requests in Node.js.
```javascript
const request = require('request');

request('https://api.example.com/data', (error, response, body) => {
    if (!error && response.statusCode === 200) {
        const data = JSON.parse(body);
        // Process retrieved data
    }
});
```

### `fetch` API (Browser)
The `fetch` API allows making HTTP requests in modern browsers.
```javascript
fetch('https://api.example.com/data')
    .then(response => response.json())
    .then(data => {
        // Process retrieved data
    })
    .catch(error => console.error('Error:', error));
```

## Reading and Writing Files with `fs` Module
The `fs` module in Node.js enables file system operations:

### Reading a File
```javascript
const fs = require('fs');

fs.readFile('data.txt', 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log(data);
});
```

### Writing to a File
```javascript
const fs = require('fs');

const newData = 'New data to write to file.';
fs.writeFile('newFile.txt', newData, err => {
    if (err) {
        console.error(err);
        return;
    }
    console.log('Data written successfully!');
});
```

## Conclusion
This README provides an overview of using JavaScript for web scraping, covering JSON data manipulation, making HTTP requests using `request` and `fetch` APIs, and file system operations with the `fs` module. Experiment with these concepts to extract and handle data efficiently from various web sources.
