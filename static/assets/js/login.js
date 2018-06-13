$(".login").hide();
if ($(".notice").text()==""){
    $(".notice").hide();
    $(".close").hide();
}
$(".close").click(function(){
    $(".notice").hide();
    $(".close").hide();
})
$(".selector_son").click(function(){
    $(".selector_son").removeClass("selector_active");
    $(this).addClass("selector_active");
    if ($(this).text()=="登录"){
        $(".login").show();
        $(".register").hide();
    }
    else{
        $(".login").hide();
        $(".register").show();
    }
})