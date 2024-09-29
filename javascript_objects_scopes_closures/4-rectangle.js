#!/usr/bin/node
class Rectangle {
    constructor(h, w) {
        if (h > 0 && w > 0) {
            this.height = h;
            this.width = w;
        }
    }

    print() {
      let prints = '';
      for (let cont1 = 0; cont1 < this.height; cont1++) {
        for (let cont = 0; cont < this.width; cont++) {
          prints = prints + 'X';
        }
        console.log(prints);
        prints = '';
      }
    }

    rotate() {
      let temp;
      temp = this.height;
      this.height = this.width;
      this.width = temp;
    }

    double() {
      this.height *= 2;
      this.width *= 2;
    }
}
module.exports = Rectangle;
