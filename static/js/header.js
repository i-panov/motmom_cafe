$('#cart').on('click', function() {
    $.ajax({
        url: '/cart',
        data: lsGet('cart'),
        async: false,
        method: 'post'
    })
});
