#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const dict = JSON.parse(body);
  const filmsList = dict.results;

  console.log(filmsList.reduce((count, film) => {
    if (film.characters.find((character) => character.endsWith('/18/'))) {
      return count + 1;
    } else {
      return count;
    }
  }, 0));
});
