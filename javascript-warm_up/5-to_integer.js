#!/usr/bin/node
const process = require('process');
const args = process.argv;
if (isNaN(parseInt(args[2]))) {
  console.log('Not a number');
} else if (args.lenght === 2) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(args[2]));
}
