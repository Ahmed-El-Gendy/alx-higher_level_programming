#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (__err, res) {
  console.log('code:', res.statusCode);
});
