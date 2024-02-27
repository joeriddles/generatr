from __future__ import annotations
import random
from typing import Tuple

from generatr.utils.files import ALL_WORDS_PATH, SASS_WORDS_PATH, read_file, write_file, file_exists


SASS_ENDINGS = ('ar', 'er', 'ir', 'or', 'ur')
DOMAIN_REGISTRAR_URL_PREFIX = 'https://porkbun.com/checkout/search?q='


class Generatr:
    sass_words: list[str] = []

    def __init__(self, regenerate: bool = False):  # TODO: revert to True
        if regenerate or not file_exists(SASS_WORDS_PATH):
            sass_words = self._generate_sass_file()
        else:
            sass_words = read_file(SASS_WORDS_PATH)
        self.sass_words = sass_words            

    def get_random_word(self, words: list[str]) -> str:
        return random.choice(words)

    def generate_sass_word(self, word: str) -> str:
        while word.endswith(('ar', 'er', 'ir', 'or', 'ur')):
            word = word[:-2] + 'r'
        return word

    def generate_sass_url(self, sass_word: str) -> str:
        sass_url = 'https://' + sass_word + '.io'
        return sass_url

    def generate(self, word: str = "") -> Tuple[str, str, str]:
        """Return generated sass word, url, and domain registrar purchase url"""
        if not word:
            word = self.get_random_word(self.sass_words)
        sass_word = self.generate_sass_word(word)
        sass_url = self.generate_sass_url(sass_word)
        purchase_sass_url = DOMAIN_REGISTRAR_URL_PREFIX + sass_word + '.io'
        return sass_word, sass_url, purchase_sass_url

    def _generate_sass_file(self) -> list[str]:
        all_words: list[str] = []
        if file_exists(ALL_WORDS_PATH):
            all_words = read_file(ALL_WORDS_PATH)
        sass_words = [
            word
            for word
            in all_words
            if word.endswith(SASS_ENDINGS)
        ]
        write_file(SASS_WORDS_PATH, sass_words)
        return sass_words
