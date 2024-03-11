#!/usr/bin/node
function factorial (a) {
  let result = 1;
  for (let idx = a; idx > 0; idx--) {
    result *= idx;
  }
  return result;
}
const { argv } = require('node:process');
const num = parseInt(argv[2]);
console.log(factorial(num));
