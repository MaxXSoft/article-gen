class WordFreq(object):
    def __init__(self, head_word=None, next_word=None,
                 head_prop=None, next_prop=None, word_prop=None):
        self.head_word = head_word
        self.next_word = next_word
        self.head_prop = head_prop
        self.next_prop = next_prop
        self.word_prop = word_prop

    def __bool__(self):
        return bool(self.head_word and self.next_word and self.head_prop \
                    and self.next_prop and self.word_prop)

def __inc_dict_dict(d, v0, v1):
    value = d.get(v0, {})
    value[v1] = value.get(v1, 0) + 1
    d[v0] = value

def get_freq(l):
    head, next_word = {}, {}
    head_prop, next_prop = {}, {}
    word_prop = {}
    last_word, last_prop = '', ''
    # calculate word freq
    for word, prop in l:
        word_prop[word] = prop
        if prop != 'x':
            if last_word and last_prop:
                __inc_dict_dict(next_word, last_word, word)
                __inc_dict_dict(next_prop, last_prop, prop)
                last_word, last_prop = word, prop
            else:
                head[word] = head.get(word, 0) + 1
                head_prop[prop] = head_prop.get(prop, 0) + 1
                last_word, last_prop = word, prop
        else:
            if last_word and last_prop:
                __inc_dict_dict(next_word, last_word, word)
                __inc_dict_dict(next_prop, last_prop, prop)
                last_word, last_prop = '', ''
    # return the result
    return WordFreq(head, next_word,
                    head_prop, next_prop, word_prop)

if __name__ == '__main__':
    pass
