#!/usr/bin/node
const list = require('./100-data').list;

const newList = list.map((current, idx) => current * idx);

console.log(list);
console.log(newList);
