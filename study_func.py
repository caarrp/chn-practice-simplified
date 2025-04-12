#VERSION 3

"""this file for fucntions dedicated to 
the practice and repitive study of word 
sets, creation of word sets"""

from new_Word import Words, Word
import random
from saveload_func import save_updated_word, list_words
   


    #First iteration test_trial, uses random to bounce between py/sh-y and eng_sig practice
    #critiques, there ere still unpracticed words, que devlp. could be better

def test_trial(l: "Words", filename):
    """study format, random either english, or tones and pinyin.
    random choce from all words, can be adjusted manually"""
    while True:
        t_count = len(l.all)
        r_idx = random.choice(range(t_count))
        either = random.random() 
        rand_word = l.all[r_idx] 
        if either < .5:
            #pinyin study
            ans = py_study(rand_word)
            if ans == 'exit':
                save_updated_word(list_words(l), filename)
                break
            print(f"{ans}{"!" if ans == True else ''}")
            
            rand_word.upd_score(ans)
            print(rand_word.score, rand_word.new_score())

        elif either >= .5:
            #english study
            ans = eng_study(rand_word)
            if ans == 'exit':
                save_updated_word(list_words(l), filename)
                break
            print(f"{ans}{"!" if ans == True else ''}")
            rand_word.upd_score(ans)

            print(rand_word.score, rand_word.new_score())  #龙角散



    #py_study assists test trial with py/tone cycle

def py_study(word: "Word")-> bool:
    """gives Word py tone in test format"""
    base = word.m
    py = word.py
    tone = word.sh
    ans = True
    for i in range(len(base)):
        answr_1 = input(f"{base},\n'{base[i]}' 有什么拼音?\n")
        print(f"{ans}{"!" if i == py[i] else ''}")
        print(f"\nThe correct answer is '{py[i]}',\n")
        if answr_1.strip().lower() == "q":
            print("exiting")
            return "exit"

        elif  answr_1.strip().lower() != py[i]:
            ans = False

        answr_2 = input("声音吗？\n")
        print(f"{ans}{"!" if i == tone[i] else ''}")
        print(f"\nThe correct answer is '{tone[i]}',\n")
        try:
            if answr_2.strip().lower() == "q":
                print("trying to exit")
                return "exit"
            
            elif int(answr_2.strip()) != int(tone[i]):
                ans = False

        except:
            print(ValueError("you can only input int values 1-5 or exit"))
            return False
    return ans



    #eng_study assists test trial with py/tone cycle
    
def eng_study(word:"Word")-> bool:
    """gives Word english meaning in test format"""

    base = word.m
    eng = word.yw
    
    ans = False
    answr = input(f"为了{word.grammar}, '{base}' ,\n有什么英文意思?\n")
    if answr.strip().lower() == "exit":
            print("trying to exit")
            return "exit"

    elif any(i in answr.strip() for i in eng):                                   
        ans = True                                                              

    print(f"{ans}{"!" if ans == True else ''}")
    print(f"\nThe correct answers are {eng},\n")
    return ans

    