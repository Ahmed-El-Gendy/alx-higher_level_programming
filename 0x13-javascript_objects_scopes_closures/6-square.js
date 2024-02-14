#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  constructor (c) {
    this.ch = c;
  }

  charPrint () {
    let s = '';
    if (this.ch === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        s += this.ch;
      }
      for (let i = 0; i < this.height; i++) {
        console.log(s);
      }
    }
  }
};
