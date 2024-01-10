const list = $('ul#list_movies');
$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  method: 'GET',
  success: function (films) {
    films.results.forEach((film) => {
      list.append('<li>' + film.title + '</li>');
    });
  }
});
