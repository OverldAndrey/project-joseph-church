var TimerId = setInterval(function() {
    $(".carousel").css("min-height", $(".carousel").width()*9/16+"px")
    $(".art-img > div").css("min-height", $(".carousel").width()*9/16+"px")
}, 100)