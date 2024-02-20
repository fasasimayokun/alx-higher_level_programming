#!/usr/bin/node
// a script that prints all characters of a Star Wars movie:

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const text = JSON.parse(body);
    const characters = text.characters;

    for (const character of characters) {
      request.get(character, (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          const characterNames = JSON.parse(body);
          console.log(characterNames.name);
        }
      });
    }
  }
});
