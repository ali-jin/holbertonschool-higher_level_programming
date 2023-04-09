#!/usr/bin/node
const process = require('process');
const args = process.argv;
const num = args[2];
if (args.length === 2) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < parseInt(num); i++) {
  console.log('C is fun');
}
