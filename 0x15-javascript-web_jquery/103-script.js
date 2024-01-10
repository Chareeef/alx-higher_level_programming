$(function () {
  $('input#language_code').keypress(function (event) {
    if (event.which === 13) {
      const langCode = $('input#language_code').val();
      $.ajax({
        url: 'https://hellosalut.stefanbohacek.dev/?lang=' + langCode,
        method: 'GET',
        success: function (data) {
          $('div#hello').text(data.hello);
        }
      });
    }
  });

  $('input#btn_translate').bind('click', function () {
    const langCode = $('input#language_code').val();
    $.ajax({
      url: 'https://hellosalut.stefanbohacek.dev/?lang=' + langCode,
      method: 'GET',
      success: function (data) {
        $('div#hello').text(data.hello);
      }
    });
  });
});
