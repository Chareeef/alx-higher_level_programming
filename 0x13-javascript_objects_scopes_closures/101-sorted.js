#!/usr/bin/node
const dict = require('./101-data').dict;

const newDict = {};

for (const key in dict) {
  const nbOfOccurences = dict[key];
  if (newDict[nbOfOccurences] === undefined) {
    newDict[nbOfOccurences] = [];
  }
  newDict[nbOfOccurences].push(key);
}

console.log(newDict);
