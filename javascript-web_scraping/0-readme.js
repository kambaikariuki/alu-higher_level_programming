#!/usr/bin/node
const fs = require('fs');
const file = process.argv[2];

fs.readFile(file, 'utf8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
