#!/usr/bin/node
const request = require('request');
const filmId = process.argv[2];

request.get(`https://swapi-api.alx-tools.com/api/films/${filmId}`, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const charactersURLs = JSON.parse(body).characters;
  for (const url of charactersURLs) {
    request.get(url, (error, response, body) => {
      if (error) {
        console.log(error);
        return;
      }
      console.log(JSON.parse(body).name);
    });
  }
});
