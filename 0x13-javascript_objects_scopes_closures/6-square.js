#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let s = '';
      for (let i = 0; i < this.width; i++) {
        s += c;
      }
      for (let i = 0; i < this.height; i++) {
        console.log(s);
      }
    }
  }
};
