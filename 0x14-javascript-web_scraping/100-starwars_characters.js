#!/usr/bin/node

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]), function (__err, __res, body) {
  const characters = JSON.parse(body).characters;
  for (let i = 0; i < characters.length; i++) {
    request(characters[i], function (__Err, __Res, Body) {
      console.log(JSON.parse(Body).name);
    });
  }
});
