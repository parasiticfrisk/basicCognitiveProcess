$(document).ready(function () {
    $('body').removeClass('preload'); // fix for animation movement on page load
});

let resizeTimer;
window.addEventListener("resize", () => {
    document.body.classList.add("resize-animation-stopper");
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(() => {
        document.body.classList.remove("resize-animation-stopper");
    }, 400);
});

// fix for mobile: 
document.addEventListener("touchstart", function () { }, true); // This snippet will enable hover effects for touchscreens

// code for input mask on phone number
// fix for tel keypad missing dashes on mobile device, this will automatically add them
$('input[type="tel"]#phone').keyup(function (event) {
    var t = event.target, v = t.value;
    if (v.length == 3) { t.value = v + '-'; }
    if (v.length == 7) { t.value = v + '-'; }
});