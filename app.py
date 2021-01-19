from __future__ import annotations

from flask import Flask, render_template

from generatr.generatr import generate


app = Flask(__name__)
GOOGLE_URL_PREFIX = 'https://domains.google.com/registrar/search?searchTerm='

@app.route('/')
def main():
    sass_word, sass_url = generate()
    google_sass_url = GOOGLE_URL_PREFIX + sass_word + '.io'
    render_result = render_template('template.html', sass_word=sass_word, sass_url=sass_url, google_sass_url=google_sass_url)
    return render_result
