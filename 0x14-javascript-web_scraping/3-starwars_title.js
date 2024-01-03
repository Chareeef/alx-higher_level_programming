#!/usr/bin/node
const request = require('request');
const film_id = process.argv[2]

request.get(`https://swapi-api.alx-tools.com/api/films/${film_id}`, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const dict = JSON.parse(body);
  console.log(dict.title);
});
