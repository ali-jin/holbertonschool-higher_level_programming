#!/usr/bin/node
const process = require('process');
const nbArg = process.argv;
if (nbArg.length === 2) {
  console.log('No argument');
} else if (nbArg.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
