"""Task about class container and iterator"""

import re


class Sentence:
    """Class container"""

    def __init__(self, text: str):

        # if text have a something digits
        if any(map(str.isdigit, text)):
            raise TypeError

        check = r"(\w\s)*[!|?|...|.]"
        correct = re.finditer(check, text)
        indices = [m.start(0) for m in correct]

        if (len(indices) == 1 and text[indices[0]] != text[-1]) or text == "":
            raise ValueError
        if len(indices) != 1 or text[:3] != "...":
            raise MultipleSentencesError

        self.text = text
        self.len_words = len(re.findall("[A-z]+", self.text))
        self.len_others = len(re.findall("[^A-z]", self.text))
        self.words_ = self._words()
        self.other_ = (char for char in re.findall("[^A-z]", self.text))

    def __repr__(self):
        """Get info about words and chars"""
        return f"<Sentence(words={self.len_words}, other_chars={self.len_others})>"

    def __iter__(self):
        return SentenceIterator(self.text, self.len_words)

    def __getitem__(self, index):
        """Get words by index or slice"""
        if isinstance(index, slice):
            return list(self.words_)[index.start:index.stop:index.step]
        if index < 0 or index > self.len_words:
            raise IndexError
        return list(self.words_)[index]

    def _words(self):
        """lazy iterator"""
        return (word for word in re.findall("[A-z]+", self.text))

    @property
    def words(self):
        """Get all words from text"""
        return list(self.words_)

    @property
    def other_chars(self):
        """Get all other chars from text"""
        return list(self.other_)


class MultipleSentencesError(Exception):
    """Custom exception about 2+ sentences in text"""


class SentenceIterator:
    """Class iterator"""

    def __init__(self, text, len_text):
        self.text = text
        self._counter = len_text

    def _get_word(self):
        """Get next word from text"""
        if self._counter > 0:
            next_word = re.match("[A-z]+", self.text).group()
            self.text = self.text[len(next_word) + 1:]
            self._counter -= 1
            return next_word
        raise StopIteration

    def __next__(self):
        """Return func about next word"""
        return self._get_word()

    def __iter__(self):
        """For work iterations"""
        return self


# # Test about for and __repr__
# while True:
#     message = input("Text ---> ")
#     temp = Sentence(message)
#     print(temp)
#     for i in temp:
#         print(i)

# # Test about index
# print(Sentence("Vlad hello.")[0])

# print(Sentence("Hello all every body and all.")[2:])  # ['every', 'body', 'and', 'all']

# # Test about next()
# words_all = Sentence('Hello word!')._words()
# print(next(words_all))
# print(next(words_all))
# print(next(words_all))  # Stop Iteration

# # Test about iter
# test1 = Sentence("Vlad demo.")
# hop = iter(test1)
# for i in hop:
#     print(i)

# # Test about @property
# mess = Sentence("Hello Vlad.")
# print(mess.words)  # get list words
# print(mess.other_chars)  # get list other chairs

# # Test about multiple
# new_text = Sentence("Hello! World.")  # get MultipleSentencesError
