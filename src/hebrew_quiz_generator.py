import random

class HebrewQuizGenerator:
    def generate_quiz(self, text):
        tokenizer = HebrewTokenizer()
        words = tokenizer.tokenize(text)
        quiz = []
        for word in words:
            if len(word) > 2:
                quiz.append({'word': word, 'options': self._generate_options(word)})
        return quiz

    def _generate_options(self, word):
        options = [word]
        while len(options) < 4:
            option = ''.join(random.sample(word, len(word)))
            if option not in options:
                options.append(option)
        random.shuffle(options)
        return options
