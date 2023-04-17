#!/usr/bin/node
const process = require('process');
const request = require('request');
const args = process.argv;
request.get(
  args[2],
  function (error, response, body) {
    if (!error && response.statusCode === 200) {
      console.log('code: ' + response.statusCode);
    } else {
      console.log('code: ' + response.statusCode);
    }
  }
);
