const URL = 'https://hellosalut.stefanbohacek.dev/?lang=fr'
$('document').ready(function () {
  $.get(URL, function (data) {
    $('DIV#hello').text(data.hello);
  });
});
