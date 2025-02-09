from generatr import generate_saas_word

words = {
    "hello": "hello",
    "runner": "runnr",
    "runneer": "runnr",
}


def test__generate_saas_word():
    for word, expected in words.items():
        actual = generate_saas_word(word)
        assert actual == expected
