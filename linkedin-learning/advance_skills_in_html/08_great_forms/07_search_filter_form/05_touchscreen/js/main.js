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