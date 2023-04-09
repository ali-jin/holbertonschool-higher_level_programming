#!/usr/bin/node
const process = require('process');
const args = process.argv;
function add (a, b) {
  if (args.length <= 2 || isNaN(parseInt(a)) || isNaN(parseInt(b))) {
    console.log('NaN');
  } else {
    console.log(a + b);
  }
}
add(parseInt(args[2]), parseInt(args[3]));
