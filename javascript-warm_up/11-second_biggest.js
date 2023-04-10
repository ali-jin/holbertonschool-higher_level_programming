#!/usr/bin/node
const process = require('process');
const args = process.argv;

function nextBiggest (arr) {
  let max = 0;
  let result = 0;

  args.forEach((val, index) => {
    const nr = Number(val);

    if (nr > max) {
      [result, max] = [max, nr];
    } else if (nr < max && nr > result) {
      result = nr;
    }
  });

  return result;
}
console.log(nextBiggest(args));
