$(document).ready(function() {
    $.ajax({
        url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
        method: 'GET',
        success: function(data) {
            $('#hello').text(data.hello);
        },
        error: function() {
            console.error('Failed to fetch translation');
        }
    });
});