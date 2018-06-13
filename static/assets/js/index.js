function allowDrop(ev) {
    ev.preventDefault();
}

var srcdiv = null;

function drag(ev, divdom) {
    srcdiv = divdom;
    ev.dataTransfer.setData("text/html", divdom.innerHTML);
    var index=$(".curriculum div").index(divdom);
    alert(index);
}

function drop(ev, divdom) {
    ev.preventDefault();
    if (srcdiv != divdom) {
        srcdiv.innerHTML = divdom.innerHTML;
        divdom.innerHTML = ev.dataTransfer.getData("text/html");
    }
}

$(".curriculum div").each(function(index,e){
    $(this).html(index);
    $(this).offset({top:Math.floor(index/7)*60+50,left:index%7*85+200});
})