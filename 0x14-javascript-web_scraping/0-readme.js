#!/usr/bin/node
// a script that reads and prints the content of a file
// The first argument is the file path
// The content of the file must be read in utf-8
// If an error occurred during the reading, print the error object

const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', function (error, content) {
  if (error) {
    console.error('Error reading the file:', error);
  } else {
    console.log(content);
  }
});
