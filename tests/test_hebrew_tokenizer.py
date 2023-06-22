from hebrew_tokenizer import HebrewTokenizer

def test_tokenize():
    text = 'זהו טקסט בעברית'
    tokenizer = HebrewTokenizer()
    assert tokenizer.tokenize(text) == ['זהו', 'טקסט', 'בעברית']
