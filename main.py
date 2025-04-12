#VERSION 3

"""main runs system, is controller"""

from new_func import kaishi, place_word
from saveload_func import read_word
from new_Word import Words
from study_func import test_trial

w = Words()



    #main is the controller and starts the process

def main(filename):
    """consolidated"""
    words = read_word(filename, w)   
    words.make_charx()
    words.make_morphx()

    while kaishi():  
        place_word(filename, words)


    qu = input("好，你想做什么？\n")

    while qu != "":
        if any(i in ["练","学","习","复","预","考"] for i in qu):
            test_trial(words, filename)
            break




 
main("learnword.csv")
