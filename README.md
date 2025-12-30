# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

BookBot is a command-line tool that analyzes text files (books). It takes a file path as input and reports:
- Total word count
- Character frequency counts (a-z), sorted from most to least frequent

## Usage

```bash
python3 main.py <path_to_book>
```

## Example Output

```
============ BOOKBOT =============
analyzing book found at books/frankenstein.txt
--------- Word Count ----------
Found 78064 total words
------- Character Count -------
e: 45000
t: 28000
...
============ END =============
```
