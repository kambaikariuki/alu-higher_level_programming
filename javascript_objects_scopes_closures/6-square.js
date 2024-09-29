#!/usr/bin/node
const Rectangle = require('./4-rectangle');

const Square = class Square extends Rectangle {
    constructor (size) {
        super(size, size);
    }
    charPrint(c) {
      if (c) {
        let prints = '';
        for (let cont = 0; cont < this.height; cont++) {
          for (let cont = 0; cont < this.height; cont++) {
            prints = prints + c;
            }
            console.log(prints);
            prints = '';
        }
      } else {
          super.print();
      }
    }
};

module.exports = Square;
