#VERSION 3

"""first file from process, asks new word
questions to make and save a Word"""
# i will keep old comments till their questions are solved

from new_Word import Word, Words
from saveload_func import save_word, for_class



yes = ["学","对","是","有","好","要", "行"]
no = ["不","哇", "没"]



    #place_word is the new word "main"
    # want to edit to automatically give input

def place_word(filename, f:"Words"):
    """new word 'main', appends created Word to 
    Words obect all and appends to csv"""
    # while True:       how to exit when you actually 
    # dont want to make a new word?? ^0^
    hanzi = new_word()

    if hanzi:
        if hanzi in f.char_exstnce:
            a = input(f"你已经输入了 '{hanzi}' 跟{f.char_exstnce[hanzi]}的意义，\n还要继续吗？\n")
            if any(i in no for i in a):
                print("OK吧\n")
                return False

        pos = part_speech()

        if any(i in f.morp_exstnce for i in hanzi):
            #print("repeat")
            data = morp_help(hanzi, f)
            if morp_q(data):
                br = morp_fill(hanzi, data) 
                r_py = br[0]
                r_sy = br[1]
            else:
                r_py = pinyin(hanzi)
                r_sy = sheng(hanzi)  
        else:
            r_py = pinyin(hanzi)
            r_sy = sheng(hanzi) 

        for idx in range(len(pos)): 
            eng_ys = english(hanzi, pos[idx][1])
            cl_word = pos[idx][0]
            temp_word = cl_word(hanzi, r_py, eng_ys, r_sy)
            temp_word.pinyin_unicode()
            print(temp_word)
            f.all.append(temp_word)
            save_word(temp_word, filename)


    
    # first function kaishi :') asks whether
    # or not user has learned a new word

def kaishi():
    """prompts if you want to start new word cycle"""
    word_q = input("你学会一组生词吗？\n")

    if len(word_q.strip()) == 0:
        return False
    elif any(ch in word_q for ch in no):
        return False
    elif any(ch in word_q for ch in yes):
        return True
    


    #new_word is step 1, asks how to 
    # spell (in characters) word

def new_word():
    """step 1 characters"""
    生词汇 = input("这组生词怎么写？\n")
    if 生词汇.strip() == "" or 生词汇.strip() == "exit":
        return False                            #What if its empty??!!!! FIX_ME!  
    else:
        print("好吧！\n")
        
        return 生词汇
    


    #pinyin is step 3, iterates though characters asks for
    #its pinyin equivalent. hopefully bypassed if char in "known"

def pinyin(sc:str)-> list[str]:
 
    print(f"\n这组生词有{len(sc)}个字,")
    pinyin = []
    for i in range(1, len(sc) + 1):
        py = input(f"第{i}个字的拼音怎么写？\n").strip()
        pinyin.append(py.lower())                       
    return pinyin



    #sheng is step 4, iterates though and obtains a list
    # of each char's tone 

def sheng(sc: str) -> list[int]:
    print(" ")
    sheng = []
    for i in range(1, len(sc) + 1):
        while True:  # Keep asking for input until valid
            try:
                sh = input(f"第{i}个字有什么声？\n")
                sh_value = int(sh.strip())
                if sh_value not in range(1, 6):  # Validate that the input is between 1 and 5
                    raise ValueError
                sheng.append(sh_value)
                break    # Exit the loop when valid input is received
            except ValueError:
                print("you can only input int values 1-5 or exit")
    
    return sheng



    #part_speech is step 2 asks for char part of 
    # speech and continues if there are more than one #HAS EXIT AS OPTION

def part_speech() -> list[tuple]:
    """asks new word for part of spech (step 2)"""
    first = input(f"你知道这组词有什么语法？\n")
    pos = []

    if for_class(first.strip()):
        pos.append((for_class(first.strip()), first.strip()))
        if first == "成语" or first == "短语":
            return pos
    else:
        print("\n可以说:\n名词(noun), 动词(verb), 形容词(adjective), "
              "副词(adverb), \n连词(conj.), 代词(pron.), 介词(prep.), 等等\n")

        if first == "exit":
            return "exit"
        
    next = input("还有其他语法吗？\n") 
    while for_class(next):
        pos.append((for_class(next.strip()), next))  #how to make sure no repeats
        next = input("还有其他语法吗？\n") 
    if len(pos) == 0:
        return "exit"
    return pos

        
      
# print(part_speech())
    #english is part 5, last question, adds a list of all 
    #english meaning entries related to given character

def english(word, pos:tuple)->list[str]:
    """uses char and pos to obtain list of english meanings"""
    eng = []
    first = input(f"\n作为{pos}, 这个词有什么英文意思？\n")
    fir = first.lower()
    eng.append(fir.strip())
    while True:
        next = input("有别的英文意思？\n")
        if any(i in next for i in no) or next.strip() == "":
            break
        else:
            n = next.lower()
            eng.append(n.strip())
    return eng



    #morp help function starts if prev used morphemes  
    # entered, and returns them w index in string

def morp_help(word:str, words:"Words"):
    other = []
    for idx, morp in enumerate(word):
        if morp in words.morp_exstnce:
            data = words.morp_exstnce[morp]
            info = (idx, morp, data[0], data[1])
            #print(info)
            other.append(info)
            #print(other)
      
    return other



    #morp_q asks if you want to reuse found morphemes
    
def morp_q(data):
    string = f"您之前说,\n"
    for item in data:
        #print(item)
        string += f"\t第{str(int(item[0])+1)}个字, {item[1]}, 有{item[3]}声调和{item[2]}拼音\n"
    
    string += "现在还是这样吗?\n"
    #print(string)

    yn = input(string)
    if any(i in no for i in yn):
        return False
    return True 




# def morp_fill(word: str, data: list):
#     tone = []
#     pin = []

#     for idx, ipt in enumerate(word):
#         # print(idx, "idx")
#         # print(data[0][0], "data[0][0]")
#         if len(data) != 0:
#             if idx == data[0][0]:
#                 var = data.pop(0)
#                 dra, hho, p, s = var
#                 tone.append(s)
#                 pin.append(p)
#             else:
#                 p = input(f"{ipt}的拼音是什么？\n")
#                 s = input(f"{ipt}的声调是什么？\n")
#                 pin.append(p)
#                 tone.append(int(s))
#         else:
#             p = input(f"{ipt}的拼音是什么？\n")
#             s = input(f"{ipt}的声调是什么？\n")
#             pin.append(p)
#             tone.append(int(s))
#     print(pin, tone)
#     return pin, tone

#what chat gpt made for men and what im gonna try out to see if it works

    #morp_fill takes the word and data from morp_help and
    # returns a tuple with pinyin and tone of complete word.

def morp_fill(word: str, data: list):
    tone = []
    pin = []

    def get_inputs(ipt):
        p = input(f"{ipt}的拼音是什么？\n")
        s = input(f"{ipt}的声调是什么？\n")
        return p, int(s)

    for idx, ipt in enumerate(word):
        if len(data) != 0 and idx == data[0][0]:
            _, _, p, s = data.pop(0)
        else:
            p, s = get_inputs(ipt)
        
        pin.append(p)
        tone.append(s)

    print(pin, tone)
    return pin, tone


               
