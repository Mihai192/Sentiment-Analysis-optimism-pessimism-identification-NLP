import re

def tokenize(text):
    words = re.findall(r'\b\w+\b', text)
    return words
