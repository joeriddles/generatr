from __future__ import annotations

import dataclasses
import json
import random
from typing import Tuple

import requests

from generatr.utils.files import (
    ALL_WORDS_PATH,
    SAAS_WORDS_PATH,
    file_exists,
    read_file,
    write_file,
)
from generatr.utils.files.files import PORKBUN_PRICING_PATH

SAAS_ENDINGS = ("ar", "er", "ir", "or", "ur")
DOMAIN_REGISTRAR_URL_PREFIX = "https://porkbun.com/checkout/search?q="

@dataclasses.dataclass
class PorkbunPrice:
    registration: str
    renewal: str
    transfer: str
    coupons: list
    specialType: str = ""


@dataclasses.dataclass
class GeneratrResult:
    word: str
    saas_word: str
    url: str
    purchase_url: str
    price: PorkbunPrice | None


class Generatr:
    saas_words: list[str] = []
    _pricing: dict[str, PorkbunPrice] = {}

    def __init__(self, regenerate_words: bool = False, get_pricing: bool = False):
        if regenerate_words or not file_exists(SAAS_WORDS_PATH):
            saas_words = self._generate_saas_file()
        else:
            saas_words = read_file(SAAS_WORDS_PATH)
        self.saas_words = saas_words

        pricing: dict[str, dict] | None = None
        if get_pricing or not file_exists(PORKBUN_PRICING_PATH):
            pricing_resp = requests.get("https://api.porkbun.com/api/json/v3/pricing/get")
            if pricing_resp.ok:
                body = pricing_resp.json()
                if body.get("status", "").casefold() == "success":
                    write_file(PORKBUN_PRICING_PATH, [pricing_resp.text])
                    pricing = body["pricing"]
                else:
                    print(f"pricing request failed {pricing_resp.status_code}: {pricing_resp.text}")
            else:
                print(f"pricing request failed {pricing_resp.status_code}: {pricing_resp.text}")
        if not pricing and file_exists(PORKBUN_PRICING_PATH):
            pricing = json.loads(read_file(PORKBUN_PRICING_PATH)[0])["pricing"]

        if pricing:
            self._pricing = {
                tldn: PorkbunPrice(**price)
                for tldn, price
                in pricing.items()
            }

    def get_random_word(self, words: list[str]) -> str:
        return random.choice(words)

    def generate_saas_word(self, word: str) -> str:
        while word.endswith(("ar", "er", "ir", "or", "ur")):
            word = word[:-2] + "r"
        return word

    def generate_saas_url(self, saas_word: str) -> str:
        saas_url = "https://" + saas_word + ".io"
        return saas_url

    def generate(self, word: str = "") -> GeneratrResult:
        """Return generated saas word, url, domain registrar purchase url, and maybe price."""
        if not word:
            word = self.get_random_word(self.saas_words)
        saas_word = self.generate_saas_word(word)
        saas_url = self.generate_saas_url(saas_word)
        price = self._pricing.get("io", None)
        purchase_saas_url = DOMAIN_REGISTRAR_URL_PREFIX + saas_word + ".io"
        return GeneratrResult(word, saas_word, saas_url, purchase_saas_url, price)

    def _generate_saas_file(self) -> list[str]:
        all_words: list[str] = []
        if file_exists(ALL_WORDS_PATH):
            all_words = read_file(ALL_WORDS_PATH)
        saas_words = [word for word in all_words if word.endswith(SAAS_ENDINGS)]
        write_file(SAAS_WORDS_PATH, saas_words)
        return saas_words
