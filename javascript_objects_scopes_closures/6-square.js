#!/usr/bin/node
const oldSquare = require('./5-square.js');

module.exports = class Square extends oldSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print(c);
    } else {
      let row;
      for (let i = 0; i < this.height; i++) {
        row = '';
        for (let j = 0; j < this.width; j++) {
          row += c;
        }
        console.log(row);
      }
    }
  }
};
