class WordFreq(object):
    def __init__(self, head_word=None, next_word=None,
                 head_pos=None, next_pos=None, word_pos=None):
        self.head_word = head_word
        self.next_word = next_word
        self.head_pos = head_pos
        self.next_pos = next_pos
        self.word_pos = word_pos

    def __bool__(self):
        return bool(self.head_word and self.next_word and self.head_pos \
                    and self.next_pos and self.word_pos)

def __inc_dict_dict(d, v0, v1):
    value = d.get(v0, {})
    value[v1] = value.get(v1, 0) + 1
    d[v0] = value

def get_freq(l):
    head, next_word = {}, {}
    head_pos, next_pos = {}, {}
    word_pos = {}
    last_word, last_prop = '', ''
    # calculate word freq
    for word, prop in l:
        word_pos[word] = prop
        if prop != 'x':
            if last_word and last_prop:
                __inc_dict_dict(next_word, last_word, word)
                __inc_dict_dict(next_pos, last_prop, prop)
                last_word, last_prop = word, prop
            else:
                head[word] = head.get(word, 0) + 1
                head_pos[prop] = head_pos.get(prop, 0) + 1
                last_word, last_prop = word, prop
        else:
            if last_word and last_prop:
                __inc_dict_dict(next_word, last_word, word)
                __inc_dict_dict(next_pos, last_prop, prop)
                last_word, last_prop = '', ''
    # return the result
    return WordFreq(head, next_word, head_pos, next_pos, word_pos)

if __name__ == '__main__':
    pass
