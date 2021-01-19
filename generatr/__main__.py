from __future__ import annotations

import typer

from generatr.generatr import generate_sass_url, generate_sass_word, get_random_word, read_er_words

typer_app = typer.Typer()

@typer_app.command()
def word():
    words = read_er_words()
    word = get_random_word(words)
    sass_word = generate_sass_word(word)
    sass_url = generate_sass_url(sass_word)
    print(f'{word} -> {sass_word} -> {sass_url}')


if __name__ == '__main__':
    typer_app()
