const URL = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
fetch(URL).then(function (response) {
  return response.json();
}).then(function (myJson) {
  $('#character').html(myJson.name);
});
