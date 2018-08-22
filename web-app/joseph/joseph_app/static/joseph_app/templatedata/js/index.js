var TimerId = setInterval(function() {
    windowHeight = window.innerHeight
    $(".index-top").css("min-height", windowHeight+"px")
    $(".index-news").css("margin-top", windowHeight+"px")
    $(".index-news").css("min-height", windowHeight+"px")
    $(".index-events").css("margin-top", windowHeight+"px")
    $(".index-events").css("min-height", windowHeight+"px")
    $(".index-footer").css("margin-top", windowHeight+"px")
    $(".index-footer").css("min-height", windowHeight+"px")
    $(".frame").css("height", $(".index-news").height()+"px")
    if (window.innerWidth > 768) {
        $("#index-login").css("margin-top", windowHeight/5+"px")
        $("#index-cab").css("margin-top", windowHeight/5+"px")
        $(".art-img").css("height", $(".frame").height()-$("#news-title").outerHeight(true)+"px")
    } else {
        $(".car-content").css("height", ($(".frame").height()-$("#news-title").outerHeight(true))*0.65+"px")
        $(".art-img").css("height", $(".frame").height()-$(".car-content").outerHeight(true)-$("#news-title").outerHeight(true)+"px")
    }
    $("#index-arrows").css("height", windowHeight/10+"px")
    $(".index-news-stairs").css("margin-top", windowHeight*2+"px")
    $(".index-events-stairs").css("margin-top", windowHeight*4+"px")
},100)

$("#iarrow1").css("opacity", 1)
setTimeout(function(){
    $("#iarrow2").css("opacity", 1)
    $("#iarrow1").css("opacity", 0)
    setTimeout(function(){
        $("#iarrow3").css("opacity", 1)
        $("#iarrow2").css("opacity", 0)
        setTimeout(function(){
            $("#iarrow4").css("opacity", 1)
            $("#iarrow3").css("opacity", 0)
            setTimeout(function(){
                $("#iarrow5").css("opacity", 1)
            }, 200)
        }, 200)
    }, 200)
}, 200)



