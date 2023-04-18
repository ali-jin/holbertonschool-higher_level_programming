#!/usr/bin/node
const process = require('process');
const request = require('request');
const args = process.argv;
request(args[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const usesrTasks = {};
    const users = JSON.parse(body);
    for (const task of users) {
      if (task.completed === true) {
        if (task.userId in usesrTasks) {
          usesrTasks[task.userId]++;
        } else {
          usesrTasks[task.userId] = 1;
        }
      }
    }
    console.log(usesrTasks);
  }
});
