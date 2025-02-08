function get_word() {
    const url = "/api/word";
    fetch(url)
        .then(response => response.json())
        .then(jsonResponse => {
            const { sass_word, sass_url, purchase_sass_url } = jsonResponse;
            document.getElementById("sass-word").innerHTML = sass_word;
            document.getElementById("sass-url").href = sass_url;
            document.getElementById("sass-url-value").innerHTML = sass_url;
            document.getElementById("purchase-sass-url").href = purchase_sass_url
        });
}
