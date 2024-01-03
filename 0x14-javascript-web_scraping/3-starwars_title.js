#!/usr/bin/node
const request = require('request');
const filmId = process.argv[2];

request.get(`https://swapi-api.alx-tools.com/api/films/${filmId}`, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const dict = JSON.parse(body);
  console.log(dict.title);
});
