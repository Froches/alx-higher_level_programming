$(document).ready(function() {
    $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
        var movies = data.results;
        var ul = $('#list_movies');
        $.each(movies, function(i, movie) {
            ul.append($('<li>').text(movie.title));
        });
    });
 }); 