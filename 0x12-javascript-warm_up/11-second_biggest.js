#!/usr/bin/node
const { argv } = require('node:process');
const numbers = [];
for (let idx = 2; idx < argv.length; idx++) {
  numbers[idx - 2] = parseInt(argv[idx]);
}
const sorted = numbers.sort();
console.log(sorted[argv.length - 4]);
