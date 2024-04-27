#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, function (err, __res, body) {
  if (err) {
    console.log(err);
  } else {
    const todos = JSON.parse(body);
    const completedTask = {};

    todos.forEach(todo => {
      if (todo.completed) {
        if (completedTask[todo.userId]) {
          completedTask[todo.userId]++;
        } else {
          completedTask[todo.userId] = 1;
        }
      }
    });

    console.log(completedTask);
  }
});
