#!/usr/bin/node
// a script that prints the title of a Star Wars movie where the
// episode number matches a given integer.
// The first argument is the movie ID
// You must use the Star wars API with the endpoint
// https://swapi-api.alx-tools.com/api/films/:id u must use the module request

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const text = JSON.parse(body);
    console.log(text.title);
  }
});
