#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  todos = JSON.parse(body);
  usersStats = {}
  for (task of todos) {
    if (!(task.userId in usersStats) && task.completed) {
      usersStats[task.userId] = 1;
    }
    else if (task.completed) {
      usersStats[task.userId] += 1;
    }
  }

  console.log(usersStats);
});
