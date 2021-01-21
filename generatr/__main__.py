from __future__ import annotations

import typer

from generatr.generatr import Generatr

typer_app = typer.Typer()

@typer_app.command()
def word():
    generatr = Generatr()
    word = generatr.get_random_word()
    sass_word = generatr.generate_sass_word(word)
    sass_url = generatr.generate_sass_url(sass_word)
    print(f'{word} -> {sass_word} -> {sass_url}')


if __name__ == '__main__':
    typer_app()
