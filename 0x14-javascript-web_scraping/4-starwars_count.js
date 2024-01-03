#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const dict = JSON.parse(body);
  const filmsList = dict.results;
  let count = 0;
  const characterUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
  for (const film of filmsList) {
    if (film.characters.includes(characterUrl)) {
      count++;
    }
  }

  console.log(count);
});
