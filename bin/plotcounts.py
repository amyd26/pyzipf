"""Plots word count distribution"""

import argparse

import pandas as pd


def main(args):
    """Run the program."""
    input_csv = args.infile
    df = pd.read_csv(input_csv, header=None,
                    names=('word', 'word_frequency'))
    df['rank'] = df['word_frequency'].rank(ascending=False,
                                        method='max')
    df['inverse_rank'] = 1 / df['rank']
    ax = df.plot.scatter(x='word_frequency',
                            y='inverse_rank',
                            figsize=[12, 6],
                            grid=True, xlim = args.xlim)
    ax.figure.savefig(args.outfile)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('infile', type=argparse.FileType('r'),
                        nargs='?', default='-',
                        help='Input file name')
    parser.add_argument('--outfile', type=str, default='plotcounts.png',
                        help='Output file name')
    parser.add_argument('--xlim', type=float, nargs=2,
                        metavar=('XMIN', 'XMAX'),
                        default=None,
                        help='x-axis bounds')
    args = parser.parse_args()
    main(args)
    