$("#navAdd1").css("width", $("#logo").width()+150+30+"px")
$("#navAdd2").css("width", $("#logo").width()+300+30+"px")
$("#navAdd3").css("width", $("#logo").width()+450+30+"px")
$("#navAdd1").css("left", -$("#logo").width()-30+"px")
$("#navAdd2").css("left", -$("#logo").width()-30+"px")
$("#navAdd3").css("left", -$("#logo").width()-30+"px")


var TimerId = setInterval(function() {
    $(".header").css("width", $("BODY").width()+"px")
    $(".header").css("height", "768px")
    $(".header").css("transform", "translate("+"-"+($("BODY").width()/12+2)+"px"+", -128px)")
    //$(".header > img").css("width", $("BODY").width()*0.7+"px")
    $(".header-divide").css("width", $("BODY").width()*0.4+"px")
    if (window.innerWidth > 768) {
        $("#nav-avatar").css("width", "10%")
    } else {
        $("#nav-avatar").css("width", "100%")
        $("#nav-avatar > .nav-link").css("height", "50px;")
        $("#nav-avatar > .nav-link > .nav-profile-img").css("height", "50px;")
        $("#nav-avatar > .nav-link > .nav-profile-img").css("width", "50px;")
    }
}, 100)

var TimerId1 = setInterval(function() {
    $(".stairs-update-user").css("left", "-"+($("BODY").width()/12+2)+"px")
    $(".stairs-update-user").css("width", $("BODY").width()+"px")
    $("#stair-updusr2").css("height", parseFloat($("#stair-updusr1").css("top"))-parseFloat($("#stair-updusr2").css("top"))+150+"px")
}, 100)
