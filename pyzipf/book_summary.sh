# Get author information from a Project Gutenberg eBook.
# usage: bash book_summary.sh /path/to/file.txt what_to_look_for
head -n 17 $1 | tail -n 8 | grep $2


