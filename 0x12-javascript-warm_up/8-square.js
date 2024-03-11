#!/usr/bin/node
const { argv } = require('node:process');
const num = parseInt(argv[2]);
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < num; x++) {
    console.log('X'.repeat(num));
  }
}
