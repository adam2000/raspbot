$(document).ready(function() {
    $('a').bind('click', function(e) {
        var url = $(this).attr('href');
        $.get(url);
        return false;
    });
    /*$('#set').bind('click', function(e) {
        var speed = $('#speed').val();
        $.get('/engines/speed=' + speed);
    });*/
    $('#slider').slider({
        step: 32,
        max: 1024,
        min: 512,
        
        change: function (e, ui) {
        var speed = ui.value;
        //$('#speed').val(speed);
        $.get('/engines/speed=' + speed);
        }
    });
    if ($(window).width() < $(window).height()) {
        $('#direction').width($(window).width());
        $('#direction').height($(window).width());
    }
});
