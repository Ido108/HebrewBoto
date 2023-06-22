from hebrew_spell_checker import HebrewSpellChecker

def test_check_spelling():
    spell_checker = HebrewSpellChecker()
    assert spell_checker.check_spelling('זהו') == True
    assert spell_checker.check_spelling('זהוו') == False
