#!/usr/bin/node
const array = process.argv.slice(2);
const number = parseInt(array[0]);
function factorial (n) {
  if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
if (isNaN(array[0])) {
  console.log(1);
} else {
  console.log(factorial(number));
}
