// a JavaScript script that adds, removes and clears LI elements from a list
// when the user clicks You must use the JQuery API
$('document').ready(function () {
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Items</li>');
  });
  $('DIV#remove_item').click(function () {
    $('UL.my_list li:last').remove();
  });
  $('DIV#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});
