import sys

class ArgumentParser(object):
    def __init__(self):
        self.file_list = []
        self.seed = -1
        self.length = 0
        self.dump_file = ''
        self.load_dump = False
        self.show_progress = False
        self.separator = ''
        self.use_weight = True

    def parse(self):
        args = sys.argv
        args.pop(0)
        self.__init__()
        for i in args:
            if i.startswith('-s='):
                self.seed = int(i[len('-s='):])
            elif i.startswith('-len='):
                self.length = int(i[len('-len='):])
            elif i.startswith('-d='):
                self.dump_file = i[len('-d='):]
                self.load_dump = False
            elif i.startswith('-l='):
                self.dump_file = i[len('-l='):]
                self.load_dump = True
            elif i == '-p':
                self.show_progress = True
            elif i == '-sep':
                self.separator = ' '
            elif i == '-u':
                self.use_weight = False
            else:
                self.file_list.append(i)
