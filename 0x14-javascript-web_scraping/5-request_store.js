#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const path = process.argv[3];
const fs = require('fs');

request.get(url, 'utf8', function (__err, __res, body) {
  fs.writeFile(path, body, 'utf8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});
