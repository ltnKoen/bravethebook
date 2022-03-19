# bravethebook
Small tool to help design thematic variants and translations for "Brave the book", the bookmark game

## Example

    git clone https://github.com/ltnKoen/bravethebook/
    cd bravethebook
    python3 bravethebook_builder.py -v lettervalues_english.txt -w mythical_creatures_english.txt -o sorted_creatures_english.txt

Read files `lettervalues_english.txt` and `mythical_creatures_english.txt`, calculate a score for every creature in the list, and write the results to `sorted_creatures_english.txt`.

## Usage
    usage: bravethebook_builder.py [-h] [-v LETTERVALUES] [-w WORDS] [-s SEPARATOR]
                                   [-o OUTFILE]

    Score words from a list to help design a thematic variant for "Brave the Book",
    the bookmark game.

    options:
      -h, --help            show this help message and exit
      -v LETTERVALUES, --lettervalues LETTERVALUES
                            input file listing one letter and one lettervalue per
                            line
      -w WORDS, --words WORDS
                            input file listing all the words
      -s SEPARATOR, --separator SEPARATOR
                            ignore everything on the left of this character or string
                            in the words file
      -o OUTFILE, --outfile OUTFILE
                            output file to write the results to
