import wordfreq
import random, sys

class SentenceGen(object):
    def __init__(self, separator='', use_weight=True):
        self.separator = separator
        self.use_weight = use_weight
        self.new_seed()

    def __choice(self, weight):
        if self.use_weight:
            t = random.randint(0, sum(weight) - 1)
            for val in weight:
                t -= val
                if t < 0:
                    return val
        else:
            return random.choice(list(weight))

    def seed(self):
        return self.__seed

    def new_seed(self, seed=-1):
        self.__seed = seed if seed > -1 else random.randint(0, sys.maxsize)
        random.seed(self.__seed)
        return self.__seed

    def word_choice(self, word_dict):
        k = self.__choice(word_dict.keys())
        l = word_dict[k]
        return random.choice(l)

    def next(self, word, next_word):
        sentence = ''
        new_word = word
        while wordfreq.is_word(new_word):
            sentence += new_word + self.separator
            word_dict = next_word[new_word]
            new_word = self.word_choice(word_dict)
        return sentence + new_word + self.separator
