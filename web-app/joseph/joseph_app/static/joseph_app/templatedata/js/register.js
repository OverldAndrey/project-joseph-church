var TimerId1 = setInterval(function() {
    $(".stairs-register").css("left", "-"+($("BODY").width()/12+2)+"px")
    $(".stairs-register").css("width", $("BODY").width()+"px")
    $("#stair-reg4").css("height", parseFloat($("#stair-reg2").css("top"))+parseFloat($("#stair-reg2").css("height"))-parseFloat($("#stair-reg4").css("top"))+90+"px")
    if (window.innerWidth > 992) {
        $("#stair-reg8").css("height", $("#avatar").offset().top-$("#email_new").offset().top+"px")
    } else {
        $("#stair-reg8").css("height", $("#avatar").offset().top-$("#email_new").offset().top+10+"px")
        $("#stair-reg8").css("left", ($("#reg-form").offset().left+$("#email_new").offset().left)/2+1+"px")
        $("#stair-reg8").css("width", ($("#reg-form").outerWidth()+$("#email_new").outerWidth())/2+1+"px")
    }
}, 100)