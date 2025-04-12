#VERSION 3

"""file processes Word objects to and from Words
as well as csv file, and updates said information"""
import os
import csv
from new_Word import *
import ast



    #list_words takes Words object and converts Word to dict
    # then places into list to save to csv.

def list_words(words: "Words"):
    """Word to dict, dict(s) into list, expidites csv writing"""
    study_words_ = []
    for study_word in words.all:
        word = study_word.to_dict()
        study_words_.append(word)
    return study_words_



    #help_str_int does crucial reading of data 
    # from csv when list strings get touchy.

def help_str_int(string:str)->list:
    """any list strings from csv to lists"""
    try:
        result_list = ast.literal_eval(string)
    except Exception as e:
        return f"Error converting string to list: {e}"
    
    return result_list


def csv_file_exists(filename):
    """
    This function checks if a CSV file exists or not.
    :param filename: The name of the CSV file to check.
    :return: True if the file exists, False otherwise.
    """
    return os.path.exists(filename) and filename.endswith('.csv') 



    #read_word reads from csv file, takes a Words object
    # and turns ine into word, and appends to all.

def read_word(filename, lst: "Words"):
    """reads line in file converts to Word saves to Words.all"""
    if csv_file_exists(filename):
            
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            headers = reader.fieldnames

            for line in reader:
                morpheme = line['morpheme']
                pinyin = help_str_int(line['pinyin'])
                english = help_str_int(line['eng_sig'])
                sheng = help_str_int(line['tone'])
                grammar = line["grammar"]
                uni = line['unicode']
                clath = for_class(grammar)

                sr = help_str_int(line["score"])

                new = clath(morpheme, pinyin, english, sheng, unicode=uni, score=sr)
                # print(new.score)

                lst.append_main(new)#saving to .all
            return lst
    else:
        with open(filename, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['morpheme', 'grammar', 'unicode', 'pinyin', 'tone', 'eng_sig','score'])
            writer.writeheader()
            return lst


    #for_class assumes input is in pos, and returns the 
    #class Word that is its equivalent.

def for_class(grammar: str)->"Word":
        """checks in part of speech, returns Word"""
        pos = ["动词", "名词", "副词", "形容词", "量词","叹词", "成语", "数词", "连词",
        "介词", "代词", "助词", "助动词", "拟声词", "象声词", "专名词", "短语"]
        clas_eq = [Verb, Noun, Adverb, Adjective, Classifier, Interj, Idiom, Num, Conj,   
            Prep, Pronoun, AuxW, AuxV, Onomat, Onomat, PrNoun, Phrase]
        if grammar not in pos:
            return False
        g_idx = pos.index(grammar)
        word = clas_eq[g_idx]
        return word



    #save_updated_word rewrites a file with an 
    # updated score from practicing. from what I cam tell they are 
    # all still written in the same order.

def save_updated_word(words, filename):
    """rewrites a file with updated list of words"""
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['morpheme', 'grammar', 'unicode', 'pinyin', 'tone', 'eng_sig', 'score'])
        writer.writeheader()
        writer.writerows(words)



    #save_word used in new word writes a new word line
    # by line into csv file. 

def save_word(word, filename):
    """"""
    with open(filename, 'a', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['morpheme', 'grammar', 'unicode', 'pinyin', 'tone', 'eng_sig', 'score'])
        if f.tell() == 0:           #find out more about tell
            writer.writeheader()  
        writer.writerow(word.to_dict())



 