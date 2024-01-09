#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let nm = 0; nm < this.height; nm++) {
      let st = '';
      for (let m = 0; m < this.width; m++) {
        st += 'X';
      }
      console.log(st);
    }
  }
}

module.exports = Rectangle;
