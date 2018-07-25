import wordfreq
import random, sys

class SentenceGen(object):
    def __init__(self, separator='', use_weight=True, pos_prop=0.5):
        self.__head_candidate = {}
        self.__word_cand_dict = {}
        self.separator = separator
        self.use_weight = use_weight
        self.pos_prop = pos_prop
        self.word_freq = wordfreq.WordFreq()
        self.new_seed()

    def __choice(self, weight):
        if self.use_weight:
            bound = sum(weight) - 1
            if bound < 0:
                return random.randint(0, len(weight) - 1)
            else:
                t = random.randint(0, bound)
                for i, val in enumerate(weight):
                    t -= val
                    if t < 0:
                        return i
        else:
            return random.randint(0, len(weight) - 1)

    def seed(self):
        return self.__seed

    def new_seed(self, seed=-1):
        self.__seed = seed if seed > -1 else random.randint(0, sys.maxsize)
        random.seed(self.__seed)
        return self.__seed

    def __get_candidate(self, word_dict, pos_dict):
        candidate = {}
        for word, count in word_dict.items():
            pos = self.word_freq.word_pos[word]
            pos_count = pos_dict.get(pos, 0)
            candidate[word] = int(count * (1 - self.pos_prop) + \
                                  pos_count * self.pos_prop)
        return candidate

    def __word_choice(self, candidate):
        i = self.__choice(candidate.values())
        return list(candidate.keys())[i]

    def head(self):
        if not self.__head_candidate:
            self.__head_candidate = self.__get_candidate(
                    self.word_freq.head_word, self.word_freq.head_pos)
        return self.__word_choice(self.__head_candidate)

    def next(self):
        sentence = ''
        new_word = self.head()
        new_pos = self.word_freq.word_pos[new_word]
        while new_pos != 'x':
            sentence += new_word + self.separator
            candidate = self.__word_cand_dict.get(new_word)
            if not candidate:
                word_dict = self.word_freq.next_word[new_word]
                pos_dict = self.word_freq.next_pos[new_pos]
                candidate = self.__get_candidate(word_dict, pos_dict)
                self.__word_cand_dict[new_word] = candidate
            new_word = self.__word_choice(candidate)
            new_pos = self.word_freq.word_pos[new_word]
        return sentence + new_word + self.separator

if __name__ == '__main__':
    pass
