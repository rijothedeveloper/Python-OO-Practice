"""Word Finder: finds random words from a dictionary."""


import random

class WordFinder:
    def __init__(self):
        self.words = []
        file = open("words.txt", "r")
        for line in file:
            self.words.append(line)
        print(f"{len(self.words)} words read")
    
    def random(self):
        return random.choice(self.words)
