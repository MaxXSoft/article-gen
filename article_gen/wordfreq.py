def is_word(word):
    first = word[0]
    return '\u4e00' <= first <= '\u9fff' or 'a' <= first.lower() <= 'z' or '0' <= first <= '9'

def get_freq(l):
    next_word = {}
    head = {}
    last_word = ''
    # calculate word freq
    for word in l:
        if is_word(word):
            if last_word:
                next_list = next_word.get(last_word, {})
                next_list[word] = next_list.get(word, 0) + 1
                next_word[last_word] = next_list
                last_word = word
            else:
                head[word] = head.get(word, 0) + 1
                last_word = word
        else:
            if last_word:
                next_list = next_word.get(last_word, {})
                next_list[word] = next_list.get(word, 0) + 1
                next_word[last_word] = next_list
                last_word = ''
    # reverse word freq dictionary
    next_word_rev = {}
    head_rev = {}
    # reverse next_word
    for word, d in next_word.items():
        d_rev = {}
        for w, count in d.items():
            l = d_rev.get(count, [])
            l.append(w)
            d_rev[count] = l
        next_word_rev[word] = d_rev
    # reverse head
    for word, count in head.items():
        l = head_rev.get(count, [])
        l.append(word)
        head_rev[count] = l
    # return the result
    return head_rev, next_word_rev

if __name__ == '__main__':
    pass
