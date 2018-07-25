__version__ = '0.0.2'
__license__ = 'MIT'

def main():
    import article, argparse

    # initialize parser
    parser = argparse.ArgumentParser(prog='article_gen')
    parser.formatter_class = argparse.RawTextHelpFormatter
    parser.description = 'automatic article generator by MaxXing\n' + \
                         'based on jieba and Hidden Markov Model (HMM)'
    parser.add_argument('file', metavar='FILE', nargs='*',
                        help='list of text files or directories')
    parser.add_argument('-s', '--seed', default=-1, type=int,
                        help='specify a random seed (unsigned integer)')
    parser.add_argument('-len', '--length', default=0, type=int,
                        help='specify the length of article')
    parser.add_argument('-d', '--dump', default='',
                        help='dump the word data from input file')
    parser.add_argument('-l', '--load', default='',
                        help='load word data from dump file')
    parser.add_argument('-pp', '--proportion', default=0.5, type=float,
                        help='set the proportion of impact of POS')
    parser.add_argument('-p', '--print', action='store_true',
                        help='print progress information while scanning file')
    parser.add_argument('-sep', '--separator', action='store_const',
                        const=' ', default='',
                        help='add separators between every two words')
    parser.add_argument('-u', '--uniform', action='store_true',
                        help='use uniform distribution model instead of HMM')
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s ' + __version__)

    # parse arguments
    args = parser.parse_args()
    if not args.file and not args.load:
        parser.print_help()
        exit(0)

    # initialize generator
    gen = article.ArticleGen(
            show_progress=args.print,
            separator=args.separator,
            use_weight=not args.uniform,
            pos_prop=args.proportion)

    # generate seed
    if args.seed > -1:
        s = gen.new_seed(args.seed)
    else:
        s = gen.seed()
    print('seed:', s)

    # load data
    if args.load:
        gen.dump_file = args.load
        if not gen.load_dump():
            parser.error('cannot read word from dump')
    else:
        if not gen.load(args.file):
            parser.error('cannot read word from input files')
        if args.dump:
            gen.dump_file = args.dump
            gen.dump()

    # generate article
    text = gen.generate(args.length)
    print(text)
