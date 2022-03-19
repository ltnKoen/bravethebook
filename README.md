# bravethebook
Small tool to help design thematic variants and translations for "Brave the book", the bookmark game

## Install
Make sure you have python3 installed, then run the following commands from the command file:

    git clone https://github.com/ltnKoen/bravethebook/
    cd bravethebook

## Examples
    python3 bravethebook_builder.py -v scrabble_english.txt -w creatures_english.txt -o creatures_english.txt

Read files `resources/scrabble_english.txt` and `resources/creatures_english.txt`, calculate a score for every creature in the list, and write the results to `results/creatures_english.txt`.

    python3 bravethebook_builder.py -s " - " -v scrabble_english.txt -w creatures_english.txt -o creatures_english.txt
Use `" - "` as a separator to ignore definitions: anything following `" - "` on a line in the list of words will be ignored.

## Usage
    usage: bravethebook_builder.py [-h] [-v LETTERVALUES] [-w WORDS] [-d DIRECTORY]
                                   [-s SEPARATOR] [--separator-whitespace] -o OUTFILE
                                   [--output-dir OUTPUT_DIR]

    Score words from a list to help design a thematic variant for "Brave the Book",
    the bookmark game.

    options:
      -h, --help            show this help message and exit
      -v LETTERVALUES, --lettervalues LETTERVALUES
                            input file listing one letter and one integer lettervalue
                            per line; frequent letters such as 'e' should have low
                            value (default: scrabble_english.txt)
      -w WORDS, --words WORDS
                            input file listing all the words (default:
                            creatures_english.txt)
      -d DIRECTORY, --directory DIRECTORY
                            directory where to look for the input files (default:
                            resources)
      -s SEPARATOR, --separator SEPARATOR
                            if this option is specified, ignore everything on the
                            left of this character or string in the words file.
                            useful if the words file contains definitions. (default:
                            None)
      --separator-whitespace, --first-word-only
                            if this option is specified, ignore everything in the
                            words file except the first word of each line (default:
                            False)
      -o OUTFILE, --outfile OUTFILE
                            output file to write the results to (default: None)
      --output-dir OUTPUT_DIR
                            directory where to write for the output files (default:
                            results)
