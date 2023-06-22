class HebrewSpellChecker:
    def __init__(self):
        self.dictionary = set(['אבגדהוזחטיכלמנסעפצקרשת'])

    def check_spelling(self, word):
        return set(word).issubset(self.dictionary)
