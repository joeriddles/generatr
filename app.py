from __future__ import annotations

from flask import Flask, render_template

from generatr.generatr import Generatr



app = Flask(__name__)
generatr = Generatr()

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
