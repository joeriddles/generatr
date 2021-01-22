function get_word() {
    const url = "./api/word";
    fetch(url)
        .then(response => response.json())
        .then(jsonResponse => {
            sass_word = jsonResponse.sass_word;
            sass_url = jsonResponse.sass_url;
            google_sass_url = jsonResponse.google_sass_url;
            sass_word_elem = document.getElementById("sass-word");
            sass_word_elem.innerHTML = sass_word;
            sass_url_elem = document.getElementById("sass-url");
            sass_url_elem.innerHTML = sass_url;
            google_sass_url_elem = document.getElementById("google-sass-url");
            google_sass_url_elem.href = google_sass_url
        });
}
