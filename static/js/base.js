String.prototype.capitalize = function() {
    return this.charAt(0).toUpperCase() + this.slice(1);
}

function lsSet(key, value) {
    localStorage.setItem(key, JSON.stringify(value));
}

function lsGet(key) {
    return JSON.parse(localStorage.getItem(key));
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function copyTextToClipboard(text) {
    var input = document.createElement('input');
    input.display = 'none';
    input.value = text;
    document.body.appendChild(input);
    input.select();
    document.execCommand('copy');
    document.body.removeChild(input);
}

if (lsGet('cart') === null) {
    lsSet('cart', {});
}

$.ajaxSetup({
    headers: { "X-CSRFToken": getCookie("csrftoken") }
});
