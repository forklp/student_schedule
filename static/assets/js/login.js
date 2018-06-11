$(".login").hide();

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