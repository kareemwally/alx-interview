#!/usr/bin/node
const request = require('request');
const util = require('util');
const requestGet = util.promisify(request.get);

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

async function getCharacterNames () {
  try {
    const response = await requestGet(url);
    if (response.statusCode !== 200) {
      throw new Error(`Failed to fetch movie data: ${response.statusCode}`);
    }

    const characters = JSON.parse(response.body).characters;

    for (const character of characters) {
      const characterResponse = await requestGet(character);
      if (characterResponse.statusCode !== 200) {
        throw new Error(`Failed to fetch character data: ${characterResponse.statusCode}`);
      }
      const characterName = JSON.parse(characterResponse.body).name;
      console.log(characterName);
    }
  } catch (error) {
    console.error(error);
  }
}

getCharacterNames();
