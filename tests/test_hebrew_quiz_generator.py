from hebrew_quiz_generator import HebrewQuizGenerator

def test_generate_quiz():
    quiz_generator = HebrewQuizGenerator()
    text = 'זהו טקסט בעברית'
    quiz = quiz_generator.generate_quiz(text)
    assert len(quiz) == 2
    for question in quiz:
        assert question['word'] in text
        assert question['word'] in question['options']
        assert len(question['options']) == 4
