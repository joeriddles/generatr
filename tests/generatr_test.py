from generatr import generate_sass_word

words = {
    'hello': 'hello',
    'runner': 'runnr',
    'runneer': 'runnr',
}


def test__generate_sass_word():
    for word, expected in words.items():
        actual = generate_sass_word(word)
        assert actual == expected
