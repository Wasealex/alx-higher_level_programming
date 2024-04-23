#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const filepath = process.argv[3];
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(filepath, body, 'utf-8', (error) => {
      if (error) {
        console.error(error);
      }
    });
  }
});
