import re

class HebrewGrammarChecker:
    def __init__(self):
        self.pattern = re.compile(r'[\u0590-\u05FF]+')

    def check_grammar(self, text):
        errors = []
        words = self.pattern.findall(text)
        for i in range(len(words) - 1):
            if words[i][-2:] == 'הם' and words[i+1][:2] == 'של':
                errors.append(f'Error: "{words[i]} {words[i+1]}" violates grammar rules')
        return errors
