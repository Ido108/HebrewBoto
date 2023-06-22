from flask import Flask, render_template, request
from hebrew_text import HebrewText
from hebrew_tokenizer import HebrewTokenizer
from hebrew_spell_checker import HebrewSpellChecker
from hebrew_grammar_checker import HebrewGrammarChecker
from hebrew_vocabulary_builder import HebrewVocabularyBuilder
from hebrew_quiz_generator import HebrewQuizGenerator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/spell_check', methods=['POST'])
def spell_check():
    text = request.form['text']
    tokenizer = HebrewTokenizer()
    spell_checker = HebrewSpellChecker()
    words = tokenizer.tokenize(text)
    misspelled_words = []
    for word in words:
        if not spell_checker.check_spelling(word):
            misspelled_words.append(word)
    return {'misspelled_words': misspelled_words}

@app.route('/grammar_check', methods=['POST'])
def grammar_check():
    text = request.form['text']
    grammar_checker = HebrewGrammarChecker()
    return {'errors': grammar_checker.check_grammar(text)}

@app.route('/vocabulary', methods=['POST'])
def vocabulary():
    text = request.form['text']
    tokenizer = HebrewTokenizer()
    vocabulary_builder = HebrewVocabularyBuilder()
    words = tokenizer.tokenize(text)
    vocabulary = vocabulary_builder.build_vocabulary(words)
    return {'vocabulary': vocabulary}

@app.route('/quiz', methods=['POST'])
def quiz():
    text = request.form['text']
    quiz_generator = HebrewQuizGenerator()
    quiz = quiz_generator.generate_quiz(text)
    return {'quiz': quiz}

if __name__ == '__main__':
    app.run()
