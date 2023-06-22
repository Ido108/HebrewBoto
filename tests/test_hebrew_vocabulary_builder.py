from hebrew_vocabulary_builder import HebrewVocabularyBuilder

def test_build_vocabulary():
    vocabulary_builder = HebrewVocabularyBuilder()
    words = ['זהו', 'טקסט', 'בעברית', 'זהו', 'טקסט']
    assert vocabulary_builder.build_vocabulary(words) == ['בעברית', 'זהו', 'טקסט']
