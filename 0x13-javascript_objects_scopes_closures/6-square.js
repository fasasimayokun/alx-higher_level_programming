#!/usr/bin/node
const SquareFirst = require('./5-square');

class Square extends SquareFirst {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let nm = 0; nm < this.height; nm++) {
      let st = '';
      for (let m = 0; m < this.width; m++) {
        st += c;
      }
      console.log(st);
    }
  }
}

module.exports = Square;
