class HebrewText:
    def __init__(self, text):
        self.text = text

    def get_text(self):
        return self.text

    def set_text(self, text):
        self.text = text

    def get_num_words(self):
        return len(self.text.split())
