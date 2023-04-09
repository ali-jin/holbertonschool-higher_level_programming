#!/usr/bin/node
const process = require('process');
const args = process.argv;
const size = args[2];
if (args.length === 2 || isNaN(parseInt(args[2]))) {
  console.log('Missing size');
}
for (let i = 0; i < size; i++) {
  let row = '';
  for (let j = 0; j < size; j++) {
    row += 'X';
  }
  console.log(row);
}
