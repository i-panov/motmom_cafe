
function lsSet(key, value) {
    localStorage.setItem(key, JSON.stringify(value));
}

function lsGet(key) {
    return JSON.parse(localStorage.getItem(key));
}


if (lsGet('cart') === null) {
    lsSet('cart', {});
}
