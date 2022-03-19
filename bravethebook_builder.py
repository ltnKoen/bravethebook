#!/usr/bin/env python3

def read_words(filename, separator=None):
    with open(filename, 'r') as f:
        return [
            line.split(separator, maxsplit=1)[0].strip().lower()
            for line in f if len(line) > 2
        ]

def write_words(filename, words):
    with open(filename, 'w') as f:
        f.write('\n'.join(words))

def read_lettervalues(filename):
    with open(filename, 'r') as f:
        return {
            row[0].strip().lower(): int(row[1].strip())
            for line in f
            if len(row := line.split()) >= 2
        }

def score_word(word, lettervalues):
    score_letter = lambda letter: lettervalues.get(letter, 0)
    return sum(map(score_letter, word))

def group_words_by_score(words, lettervalues):
    groups = {}
    for word in words:
        groups.setdefault(score_word(word, lettervalues), []).append(word)
    return groups

def write_groups(filename, groups):
    with open(filename, 'w') as f:
        for score, words in sorted(groups.items()):
            print(score, file=f)
            print('\n'.join(words), file=f)
            print(file=f)

import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Score words from a list to help design a thematic variant for "Brave the Book", the bookmark game.')
    parser.add_argument('-v', '--lettervalues',
        default='lettervalues_english.txt',
        help='input file listing one letter and one lettervalue per line')
    parser.add_argument('-w', '--words',
        default='mythical_creatures_english.txt',
        help='input file listing all the words')
    parser.add_argument('-s', '--separator',
        help='ignore everything on the left of this character or string in the words file')
    parser.add_argument('-o', '--outfile',
        default='sorted_creatures_english.txt',
        help='output file to write the results to')
    args = parser.parse_args()
    return args
    # parser.add_argument('-c', '--clean', action='store_true',
    #     help='if this option is specified, do not score the words; simply rewrite a clean list of words, removing empty lines and comments from the words file')

def main():
    arguments = parse_args()
    separator = arguments.separator
    wordsfile = arguments.words
    lettersfile = arguments.lettervalues
    groupsfile = arguments.outfile
    print('OPENING FILE:')
    print(wordsfile)
    print()
    words = read_words(wordsfile, separator=separator)
    print('READ WORDS:')
    print(words)
    print()
    print('OPENING FILE: ')
    print(lettersfile)
    print()
    lettervalues = read_lettervalues(lettersfile)
    print('READ VALUES:')
    print(lettervalues)
    print()
    groups = group_words_by_score(words, lettervalues)
    print('OPENING FILE: ')
    print(groupsfile)
    write_groups(groupsfile, groups)
    print()
    print('WRITTEN WORDS BY SCORE TO FILE: ', groupsfile)

if __name__ == '__main__':
    main()
