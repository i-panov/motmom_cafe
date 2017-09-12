$(document).ready(function() {
    $.ajax({
        url: '/cart/render/',
        type: 'POST',
        data: { cart: JSON.stringify(lsGet('cart')) },
        success: function (data) {
            $('html')[0].innerHTML = data;
        }
    });
});
