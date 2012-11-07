$(document).ready(function() {
    $('a').bind('click', function(e) {
        var url = $(this).attr('href');
        $.get(url);
        return false;
    });
    $('#set').bind('click', function(e) {
        var speed = $('#speed').val();
        $.get('/engines/speed=' + speed);
    });
    $('#slider').slider({
        step: 64,
        max: 1024,
        min: 0
    });
    $('#slider').changed(function(e, ui) {
        var speed = ui.value;
        $('#speed').val(speed);
        $.get('/engines/speed=' + speed);
    });
});
