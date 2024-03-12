#!/usr/bin/node
const OldSquare = require('./5-square');

class Square extends OldSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let x = 0; x < this.height; x++) {
      let row = '';
      for (let y = 0; y < this.width; y++) {
        row += c;
      }
      console.log(row);
    }
  }
}

module.exports = Square;
