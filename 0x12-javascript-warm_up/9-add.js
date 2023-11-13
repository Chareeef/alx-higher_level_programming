#!/usr/bin/node
/* Add Two Numbers from argv */

function add (a, b) {
  return a + b;
}

const argv = process.argv;

console.log(add(Number(argv[2]), Number(argv[3])));
