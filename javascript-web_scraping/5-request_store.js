#!/usr/bin/node
const process = require('process');
const request = require('request');
const args = process.argv;
const fs = require('fs');
request(args[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(args[3], body, (err) => {
      if (err) throw err;
    });
  }
});
