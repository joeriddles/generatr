const saasWord = document.getElementById("saas-word")
const saasUrl = document.getElementById("saas-url")
const saasUrlValue = document.getElementById('saas-url-value')
const purchaseSaasUrl = document.getElementById("purchase-saas-url")
const previousSaas = document.getElementById("previous-saas")
const priceEl = document.getElementById("price")

function get_word() {
    const url = "/api/word/";
    fetch(url)
        .then(response => response.json())
        .then(jsonResponse => {
            const previousWord = saasWord.innerText
            const previousUrl = saasUrl.href

            const { word, url, purchase_url, price } = jsonResponse;
            saasWord.innerHTML = word;
            saasUrl.href = url;
            saasUrlValue.innerHTML = url;
            purchaseSaasUrl.href = purchase_url
            priceEl.innerText = price?.registration ? `\$${price.registration}` : '💸'

            const previousLi = document.createElement("li")
            const previousLink = document.createElement("a")
            previousLink.href = previousUrl
            previousLink.innerText = previousWord
            previousLi.appendChild(previousLink)
            previousSaas.appendChild(previousLi)
        });
}
