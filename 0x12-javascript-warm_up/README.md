# JavaScript - Warm up

## Why JavaScript Programming is Amazing

JavaScript is a versatile and powerful programming language that runs in the browser, making it an integral part of web development. Here are some reasons why JavaScript is amazing:

- **Versatility:** JavaScript is not limited to web development; it can be used for server-side development, mobile app development, and even desktop applications.
  
- **Client-Side Interaction:** With JavaScript, you can create dynamic and interactive user interfaces, enhancing the user experience on websites.
  
- **Large Community:** JavaScript has a vast and active community, providing a wealth of resources, libraries, and frameworks that make development faster and more efficient.

- **Asynchronous Programming:** JavaScript supports asynchronous programming, allowing for non-blocking operations, which is crucial for handling events and providing a smooth user experience.

## How to Run a JavaScript Script

To run a JavaScript script, follow these steps:

1. **Environment Setup:** Ensure you have a JavaScript environment set up. This could be a web browser console, Node.js, or a JavaScript runtime environment.

2. **Create a Script File:** Write your JavaScript code in a file with a `.js` extension. For example, `myscript.js`.

3. **Run the Script:**
    - For web browsers, open the developer console (usually by pressing `F12`), go to the "Console" tab, and paste or link your script.
    - For Node.js, open a terminal, navigate to the script's directory, and run `node myscript.js`.

## How to Create Variables and Constants

In JavaScript, you can create variables using `var`, `let`, or `const`:

```javascript
// Variable declaration with var
var variableName = "Hello, World!";

// Variable declaration with let (block-scoped)
let myNumber = 42;

// Constant declaration with const (block-scoped)
const PI = 3.14;
```

## Differences Between var, const, and let

- `var`: Function-scoped, can be redeclared and reassigned.
- `let`: Block-scoped, can be reassigned but not redeclared.
- `const`: Block-scoped, cannot be redeclared or reassigned after declaration.

## Data Types in JavaScript

JavaScript has several data types:
- **Primitive Types:** `string`, `number`, `boolean`, `null`, `undefined`, `symbol`.
- **Object Types:** `object`, `array`, `function`.
  
## How to Use if, if ... else Statements

```javascript
let condition = true;

if (condition) {
  console.log("Condition is true");
} else {
  console.log("Condition is false");
}
```

## How to Use Comments

```javascript
// This is a single-line comment

/*
  This is a
  multi-line comment
*/
```

## How to Affect Values to Variables

```javascript
let x = 10;
let y = "Hello";

x = 20; // Reassigning value to variable
```

## How to Use while and for Loops

```javascript
// While loop
let i = 0;
while (i < 5) {
  console.log(i);
  i++;
}

// For loop
for (let j = 0; j < 5; j++) {
  console.log(j);
}
```

## How to Use break and continue Statements

```javascript
for (let i = 0; i < 10; i++) {
  if (i === 5) {
    break; // Exit the loop when i is 5
  }
  console.log(i);
}

for (let i = 0; i < 10; i++) {
  if (i === 5) {
    continue; // Skip the iteration when i is 5
  }
  console.log(i);
}
```

## What is a Function and How to Use Functions

```javascript
// Function declaration
function greet(name) {
  console.log("Hello, " + name + "!");
}

// Function call
greet("John");
```

## What Does a Function That Does Not Use Any Return Statement Return

A function in JavaScript that does not use a `return` statement implicitly returns `undefined`.

## Scope of Variables

- Variables declared with `var` are function-scoped.
- Variables declared with `let` and `const` are block-scoped.

## Arithmetic Operators and How to Use Them

```javascript
let a = 5;
let b = 2;

let sum = a + b;
let difference = a - b;
let product = a * b;
let quotient = a / b;
let remainder = a % b;
```

## How to Manipulate Dictionary (Object)

```javascript
// Creating an object (dictionary)
let person = {
  name: "John",
  age: 25,
  profession: "Developer"
};

// Accessing values
console.log(person.name); // Outputs: John

// Modifying values
person.age = 26;

// Adding a new key-value pair
person.location = "City";
```

## How to Import a File

In JavaScript, file importing is done as follows:

```javascript
// Assuming 'otherFile.js' is in the same directory
const otherFile = require('./otherFile');
```

Ensure that the file path is correct, and the file you want to import/export follows the appropriate syntax for the environment.
