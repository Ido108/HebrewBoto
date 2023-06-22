from hebrew_text import HebrewText

def test_get_text():
    text = 'זהו טקסט בעברית'
    hebrew_text = HebrewText(text)
    assert hebrew_text.get_text() == text

def test_set_text():
    text = 'זהו טקסט בעברית'
    new_text = 'זהו טקסט חדש בעברית'
    hebrew_text = HebrewText(text)
    hebrew_text.set_text(new_text)
    assert hebrew_text.get_text() == new_text

def test_get_num_words():
    text = 'זהו טקסט בעברית'
    hebrew_text = HebrewText(text)
    assert hebrew_text.get_num_words() == 3
