#!/usr/bin/node

const request = require('request');
const star_uri = process.argv[2]
let cnt = 0;

request.get(star_uri, function (__err, __res, body) {
  body = JSON.parse(body).results;
  body.forEach(film => {
    const characters = film.characters.map(character => character.split('/')[5]);
    if (characters.includes('18')) {
      cnt++;
    }
  });
  console.log(cnt);
});
