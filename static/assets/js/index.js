function allowDrop(ev) {
    ev.preventDefault();
}

var srcdiv = null;
var index, x, y;
function drag(ev, divdom) {
    srcdiv = divdom;
    ev.dataTransfer.setData("text/html", divdom.innerHTML);
}

function heightX(x) {
    return x * 60 - 10;
}

function indexX(h) {
    return (h + 10) / 60;
}

function drop(ev, divdom) {
    ev.preventDefault();
    x = parseInt($(divdom).css("height"));
    y = parseInt($(srcdiv).css("height"));
    var index1 = $(".curriculum div").index(divdom);
    var index2 = $(".curriculum div").index(srcdiv);
    if (index2 + indexX(x) * 7 - 7 > 27)
        return;
    if (index1 + indexX(y) * 7 - 7 > 27)
        return;
    for (i = indexX(x); i + 1 <= indexX(y); i++) {
        if (parseInt($(".curriculum div").eq(index1 + i * 7).css("height")) > 50)
            return;
    }
    for (i = indexX(y); i + 1 <= indexX(x); i++) {
        if (parseInt($(".curriculum div").eq(index2 + i * 7).css("height")) > 50)
            return;
    }
    for (i = indexX(x); i + 1 <= indexX(y); i++) {
        $(".curriculum div").eq(index1 + i * 7).hide();
        $(".curriculum div").eq(index2 + i * 7).show();
        $(".curriculum div").eq(index2 + i * 7).css("height", "50px");
    }
    for (i = indexX(y); i + 1 <= indexX(x); i++) {
        $(".curriculum div").eq(index2 + i * 7).hide();
        $(".curriculum div").eq(index1 + i * 7).show();
        $(".curriculum div").eq(index1 + i * 7).css("height", "50px");
    }
    if (srcdiv != divdom) {
        $(divdom).css("height", y);
        $(srcdiv).css("height", x);
        srcdiv.innerHTML = divdom.innerHTML;
        divdom.innerHTML = ev.dataTransfer.getData("text/html");
    }
}

$(".curriculum div").each(function (index, e) {
    $(this).html(index);
    $(this).offset({ top: Math.floor(index / 7) * 60 + 50, left: index % 7 * 85 + 200 });
})
$(".curriculum div").each(function (index, e) {
    if ($(this).css("height") == "40px")
        $(this).hide();
})
