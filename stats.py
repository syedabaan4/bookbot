import string

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def count_words(text):
    word_list = text.split()
    count = len(word_list) 
    return count

def count_characters(text):
    stripped = text.strip(" ")
    lower_case = stripped.lower()

    # create an array of all characters
    alphabet_list = list(string.ascii_lowercase)
        
    # create empty dict
    counts = {}

    # for each char in array (key) count occurences (value)
    for i in alphabet_list:
        counts[i] = lower_case.count(f"{i}")

    return counts

def sort_on(items):
    return items["num"]

def sort_dict(dictionary):
    dict_list = []

    for key, value in dictionary.items():
        new_dict = {}
        new_dict["char"] = key
        new_dict["num"] = value
        dict_list.append(new_dict)

    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
