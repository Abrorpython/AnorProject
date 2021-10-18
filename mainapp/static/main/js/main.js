$(".confirm").on("click",function (e) {
    if(confirm("O'chirishni xoxlaysizmi?")){
        return true;
    }
    e.preventDefault();
    return false
});