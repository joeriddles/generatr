const saasWord = document.getElementById("saas-word")
const saasUrl = document.getElementById("saas-url")
const saasUrlValue = document.getElementById('saas-url-value')
const purchaseSaasUrl = document.getElementById("purchase-saas-url")
const previousSaas = document.getElementById("previous-saas")

function get_word() {
    const url = "/api/word";
    fetch(url)
        .then(response => response.json())
        .then(jsonResponse => {
            const previousWord = saasWord.innerText
            const previousUrl = saasUrl.href

            const { saas_word, saas_url, purchase_saas_url } = jsonResponse;
            saasWord.innerHTML = saas_word;
            saasUrl.href = saas_url;
            saasUrlValue.innerHTML = saas_url;
            purchaseSaasUrl.href = purchase_saas_url

            const previousLi = document.createElement("li")
            const previousLink = document.createElement("a")
            previousLink.href = previousUrl
            previousLink.innerText = previousWord
            previousLi.appendChild(previousLink)
            previousSaas.appendChild(previousLi)
        });
}
