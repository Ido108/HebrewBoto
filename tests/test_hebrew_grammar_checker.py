from hebrew_grammar_checker import HebrewGrammarChecker

def test_check_grammar():
    grammar_checker = HebrewGrammarChecker()
    text = 'זהו טקסט שלא מפר את כללי הכתיב'
    assert grammar_checker.check_grammar(text) == []
    text = 'הם ספר של הספרים'
    assert grammar_checker.check_grammar(text) == ['Error: "הם ספר של" violates grammar rules']
