import article, argparse

__usage = '''
automatic article generator by MaxXing
based on jieba and Hidden Markov Model (HMM)
version 0.0.1

usage:
    article_gen [file ...] [options]

options:
    -s=seed         specify a random seed (unsigned integer)
    -len=length     specify the length of article
    -d=dump         dump the word data from input file
    -l=dump         load word data from dump file and ignore input files
    -p              print progress information while scanning file
    -sep            add separators between every two words
    -u              use uniform distribution model instead of HMM
'''

def main():
    # initialize parser
    parser = argparse.ArgumentParser()
    parser.parse()
    if not parser.file_list and not parser.dump_file:
        print(__usage.strip('\n'))
        exit(0)

    # initialize generator
    gen = article.ArticleGen(
            dump_file=parser.dump_file,
            show_progress=parser.show_progress,
            separator=parser.separator,
            use_weight=parser.use_weight)

    # generate seed
    if parser.seed > -1:
        s = gen.new_seed(parser.seed)
    else:
        s = gen.seed()
    print('seed:', s)

    # load data
    if parser.load_dump:
        gen.load_dump()
    else:
        if not gen.load(parser.file_list):
            print('cannot read word from input files')
            exit(1)
        gen.dump()

    # generate article
    text = gen.generate(parser.length if parser.length else 0)
    print(text)

if __name__ == '__main__':
    main()
