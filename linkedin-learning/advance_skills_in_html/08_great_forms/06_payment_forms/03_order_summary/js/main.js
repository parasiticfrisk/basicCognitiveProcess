// This adds the ability to add more of the same item or remove items. 
$(document).ready(function () {

    var $input = $("#amt");

    $input.val(1); // get value of #amt

    $(".btn").click(function () {
        if ($(this).hasClass('add'))
            $input.val(parseInt($input.val()) + 1);
        else if ($input.val() >= 1)
            $input.val(parseInt($input.val()) - 1);
    });
});