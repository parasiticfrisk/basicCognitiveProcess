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


    // ZIP CODE 
    function is_int(value) {
        if ((parseFloat(value) == parseInt(value)) && !isNaN(value)) {
            return true;
        } else {
            return false;
        }
    }

    $("#zip").keyup(function () {
        var el = $(this);

        // Did they type five integers?
        if ((el.val().length == 5) && (is_int(el.val()))) {

            // Call Ziptastic for information
            $.ajax({
                url: "https://zip.getziptastic.com/v2/US/" + el.val(),
                cache: false,
                dataType: "json",
                type: "GET",
                success: function (result, success) {

                    // Fill in the city / state data  
                    $("#city").val(result.city);
                    $("#state").val(result.state);

                    $("#zip").blur();
                    $("#address-line-1").show().focus();
                },

                error: function (result, success) {

                    $(".zip-error").fadeIn(300);
                }
            });
        } else if (el.val().length < 5) {

            $(".zip-error").fadeOut(200);
        };
    });

    // update shipping amount based on radio button selection
    $('input[type=radio]').on('change', function () {
        var setValue = $("input[type='radio']:checked").val();
        $('.shipValue').text(setValue);
        var newTot = parseFloat(setValue) + 788.00;
        newTot = parseFloat(newTot).toFixed(2);
        $('.totCost').text(newTot);
    });
});

// Input mask for phone number 
document.getElementById('phone').addEventListener('input', function (e) {
    var x = e.target.value.replace(/\D/g, '').match(/(\d{0,3})(\d{0,3})(\d{0,4})/);
    e.target.value = !x[2] ? x[1] : '(' + x[1] + ') ' + x[2] + (x[3] ? '-' + x[3] : '');
});