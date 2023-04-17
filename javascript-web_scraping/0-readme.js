#!/usr/bin/node
const process = require('process');
const args = process.argv;
const fs = require('fs');
fs.readFile(args[2], 'utf-8', (err, inputD) => {
  if (err) throw err;
  console.log(inputD.toString());
});
