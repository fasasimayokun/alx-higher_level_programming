// a JavaScript script that fetches and prints how to say “Hello”
// depending on the language You must use the JQuery API
$('document').ready(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/hello/';
  $('INPUT#btn_translate').click(function () {
    $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
      $('DIV#hello').html(data.hello);
    });
  });
});
