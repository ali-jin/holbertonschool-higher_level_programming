#!/usr/bin/node
const process = require('process');
const request = require('request');
const args = process.argv;
const search = 'https://swapi-api.hbtn.io/api/people/18/';
request(args[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let count = 0;
    const chars = JSON.parse(body).results;
    for (const i in chars) {
      const result = chars[i].characters;
      for (const j in result) {
        if (result[j].includes(search)) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
