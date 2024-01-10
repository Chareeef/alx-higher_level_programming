$(function () {
  $('input#btn_translate').bind('click', function () {
    const lang_code = $('input#language_code').val();
    $.ajax({
      url: 'https://hellosalut.stefanbohacek.dev/?lang=' + lang_code,
      method: 'GET',
      success: function (data) {
        $('div#hello').text(data.hello);
      }
    });
  });
});
