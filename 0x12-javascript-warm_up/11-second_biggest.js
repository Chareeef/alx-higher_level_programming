#!/usr/bin/node
/* Searche the second biggest integer in the list of arguments */

const list = process.argv;

if (list.length < 4) {
  console.log(0);
} else {
  let biggest = Number(list[2]);
  let second = Number(list[3]);
  for (let i = 3; i < list.length; i++) {
    const current = Number(list[i]);
    if (second < current) {
      second = current;
    }
    if (biggest < current) {
      second = biggest;
      biggest = current;
    }
  }
  console.log(second);
}
