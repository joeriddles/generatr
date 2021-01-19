from __future__ import annotations
import os
import random
from typing import Tuple

TOP_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

def read_file(filepath: str) -> list[str]:
    with open(filepath, 'r') as infile:
        return [
            line.strip()
            for line
            in infile.readlines()
        ]

def read_er_words() -> list[str]:
    words_filepath = os.path.join(TOP_DIR, 'data', 'words_er.txt')
    words = read_file(words_filepath)
    return words

def get_random_word(words: list[str]) -> str:
    return random.choice(words)

def generate_sass_word(word: str) -> str:
    while word.endswith(('ar', 'er', 'ir', 'or', 'ur')):
        word = word[:-2] + 'r'
    return word

def generate_sass_url(sass_word: str) -> str:
    sass_url = 'https://' + sass_word + '.io'
    return sass_url

def generate() -> Tuple[str, str]:
    words = read_er_words()
    word = get_random_word(words)
    sass_word = generate_sass_word(word)
    sass_url = generate_sass_url(sass_word)
    return sass_word, sass_url