#!/usr/bin/node
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.get(url, function (data) {
  const movies = data.results;
  for (const movie of movies) {
    $('#list_movies').append('<li>' + movie.title + '</li>');
  }
});
