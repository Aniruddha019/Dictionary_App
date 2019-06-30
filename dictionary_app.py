import json
from difflib import get_close_matches
word_dictionary = []

def clean(word):
    word = word.rstrip()
    word = word.lower()
    return word

def found_any_matches_for(word):
    if len(get_close_matches(word,word_dictionary.keys())) > 0:
        return True
    return False

def user_affirmed_for(closest_match):
    user_input = input("Did you mean " + str(closest_match) +  " instead ?\nEnter Y for yes N for no : ")
    if(user_input is 'n'):
        return False
    return True

def translate(word):
    if word in word_dictionary:
        return word_dictionary[word]

    elif found_any_matches_for(word):
        closest_match = str(get_close_matches(word,word_dictionary.keys())[0])
        if user_affirmed_for(closest_match):
            return word_dictionary[closest_match]
        else:
            print("Sorry the word is not recognized..")

    else:
        print("That is not a word.Please double check it .. ")

    return None

def read_json():
    file_handle = open("data.json")
    data = json.load(file_handle)
    return data

def print_meaning(meanings_of_word):
    if(meanings_of_word):
        for num,meaning in enumerate(meanings_of_word,start = 1):
            print("Meaning " + str(num) + " : " + meaning)

word_dictionary = read_json()
word_to_search = input("Enter a word : ")
cleaned_word = clean(word_to_search)
meanings_of_word  =  translate(cleaned_word)
print_meaning(meanings_of_word)
