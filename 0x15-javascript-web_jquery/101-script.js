$(function () {
  $('#add_item').bind('click', function () {
    $('.my_list').append('<li>Item</li>');
  });
  $('#remove_item').bind('click', function () {
    $('.my_list :last').remove();
  });
  $('#clear_list').bind('click', function () {
    $('.my_list').empty();
  });
});
