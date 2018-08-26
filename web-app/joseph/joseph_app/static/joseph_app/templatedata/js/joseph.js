$("#navAdd1").css("width", $("#logo").width()+150+30+"px")
$("#navAdd2").css("width", $("#logo").width()+300+30+"px")
$("#navAdd3").css("width", $("#logo").width()+450+30+"px")
$("#navAdd1").css("left", -$("#logo").width()-30+"px")
$("#navAdd2").css("left", -$("#logo").width()-30+"px")
$("#navAdd3").css("left", -$("#logo").width()-30+"px")

$("#parallax1").css("height", $(".footer").offset().top*0.9+"px")
$("#parallax2").css("height", $(".footer").offset().top*0.5+"px")
$("#parallax3").css("height", $(".footer").offset().top*0.2+"px")
$("#parallax1").css("top", $(".footer").offset().top*0.05+"px")
$("#parallax2").css("top", $(".footer").offset().top*0.25+"px")
$("#parallax3").css("top", $(".footer").offset().top*0.4+"px")

$(".parallax-piece1").css("height", "350px")
$(".parallax-piece1").css("width", parseFloat($(".parallax-piece1").css("height"))*16/9+"px")
$(".parallax-piece2").css("height", "350px")
$(".parallax-piece2").css("width", parseFloat($(".parallax-piece2").css("height"))*16/9+"px")
$(".parallax-piece3").css("height", "350px")
$(".parallax-piece3").css("width", parseFloat($(".parallax-piece3").css("height"))*16/9+"px")
var pieces1 = []
var pieces2 = []
var pieces3 = []
$(".parallax-piece1").each(function(n,e){
    min = -(e.clientHeight/3)
    max = $("#parallax1").height()/5
    console.log(e.clientHeight/3)
    rand = min+Math.random()*(max-min)
    e.style.top = rand+"px"
    max = ($("#parallax1").width()-e.clientWidth)
    min = -(e.clientWidth/3)
    rand = min+Math.random()*(max-min)
    e.style.left = rand+"px"
    pieces1[n] = e.style.top
})
$(".parallax-piece2").each(function(n,e){
    min = -(e.clientHeight/3)
    max = $("#parallax2").height()/3
    console.log(e.clientHeight/3)
    rand = min+Math.random()*(max-min)
    e.style.top = rand+"px"
    max = ($("#parallax2").width()-e.clientWidth)
    min = -(e.clientWidth/3)
    rand = min+Math.random()*(max-min)
    e.style.left = rand+"px"
    pieces2[n] = e.style.top
})
$(".parallax-piece3").each(function(n,e){
    min = -(e.clientHeight/3)
    max = $("#parallax3").height()/2
    console.log(e.clientHeight/3)
    rand = min+Math.random()*(max-min)
    e.style.top = rand+"px"
    max = ($("#parallax3").width()-e.clientWidth)
    min = -(e.clientWidth/3)
    rand = min+Math.random()*(max-min)
    e.style.left = rand+"px"
    pieces3[n] = e.style.top
})

var TimerId = function() {//setInterval(function() {
    $(".header").css("width", $("BODY").width()+"px")
    $(".header").css("height", "768px")
    $(".header").css("transform", "translate("+"-"+($("BODY").width()/12+2)+"px"+", -128px)")
    //$(".header > img").css("width", $("BODY").width()*0.7+"px")
    $(".header-divide").css("width", $("BODY").width()*0.4+"px")
    if (window.innerWidth > 768) {
        $("#nav-avatar").css("width", "10%")
        $(".header-text").removeClass("header-text-resp")
    } else {
        $("#nav-avatar").css("width", "100%")
        $("#nav-avatar > .nav-link").css("height", "50px;")
        $("#nav-avatar > .nav-link > .nav-profile-img").css("height", "50px;")
        $("#nav-avatar > .nav-link > .nav-profile-img").css("width", "50px;")
        $(".header-text").addClass("header-text-resp")
    }
    $(".background-parallax").css("height", $(".footer").offset().top+"px")
    $("#parallax1").css("height", $(".footer").offset().top*0.9+"px")
    $("#parallax2").css("height", $(".footer").offset().top*0.5+"px")
    $("#parallax3").css("height", $(".footer").offset().top*0.2+"px")
    $("#parallax1").css("top", $(".footer").offset().top*0.05+"px")
    $("#parallax2").css("top", $(".footer").offset().top*0.25+"px")
    $("#parallax3").css("top", $(".footer").offset().top*0.4+"px")
    if ($(window).height() > ($('.background-parallax').height()+ $('.footer').height()+60))
		{$('.footer').addClass('fixed')} else {$('.footer').removeClass('fixed')};
}//, 100)

TimerId()

$(function() {
    $(window).resize(TimerId)
})

$(document).on({scroll:function() {
    $(".parallax-piece1").each(function(n,e){
        e.style.top = parseFloat(pieces1[n])+document.documentElement.scrollTop*0.8+"px"
    })
    $(".parallax-piece2").each(function(n,e){
        e.style.top = parseFloat(pieces2[n])+document.documentElement.scrollTop*0.45+"px"
    })
    $(".parallax-piece3").each(function(n,e){
        e.style.top = parseFloat(pieces3[n])+document.documentElement.scrollTop*0.2+"px"
    })
}})
