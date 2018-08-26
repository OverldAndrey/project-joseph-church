var TimerId = setInterval(function() {
    $(".doc > .docs-back").css("left", (-$(".frame-border").offset().left)-20+"px")
    $(".doc > .docs-back").css("width", $(".doc").width()+$(".frame-border").offset().left+"px")
    $(".frame-part").css("width", parseFloat($(".frame-border").css("border-width"))+4+"px")
}, 100)