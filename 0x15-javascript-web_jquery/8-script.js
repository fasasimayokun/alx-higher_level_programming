// a JavaScript script that fetches and lists the title for all movies by
// using this URL: https://swapi-api.alx-tools.com/api/films/?format=json
let url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, function (data) {
  let movies = data.results;
  for (let movie of movies) {
    $('UL#list_movies').append(`<li>${movie.title}<\li>`);
  }
});
