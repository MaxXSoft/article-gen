import wordlist, wordfreq, sentence
import random, pickle

class ArticleGen(object):
    def __init__(self, dump_file='', show_progress=False, separator='', use_weight=True):
        self.__wordlist = wordlist.WordList()
        self.__sentence = sentence.SentenceGen()
        self.__head = {}
        self.__next_word = {}
        self.dump_file = dump_file
        self.show_progress = show_progress
        self.separator = separator
        self.use_weight = use_weight

    def load(self, file_list):
        self.__wordlist.show_progress = self.show_progress
        word_list = self.__wordlist.get_from_list(file_list)
        if not word_list:
            return False
        else:
            self.__head, self.__next_word = wordfreq.get_freq(word_list)
            return True if self.__head and self.__next_word else False

    def load_dump(self):
        if self.dump_file:
            with open(self.dump_file, 'rb') as f:
                hn_list = pickle.load(f)
            self.__head, self.__next_word = hn_list[0], hn_list[1]
            return True if self.__head and self.__next_word else False
        else:
            False
    
    def dump(self):
        if self.dump_file:
            with open(self.dump_file, 'wb') as f:
                pickle.dump([self.__head, self.__next_word], f)
            return True
        else:
            return False

    def seed(self):
        return self.__sentence.seed()
    
    def new_seed(self, seed=-1):
        return self.__sentence.new_seed(seed)

    def generate(self, length=0):
        article = ''
        if not length:
            length = random.randint(10, 50)
        self.__sentence.use_weight = self.use_weight
        self.__sentence.separator = self.separator
        if self.__head and self.__next_word:
            for i in range(length):
                i
                word = self.__sentence.word_choice(self.__head)
                article += self.__sentence.next(word, self.__next_word)
        return article
