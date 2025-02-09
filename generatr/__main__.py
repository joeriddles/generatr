from __future__ import annotations

import typer

from generatr.generatr import Generatr

typer_app = typer.Typer()


@typer_app.command()
def word():
    generatr = Generatr()
    word = generatr.get_random_word()
    saas_word = generatr.generate_saas_word(word)
    saas_url = generatr.generate_saas_url(saas_word)
    print(f"{word} -> {saas_word} -> {saas_url}")


if __name__ == "__main__":
    typer_app()
