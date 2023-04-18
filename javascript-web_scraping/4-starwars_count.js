#!/usr/bin/node
const process = require('process');
const request = require('request');
const args = process.argv;
request(args[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  let count = 0;
  const movies = JSON.parse(body).results;
  for (const mov in movies) {
    for (const char in mov.characters) {
      if (char.includes('18')) {
        count = count + 1;
      }
    }
  }
  console.log(count);
});
