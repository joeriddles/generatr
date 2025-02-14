from __future__ import annotations

import dataclasses
import os

import flask.helpers
from flask import Flask, render_template

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


@app.route("/")
def main():
    return _render_generate()


@app.route("/<word>/")
def word(word: str):
    return _render_generate(word)


@app.route("/api/word/")
def get_word():
    return dataclasses.asdict(generatr.generate())


def _render_generate(word: str = ""):
    result = generatr.generate(word)
    return render_template(
        "template.html",
        **dataclasses.asdict(result),
    )
