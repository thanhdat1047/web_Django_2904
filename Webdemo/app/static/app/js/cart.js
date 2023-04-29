var updateBtns = document.getElementsByClassName('update-cart')
for (i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId', productId, 'action', action)
        console.log('user: ', user)
        if (user === "AnonymumousUser") {
            console.log("user not logged in")
        } else {
            updateUserOrder(productId, action)
        }

    })
}
function updateUserOrder(productId, action) {
    console.log("user logged in")
    var url = '/update_item/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
            'productId': productId,
            'action': action
        })

    })
        .then((response) => {
            // if (!response.ok) {
            //     throw Error(response.statusText);
            // }
            return response.json()
        })
        // .catch((error) => {
        //     console.log('Error:', error);
        // })
        .then((data) => {
            console.log('Data:', data)
            window.location.reload(true)
            // xử lý data tiếp ở đây
        })

}