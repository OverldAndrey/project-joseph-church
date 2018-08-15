var TimerId1 = setInterval(function() {
    $(".stairs-update-user").css("left", "-"+($("BODY").width()/12+2)+"px")
    $(".stairs-update-user").css("width", $("BODY").width()+"px")
    $("#stair-updusr2").css("height", parseFloat($("#stair-updusr1").css("top"))-parseFloat($("#stair-updusr2").css("top"))+150+"px")
}, 100)