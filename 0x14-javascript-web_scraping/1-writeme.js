#!/usr/bin/node

const fs = require('fs');
const filepath = process.argv[2];
const message = process.argv[3];

fs.writeFile(filepath, message, 'utf-8', (err) => {
  if (err) {
    console.error();
  }
});
