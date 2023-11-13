#!/usr/bin/node
/* Print 'C is fun' x times */

const occurences = parseInt(process.argv[2]);

if (!isNaN(occurences)) {
  for (let i = 0; i < occurences; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurences');
}
