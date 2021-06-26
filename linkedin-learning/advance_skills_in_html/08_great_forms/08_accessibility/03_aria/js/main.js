$(document).ready(function () {
    // helper-tip
    var btn = $(".fas.tooltip");
    $(btn).click(function () {
        $(this).siblings(".helperText").toggle();
    });

    $(".closeBtn").click(function () {
        $(this).parent("div").toggle();
    })
    // close helper-tip on input focus
    $("input").click(function () {
        $(".questWrap div").hide();
    })
});

// custom checkbox
function changeCheckbox(event) {
    let item = document.getElementById('chkPref');
    switch (item.getAttribute('aria-checked')) {
        case "true":
            item.setAttribute('aria-checked', "false");
            break;
        case "false":
            item.setAttribute('aria-checked', "true");
            break;
    }
}