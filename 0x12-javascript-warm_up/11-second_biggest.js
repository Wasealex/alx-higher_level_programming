#!/usr/bin/node
const { argv } = require('node:process');
if (argv.length < 4) {
  console.log('0');
} else {
  const numbers = [];
  for (let idx = 2; idx < argv.length; idx++) {
    numbers[idx - 2] = parseInt(argv[idx]);
  }
  const sorted = numbers.sort((a, b) => a - b);
  console.log(sorted[sorted.length - 2]);
}
