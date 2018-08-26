var TimerId = setInterval(function() {
    $(".event-img").css("height", $(".event-img").width()*10/16*1.2+"px")
    $(".img-resp").css("height", $(".img-resp").width()*9/16+"px")
}, 100)