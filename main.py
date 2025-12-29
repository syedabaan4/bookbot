from stats import *
import sys

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
 
    path = sys.argv[1]
    num = count_words(get_book_text(path))
    print("============ BOOKBOT =============")
    print(f"analyzing book found at {path}")
    print("--------- Word Count ----------")
    print(f"Found {num} total words")
    print("------- Character Count -------")

    char_count = count_characters(get_book_text(path))    
    # print(char_count)
    final_list =  sort_dict(char_count)
    for item in final_list:
        char = item["char"]
        number = item["num"]
        print(f"{char}: {number}")

    print("============ END =============")

main()
