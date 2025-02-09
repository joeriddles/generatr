from __future__ import annotations

import random
from typing import Tuple

from generatr.utils.files import (
    ALL_WORDS_PATH,
    SAAS_WORDS_PATH,
    file_exists,
    read_file,
    write_file,
)

SAAS_ENDINGS = ("ar", "er", "ir", "or", "ur")
DOMAIN_REGISTRAR_URL_PREFIX = "https://porkbun.com/checkout/search?q="


class Generatr:
    saas_words: list[str] = []

    def __init__(self, regenerate: bool = False):  # TODO: revert to True
        if regenerate or not file_exists(SAAS_WORDS_PATH):
            saas_words = self._generate_saas_file()
        else:
            saas_words = read_file(SAAS_WORDS_PATH)
        self.saas_words = saas_words

    def get_random_word(self, words: list[str]) -> str:
        return random.choice(words)

    def generate_saas_word(self, word: str) -> str:
        while word.endswith(("ar", "er", "ir", "or", "ur")):
            word = word[:-2] + "r"
        return word

    def generate_saas_url(self, saas_word: str) -> str:
        saas_url = "https://" + saas_word + ".io"
        return saas_url

    def generate(self, word: str = "") -> Tuple[str, str, str]:
        """Return generated saas word, url, and domain registrar purchase url"""
        if not word:
            word = self.get_random_word(self.saas_words)
        saas_word = self.generate_saas_word(word)
        saas_url = self.generate_saas_url(saas_word)
        purchase_saas_url = DOMAIN_REGISTRAR_URL_PREFIX + saas_word + ".io"
        return saas_word, saas_url, purchase_saas_url

    def _generate_saas_file(self) -> list[str]:
        all_words: list[str] = []
        if file_exists(ALL_WORDS_PATH):
            all_words = read_file(ALL_WORDS_PATH)
        saas_words = [word for word in all_words if word.endswith(SAAS_ENDINGS)]
        write_file(SAAS_WORDS_PATH, saas_words)
        return saas_words
