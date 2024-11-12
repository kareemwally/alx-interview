#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
request.get(url, (error, response) => {
  if (error) {
    console.log(error);
    console.log(response.statusCode);
  }
  if (!error && response.statusCode === 200) {
    const characters = JSON.parse(response.body).characters;
    for (const character of characters) {
      request.get(character, (error, response) => {
        if (error) { console.log(error); }
        if (!error && response.statusCode === 200) {
          console.log(JSON.parse(response.body).name);
        }
      });
    }
  }
});
