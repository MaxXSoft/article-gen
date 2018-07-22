import jieba, os

jieba.default_logger.setLevel(jieba.logging.INFO)

class WordList(object):
    def __init__(self, show_progress=False):
        self.show_progress = show_progress

    def get(self, file):
        if self.show_progress:
            print('reading: %s' % file)
        try:
            with open(file, 'r') as f:
                txt = f.read()
        except UnicodeDecodeError:
            try:
                with open(file, 'r', encoding='gb2312') as f:
                    txt = f.read()
            except UnicodeDecodeError:
                if self.show_progress:
                    print('decode error, skipping: %s' % file)
                txt = ''
        return jieba.cut(txt)

    def get_from_list(self, file_list):
        word_list = []
        for f in file_list:
            if os.path.exists(f):
                if os.path.isdir(f):
                    l = map(lambda x: f + '/' + x, os.listdir(f))
                    w = self.get_from_list(l)
                    if w:
                        word_list += w
                    else:
                        return []
                elif f.endswith('.txt'):
                    word_list += self.get(f)
            else:
                if self.show_progress:
                    print('file "%s" does not exist' % f)
                return []
        return word_list

if __name__ == '__main__':
    pass
