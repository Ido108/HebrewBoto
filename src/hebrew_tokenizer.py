import re

class HebrewTokenizer:
    def __init__(self):
        self.pattern = re.compile(r'[\u0590-\u05FF]+')

    def tokenize(self, text):
        return self.pattern.findall(text)
