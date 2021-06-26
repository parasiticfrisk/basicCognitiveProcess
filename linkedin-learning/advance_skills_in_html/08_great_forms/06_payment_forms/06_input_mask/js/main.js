$(document).ready(function () {

    var $input = $("#amt");

    $input.val(1);

    $(".btn").click(function () {
        if ($(this).hasClass('add'))
            $input.val(parseInt($input.val()) + 1);
        else if ($input.val() >= 1)
            $input.val(parseInt($input.val()) - 1);
    });

    // toggle the order summary on personal detail page to show/hide
    $(".showHideOrdSum").click(function () {
        $("#orderSummary").toggle();

        var $this = $(this).toggleClass('showhide');
        if ($(this).hasClass('showhide')) {
            $(this).html('<i class="fas fa-shopping-cart"></i> Hide order summary <i class="fas fa-sort-up"></i>');

        } else {
            $(this).html('<i class="fas fa-shopping-cart"></i> Show order summary <i class="fas fa-sort-down"></i>');
        }
    });
});

// Input mask for phone number 
//    /pattern/modifiers;
document.getElementById('phone').addEventListener('input', function (e) {
    var x = e.target.value.replace(/\D/g, '').match(/(\d{0,3})(\d{0,3})(\d{0,4})/);
    e.target.value = !x[2] ? x[1] : '(' + x[1] + ') ' + x[2] + (x[3] ? '-' + x[3] : '');
});