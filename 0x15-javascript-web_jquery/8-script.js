const URL = 'https://swapi-api.hbtn.io/api/films/?format=json';

fetch(URL).then(function (response) {
  return response.json();
}).then(function (myJson) {
  const list = $('#list_movies');
  for (const title of myJson.results) {
    list.append('<li>' + title.title + '</li>');
  }
});
