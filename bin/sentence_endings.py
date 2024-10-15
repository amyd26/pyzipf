"""
Count amount of !,? and . in given file
"""

import argparse


def main(args):
    """Run the command line program."""
    text = args.infile.read()
    for punctuation in ['!','.','?']:
        punc_counts = text.count(punctuation)
        print(f'Number of {punctuation} is {punc_counts}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('infile', type=argparse.FileType('r'),
                        nargs='?', default='-',
                        help='Input file name')
    args = parser.parse_args()
    main(args)
    
    