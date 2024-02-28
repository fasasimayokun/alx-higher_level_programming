// a JavaScript script that fetches the character name from this
// URL: https://swapi-api.alx-tools.com/api/people/5/?format=json using jquery
let url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.get(url, function (data) {
  $('DIV#character').text(data.name);
});
