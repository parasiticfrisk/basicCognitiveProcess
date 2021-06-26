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

    // format the CC as user types number
    $("#ccNum").on("keydown", function (e) {
        var cursor = this.selectionStart;
        if (this.selectionEnd != cursor) return;
        if (e.which == 46) {
            if (this.value[cursor] == " ") this.selectionStart++;
        } else if (e.which == 8) {
            if (cursor && this.value[cursor - 1] == " ") this.selectionEnd--;
        }
    }).on("input", function () {
        var value = this.value;
        var cursor = this.selectionStart;
        var matches = value.substring(0, cursor).match(/[^0-9]/g);
        if (matches) cursor -= matches.length;
        value = value.replace(/[^0-9]/g, "").substring(0, 16);
        var formatted = "";
        for (var i = 0, n = value.length; i < n; i++) {
            if (i && i % 4 == 0) {
                if (formatted.length <= cursor) cursor++;
                formatted += " ";
            }
            formatted += value[i];
        }
        if (formatted == this.value) return;
        this.value = formatted;
        this.selectionEnd = cursor;
    });

    // change credit card icon color      
    $('#ccNum').keyup(function () {
        var value = $(this).val();
        if (value.match(/^4/)) { // if the value starts with a 4 (visa)
            $('i.fa-cc-visa').addClass('visa');
        } else if (value.match(/^5/)) { // if the value starts with a 5 (mc)
            $('i.fa-cc-mastercard').addClass('mc');
        } else { // if neither is true remove either of the classes
            $('i.cc').removeClass('visa').removeClass('mc');;
        }
    })

    // CVV tooltip
    // hide the CVV helper text div
    document.querySelector('.helperText').classList.add('hide');
    // make the tooltip able to close on click
    const tooltip = document.querySelector('.tooltip');
    tooltip.addEventListener('click', function () {
        document.querySelector('.helperText').classList.toggle('show'); // togle the tooltip to show or hide
        document.querySelector('.helperText').classList.toggle('hide');
    })

    // expiration date formatting, add a slash after 2 characters have been entered
    var characterCount
    $('#exp').on('input', function (e) {
        if ($(this).val().length == 2 && characterCount < $(this).val().length) {
            $(this).val($(this).val() + '/');
        }
        characterCount = $(this).val().length;
    });
});

// Input mask for phone number 
document.getElementById('phone').addEventListener('input', function (e) {
    var x = e.target.value.replace(/\D/g, '').match(/(\d{0,3})(\d{0,3})(\d{0,4})/);
    e.target.value = !x[2] ? x[1] : '(' + x[1] + ') ' + x[2] + (x[3] ? '-' + x[3] : '');
});