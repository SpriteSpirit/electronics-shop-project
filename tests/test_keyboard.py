def test_change_lang(keyboard):
    keyboard.change_lang()
    assert keyboard.language == 'RU'

    keyboard.change_lang()
    assert keyboard.language == 'EN'
