from wordfinder import WordFinder


class SpecialWordFinder(WordFinder):
    def __init__(self):
        super.__init__()
        self.newWords = []
        for word in self.words:
            if not word.startsWith(" ") or not word.startsWith("#"):
                self.newWords.append(self.word)
