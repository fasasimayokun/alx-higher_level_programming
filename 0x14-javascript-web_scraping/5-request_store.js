#!/usr/bin/node
//  a script that gets the contents of a webpage and stores it in a file

const request = require('request');
const fs = require('fs');

request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(process.argv[3], body, 'utf-8', function (error) {
      if (error) {
        console.log(error);
      }
    });
  }
});
