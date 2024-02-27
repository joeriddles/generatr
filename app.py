from __future__ import annotations
import os

from flask import Flask, render_template
import flask.helpers

from generatr.generatr import Generatr

app = Flask(__name__)
generatr = Generatr()

# Force HTTPS links in production
if not app.debug:
    domain = os.environ["FLASK_DOMAIN"]
    force_https = os.environ.get("FLASK_FORCE_HTTPS", "true") == "true"

    def absolute_url_for(endpoint, **values) -> str:
        url: str = flask.helpers.url_for(endpoint, **values)
        url = domain + url

        if not url.startswith("http"):
            url = "http://" + url

        if force_https:
            url = url.replace("http://", "https://")

        return url

    app.jinja_env.globals.update(url_for=absolute_url_for)  # type: ignore

@app.route('/')
def main():
    sass_word, sass_url, purchase_sass_url = generatr.generate()
    render_result = render_template('template.html', sass_word=sass_word, sass_url=sass_url, purchase_sass_url=purchase_sass_url)
    return render_result

@app.route('/<word>/')
def word(word: str):
    sass_word, sass_url, purchase_sass_url = generatr.generate(word)
    render_result = render_template('template.html', sass_word=sass_word, sass_url=sass_url, purchase_sass_url=purchase_sass_url)
    return render_result

@app.route('/api/word/')
def get_word():
    result = {}
    result['sass_word'], result['sass_url'], result['purchase_sass_url'] = generatr.generate()
    return result
