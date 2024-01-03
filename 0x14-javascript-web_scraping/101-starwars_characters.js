#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const filmId = process.argv[2];

function fetchCharacters (display) {
  request.get(url, (error, response, body) => {
    if (error) {
      console.log(error);
      return;
    }
    const films = JSON.parse(body).results;
    const movie = films.find((item) => item.url.endsWith(`/${filmId}/`));
    display(movie.characters);
  });
}

fetchCharacters((charactersURLs) => {
  for (let i = 0; i < charactersURLs.length; i++) {
    request.get(charactersURLs[i], (error, response, character) => {
      if (error) {
        console.log(error);
        return;
      }
      console.log(JSON.parse(character).name);
    });
  }
});
