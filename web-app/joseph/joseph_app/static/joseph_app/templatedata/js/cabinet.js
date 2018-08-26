var TimerId1 = setInterval(function() {
    $(".stairs-cabinet").css("left", "-"+($("BODY").width()/12+2)+"px")
    $(".stairs-cabinet").css("width", $("BODY").width()+"px")
    $("#stair-cab1").css("left", $("#email_cab").offset().left-$(".frame").offset().left-8+"px")
    if ($("#persData").css("display") == "block") {
        $("#stair-cab1").css("width", $("#persData").offset().left-$("#email_cab").offset().left+"px")
        $("#stair-cab1").css("height", $("#saveButton").offset().top-$("#email_cab").offset().top+"px")
    } else {
        if ($("#avatarData").parent().css("display") == "block"){
            $("#stair-cab1").css("width", $("#avatarData").offset().left-$("#email_cab").offset().left+"px")
            $("#stair-cab1").css("height", $("#saveButton").offset().top-$("#email_cab").offset().top+"px")
        } else {
            $("#stair-cab1").css("width", $("BODY").width()-($("#email_cab").offset().left-8)*2+"px")
            $("#stair-cab1").css("height", $("#saveButton").offset().top-$("#email_cab").offset().top+$("#email_cab").height()*1.5+"px")
            $("#ev-create").addClass("border-0")
        }
    }
    $("#avatarData").css("height", $("#avatarData").outerWidth()+"px")
    $("#avatarData > .cab-avatar").css("height", $("#avatarData").width()+"px")
    $("#stair-cab2").css("top", $("#avatarData").offset().top-$(".frame-border").offset().top+"px")
    $("#stair-cab3").css("top", $("#h4-event-header").offset().top-$(".frame-border").offset().top-5+"px")
    $("#stair-cab3-r").css("top", $("#h4-event-header").offset().top-$(".frame-border").offset().top-5+"px")
    if ($("#h4-stat-header").offset()) {
        $("#stair-cab4").css("top", $("#h4-stat-header").offset().top-$(".frame-border").offset().top-5+"px")
        $("#stair-cab4-r").css("top", $("#h4-stat-header").offset().top-$(".frame-border").offset().top-5+"px")
    } else {
        $("#stair-cab4").css("top", $("#h4-admin-header").offset().top-$(".frame-border").offset().top-5+"px")
        $("#stair-cab4-r").css("top", $("#h4-admin-header").offset().top-$(".frame-border").offset().top-5+"px")
    }
    $("#stair-cab5").css("top", $("#passwordChangeButton").offset().top+$("#passwordChangeButton").outerHeight()-$(".frame-border").offset().top+10+"px")
    $("#stair-cab6").css("top", $("#passwordChangeButton").offset().top-$(".frame-border").offset().top+"px")
    if ($("#article-create-h5").offset()) {
        $("#stair-cab9").css("top", $("#article-create-h5").offset().top-$(".frame-border").offset().top+"px")
        $("#stair-cab10").css("top", $("#event-create-h5").offset().top-$(".frame-border").offset().top+"px")
        $("#stair-cab11").css("top", $("#poll-create-h5").offset().top-$(".frame-border").offset().top+"px")
    }
    $("#stair-cab7").css("height", $("#stair-cab6").offset().top-$("#stair-cab7").offset().top+"px")
    $(".event-img").css("height", $(".event-img").width()*10/16*1.2+"px")
    $(".img-resp").css("height", $(".img-resp").width()*9/16+"px")
    $(".qr").css("width", screen.availWidth+"px")
    $(".qr").css("height", screen.availHeight+"px")
    if (screen.availWidth > screen.availHeight) {
        $(".qr > div").css("height", screen.availHeight*0.8+"px")
        $(".qr > div").css("width", $(".qr > div").css("height"))
    } else {
        $(".qr > div").css("width", screen.availWidth*0.8+"px")
        $(".qr > div").css("height", $(".qr > div").css("width"))
    }
    if ($("#collapsePersData").hasClass("show")) {
        $("#pers-close").removeClass("d-none")
        $("#pers-open").addClass("d-none")
    } else {
        $("#pers-close").addClass("d-none")
        $("#pers-open").removeClass("d-none")
    }
}, 100)

