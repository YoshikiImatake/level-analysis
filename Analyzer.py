import re

class Analyzer:
    def __init__(self, text, reviewed):
        self.text = text
        self.reviewed = reviewed
 
    def sentence_length(self, text):
        text_splitted = re.split('\n|。', text)
        print(text_splitted[0])






