$(document).ready(function() {
    var cart = lsGet('cart');

    for (var id in cart) {
        $(`.product[id=${id}]`).val(cart[id]);
    }
});

$('.product').on('change', function() {
   var id = $(this).attr('id');
   var count = +$(this).val();
   var cart = lsGet('cart');

   if (count === 0) {
       delete cart[id];
   }
   else {
       cart[id] = count;
   }

   lsSet('cart', cart);
});
