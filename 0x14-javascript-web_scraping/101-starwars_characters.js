#!/usr/bin/node
// a script that prints all characters of a Star Wars movie:

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, function (error, response, body) {
  if (!error) {
    const text = JSON.parse(body);
    const characters = text.characters;

    displayCharacters(characters, 0);
  }
});

function displayCharacters (characters, index) {
  request(characters[index], (error, response, body) => {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        displayCharacters(characters, index + 1);
      }
    }
  });
}
