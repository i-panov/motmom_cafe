function setOrderStatus(pk, status) {
    $.ajax({
        url: '/accounts/set_order_status/',
        type: 'POST',
        data: { pk: pk, status: String(status).capitalize() },
        success: function (data) {
            if (data.status === 'success') {
                alert('Статус заказа успешно изменен!');
                window.location = '/';
            }
        }
    });
}
