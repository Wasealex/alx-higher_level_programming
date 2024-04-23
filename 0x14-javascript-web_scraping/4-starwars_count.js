#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const characterID = 18;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    if (response.statusCode === 200) {
      const films = JSON.parse(body).results;
      let count = 0;

      films.forEach((film) => {
        const characters = film.characters;
        characters.forEach((character) => {
          if (character.includes(`/${characterID}/`)) {
            count++;
          }
        });
      });
      console.log(`${count}`);
    } else {
      console.log('not found');
    }
  }
});
