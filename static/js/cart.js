$(document).ready(function() {
    var cart = lsGet('cart');

    $.ajax({
        url: '/cart/render/',
        type: 'POST',
        data: { cart: JSON.stringify(cart) },
        success: function (data) {
            $('html')[0].innerHTML = data;

            for (var id in cart) {
                $(`.product[id=${id}]`).val(cart[id]);
            }

            $('.product').on('change', function() {
               var id = $(this).attr('id');
               var count = +$(this).val();
               var cart = lsGet('cart');

               if (count === 0) {
                   delete cart[id];
                   $(this.parentNode).remove();
               }
               else {
                   cart[id] = count;
               }

               lsSet('cart', cart);
            });

            $('.remove-product').on('click', function() {
                var row = $(this.parentNode);
                var id = row.find('.product').attr('id');
                var cart = lsGet('cart');
                delete cart[id];
                lsSet('cart', cart);
                row.remove();
            });

            $('#add-order').on('click', function() {
                $.ajax({
                    url: '/accounts/order/add/',
                    type: 'POST',
                    data: {cart: JSON.stringify(lsGet('cart'))},
                    success: function (data) {
                        if (data.status === 'success') {
                            lsSet('cart', {});
                            window.location = '/';
                        }
                    }
                });
            });
        }
    });
});