//TimerId1()
//
//$(function() {
//    $(window).resize(TimerId1)
//})
//
//var Timer = setInterval(function() {
//    if ($("#persData").css("display") == "block") {
//        $("#stair-cab1").css("width", $("#persData").offset().left-$("#email_cab").offset().left+"px")
//        $("#stair-cab1").css("height", $("#saveButton").offset().top-$("#email_cab").offset().top+"px")
//    } else {
//        if ($("#avatarData").parent().css("display") == "block"){
//            $("#stair-cab1").css("width", $("#avatarData").offset().left-$("#email_cab").offset().left+"px")
//            $("#stair-cab1").css("height", $("#saveButton").offset().top-$("#email_cab").offset().top+"px")
//        } else {
//            $("#stair-cab1").css("width", $("BODY").width()-($("#email_cab").offset().left-8)*2+"px")
//            $("#stair-cab1").css("height", $("#saveButton").offset().top-$("#email_cab").offset().top+$("#email_cab").height()*1.5+"px")
//            $("#ev-create").addClass("border-0")
//        }
//    }
//    $("#stair-cab2").css("top", $("#avatarData").offset().top-$(".frame-border").offset().top+"px")
//    $("#stair-cab3").css("top", $("#h4-event-header").offset().top-$(".frame-border").offset().top-5+"px")
//    $("#stair-cab3-r").css("top", $("#h4-event-header").offset().top-$(".frame-border").offset().top-5+"px")
//    if ($("#h4-stat-header").offset()) {
//        $("#stair-cab4").css("top", $("#h4-stat-header").offset().top-$(".frame-border").offset().top-5+"px")
//        $("#stair-cab4-r").css("top", $("#h4-stat-header").offset().top-$(".frame-border").offset().top-5+"px")
//    } else {
//        $("#stair-cab4").css("top", $("#h4-admin-header").offset().top-$(".frame-border").offset().top-5+"px")
//        $("#stair-cab4-r").css("top", $("#h4-admin-header").offset().top-$(".frame-border").offset().top-5+"px")
//    }
//    $("#stair-cab5").css("top", $("#passwordChangeButton").offset().top+$("#passwordChangeButton").outerHeight()-$(".frame-border").offset().top+10+"px")
//    $("#stair-cab6").css("top", $("#passwordChangeButton").offset().top-$(".frame-border").offset().top+"px")
//    $("#stair-cab9").css("top", $("#article-create-h5").offset().top-$(".frame-border").offset().top+"px")
//    $("#stair-cab10").css("top", $("#event-create-h5").offset().top-$(".frame-border").offset().top+"px")
//    $("#stair-cab11").css("top", $("#poll-create-h5").offset().top-$(".frame-border").offset().top+"px")
//    $("#stair-cab7").css("height", $("#stair-cab6").offset().top-$("#stair-cab7").offset().top+"px")
//}, 100)


function add_article_image(article_image_count) {
    $("<div>", {
        class : "custom-file mb-1",
        id : "article_image_el"+article_image_count,
    }).insertAfter($("#article_image_el"+(article_image_count-1)))
    $("<input>", {
        type : "file",
        class : "custom-file-input", 
        name : "article_image"+article_image_count, 
        id : "article_image"+article_image_count
    }).appendTo($("#article_image_el"+(article_image_count)))
    $("<label>", {
        class : "custom-file-label", 
        for : "article_image"+article_image_count
    }).appendTo($("#article_image_el"+(article_image_count)))
    $("#article_image_el"+(article_image_count)+" > label").append("Файл")
    if (article_image_count >= 10) {
        $("#add_ar_img_field").addClass("d-none")
    }
    $("#add_ar_img_field").attr("onclick", "add_article_image("+(article_image_count+1)+")")
}


function add_poll_choice(poll_choice_count) {
    $(".input-group.mt-1").last().clone().insertAfter($(".input-group.mt-1").last())
    $(".input-group.mt-1").last().children(".input-group-prepend").children(".input-group-text").attr("id", "poll_ch"+poll_choice_count)
    $(".input-group.mt-1").last().children(".input-group-prepend").children(".input-group-text").text(poll_choice_count)
    $(".input-group.mt-1").last().children("input").attr("id", "poll"+poll_choice_count)
    $(".input-group.mt-1").last().children("input").attr("name", "poll"+poll_choice_count)
    $(".input-group.mt-1").last().children("input").attr("aria-describedby", "poll_ch"+poll_choice_count)
    if (poll_choice_count >= 10) {
        $("#add_pc_field").addClass("d-none")
    }
    $("#add_pc_field").attr("onclick", "add_poll_choice("+(poll_choice_count+1)+")")
}

function show_qr(event_pk) {
    $("#qr-"+event_pk).removeClass("d-none")
}

function hide_qr(event_pk) {
    $("#qr-"+event_pk).addClass("d-none")
}