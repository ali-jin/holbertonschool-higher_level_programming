#!/usr/bin/node
const process = require('process');
const args = process.argv;
let arg;
args.forEach((val, index) => {
  if (index === 2) {
    arg = val;
  } if (index === 1) {
    arg = 'No argument';
  }
});
console.log(arg);
