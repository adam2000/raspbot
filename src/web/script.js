var title = '';
var artist = '';
var album = '';
var oldtitle = '';
var oldartist = '';
var oldalbum = '';
var artistimages = [];
var artistimagesi = 0;
var timeout;
$(document).ready(function() {
    $('#song').offset({ top: $('#song').offset.top, left: $('#art').height()*1.09 + 20});
    $(window).bind('resize', function() {
        if ($('#art').attr("src") == "arts/art.png") {
            $('#song').offset({ top: $('#song').offset.top, left: $('#art').height()*1.09 + 20});
        } else {
            $('#song').offset({ top: $('#song').offset.top, left: $('#art').height() + 20});
        }
    });
    $(window).bind('keydown', function(e) {
        if (e.keyCode == 0 || e.keyCode == 32) { // `0` works in mozilla and `320 in other`
            $.get('http://192.168.1.14:90/cmd/toggle');
            return false;
        } else if (e.keyCode == 37) {
            $.get('http://192.168.1.14:90/cmd/previous');
            return false;
        } else if (e.keyCode == 39) {
            $.get('http://192.168.1.14:90/cmd/next');
            return false;
        }
        return true;
    });
    update();
    setInterval ("update()", 1000);
});
function changeimage() {
    if (artistimages.length > 1) {
        if (artistimagesi + 1 < artistimages.length) {
            artistimagesi = artistimagesi + 1;
            $('#picture').css("background-image", "url(" + artistimages[artistimagesi] + ")");
        } else {
            artistimagesi = 0;
            $('#picture').css("background-image", "url(" + artistimages[0] + ")");
        }
    }
    timeout = setTimeout ("changeimage()", 10000);
}
function slideSwitch() {
    var $active = $('#slideshow DIV.active');

    if ( $active.length == 0 ) $active = $('#slideshow DIV:last');

    var $next =  $active.next().length ? $active.next()
        : $('#slideshow DIV:first');
    if ($next.attr('id') != $active.attr('id')) {
        $active.addClass('last-active');
        $active.animate({opacity: 0.0}, 2000);

        $next.css({opacity: 0.0})
            .addClass('active')
            .animate({opacity: 1.0}, 3000, function() {
                $active.removeClass('active last-active');
            });
        timeout = setTimeout ("slideSwitch()", 20000);
    } else {
        $next.css({opacity: 0.0})
            .addClass('active')
            .animate({opacity: 1.0}, 3000, function() {
                $active.removeClass('active last-active');
            });
    }
}

function update() {
    $.get('info', function(data) {
        var obj = $.parseJSON(data);
        title = obj.current.title;
        artist = obj.current.artist;
        album = obj.current.album;
        if (title != oldtitle) {
            $('#title').text(title);
        }
        if (artist != oldartist) {
            $('#artist').text(artist);
        }
        if (album != oldalbum) {
            $('#album').text(album);
        }
        if (artist != '' && title != '')  {
            if (title != oldtitle || artist != oldartist || album != oldalbum) {
                $('#lyric').fadeOut('fast');
                $.get('lyric', function(data) {
                    $('#lyric').css("top", 10);
                    $('#lyric').html(data + '<br />');
                    $('#lyric').fadeIn('slow');
                    $('#slideshow').width($(window).width() - $('#lyric').width() - $(window).width() * 0.05);
                    $('#song').width($(window).width() - $('#lyric').width() - $('#song').offset.left - $(window).width() * 0.05);
                });
            }
        }
        if (artist != '' && album != '')  {
            if (artist != oldartist || album != oldalbum) {
                $('#art').attr("src","arts/art.png");
                $.get('albumart', function(data) {
                    if (data != '') {
                        $('#art').attr("src", data);
                        $('#song').offset({ top: $('#song').offset.top, left: $('#art').height() + 20});
                    } else {
                        $('#art').attr("src","arts/art.png");
                        $('#song').offset({ top: $('#song').offset.top, left: $('#art').height()*1.09 + 20});
                    }
                });
            }
        }

        if (artist != '')  {
            if (artist != oldartist) {
                $('#slideshow').fadeOut('slow');
                clearTimeout(timeout);
                $.get('artistart', function(data) {
                    if (data != '') {
                        artistimages = data.split(';')
                        $('#slideshow').html('');
                        for (var image in artistimages) {
                            $('#slideshow').html($('#slideshow').html() + '<div id="pic' + image + '"/>');
                        }
                        setTimeout(function(){
                            for (var image in artistimages) {
                                $('#pic' + image).css("background-image", "url(" + artistimages[image] + ")");
                            }
                        }, 1000);
                        slideSwitch();
                        $('#slideshow').fadeIn('slow');
                        //$('#picture').css("background-image", "url(" + artistimages[0] + ")");
                    } else {
                        artistimages = [];
                    }
                });
            }
        }
        oldtitle = title;
        oldartist = artist;
        oldalbum = album;
        if (obj.current.time != '' && obj.status.elapsed != '')  {
            scroll(obj.current.time, obj.status.elapsed);
        }
    });
}
function scroll(total, current) {
    if ($(window).height() < $('#lyric').height()) {
        if (current > total * 0.2 && current < total * 0.8) {
            var percent = (current - (total * 0.2)) / (total * 0.6);
            var length = percent * ($('#lyric').height() - $(document).height());
            $('#lyric').css("top", 10 - length);
        } else if (current > total * 0.8) {
            var length = ($('#lyric').height() - $(document).height());
            $('#lyric').css("top", 10 - length);
        } else if (current < total * 0.2) {
            $('#lyric').css("top", 10);
        }
    }
}
function getflickr(text) {
    var apiKey = '6014d813c67ac1dd67976452253dd5d6';
    var perPage = '3';
    var showOnPage = '6';

    $.getJSON('http://api.flickr.com/services/rest/?format=json&method='+
        'flickr.photos.search&api_key=' + apiKey + '&text=' + text +
        '&per_page=' + perPage + '&jsoncallback=?',
        function(data){
        var classShown = 'class="lightbox"';
        var classHidden = 'class="lightbox hidden"';

        $.each(data.photos.photo, function(i, rPhoto){
            var basePhotoURL = 'http://farm' + rPhoto.farm + '.static.flickr.com/'
                + rPhoto.server + '/' + rPhoto.id + '_' + rPhoto.secret;

            var thumbPhotoURL = basePhotoURL + '_s.jpg';
            var mediumPhotoURL = basePhotoURL + '.jpg';

            var photoStringStart = '<a ';
            var photoStringEnd = 'title="' + rPhoto.title + '" href="'+
                mediumPhotoURL +'"><img src="' + thumbPhotoURL + '"class="flimg" alt="' +
                rPhoto.title + '"/></a>;'
            var photoString = (i < showOnPage) ?
                photoStringStart + classShown + photoStringEnd :
                photoStringStart + classHidden + photoStringEnd;

            $(photoString).appendTo("#flickr");
        });
    });
}
