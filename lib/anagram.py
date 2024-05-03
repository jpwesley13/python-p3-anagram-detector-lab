class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, list):
        anagram = []
        for words in list:
            if sorted([letter for letter in words]) == sorted([letter for letter in self.word]):
                anagram.append(words)
            else: 
                return anagram