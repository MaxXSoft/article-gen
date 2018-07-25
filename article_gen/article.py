import wordlist, wordfreq, sentence
import random, pickle

class ArticleGen(object):
    def __init__(self, dump_file='', show_progress=False, separator='',
                 use_weight=True, pos_prop=0.5):
        self.__wordlist = wordlist.WordList()
        self.__word_freq = wordfreq.WordFreq()
        self.__sentence = sentence.SentenceGen()
        self.dump_file = dump_file
        self.show_progress = show_progress
        self.separator = separator
        self.use_weight = use_weight
        self.pos_prop = pos_prop

    def load(self, file_list):
        self.__wordlist.show_progress = self.show_progress
        word_list = self.__wordlist.get_from_list(file_list)
        if not word_list:
            return False
        else:
            self.__word_freq = wordfreq.get_freq(word_list)
            return True if self.__word_freq else False

    def load_dump(self):
        if self.dump_file:
            try:
                with open(self.dump_file, 'rb') as f:
                    self.__word_freq = pickle.load(f)
            except:
                return False
            return True
        else:
            False
    
    def dump(self):
        if self.dump_file:
            with open(self.dump_file, 'wb') as f:
                pickle.dump(self.__word_freq, f)
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
        self.__sentence.separator = self.separator
        self.__sentence.use_weight = self.use_weight
        self.__sentence.pos_prop = self.pos_prop
        self.__sentence.word_freq = self.__word_freq
        if self.__word_freq:
            for i in range(length):
                i
                article += self.__sentence.next()
        return article

if __name__ == '__main__':
    pass
