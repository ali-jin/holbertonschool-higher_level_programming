#!/usr/bin/node
const process = require('process');
const args = process.argv;
function factorial (n) {
  if (n === 0 || n === 1 || isNaN(n) || args.length === 2) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
const sum = factorial(parseInt(args[2]));
console.log(sum);
