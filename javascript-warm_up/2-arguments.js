#!/usr/bin/node
const process = require('process');
const nbArg = process.argv;
if (nbArg.length === 2) {
  console.log('No argument');
} else {
  console.log('Arguments found');
}
