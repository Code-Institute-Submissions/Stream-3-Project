// FLIP CARDS ON products.html PAGE

// when the mouse enters the div flip 180degs
$(".flip").mouseenter(function(event) {
    // get the browser type 
    var ua = window.navigator.userAgent;
    // checks if the browser is Internet Explorer 
    var browser_ie = /MSIE|Trident/.test(ua);
  
    // if it is not Internet Explorer add the mousein class
    if (!browser_ie){
        $(this).addClass("mousein");
    }
});

// when the mouse exits the card flip back to 0
$(".flip").mouseleave(function(event) {
       $(this).removeClass("mousein");
});

