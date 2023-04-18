#!/usr/bin/node
const process = require('process');
const request = require('request');
const args = process.argv;
request(args[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const movies = JSON.parse(body).results;
  let count = 0;
  for (const mov of movies) {
    for (const char of mov.characters) {
      if (char.includes('18')) {
        count = count + 1;
      }
    }
  }
  console.log(count);
});
