#VERSION 3

"""Word and Words object"""

import unicodedata



class Words:
    def __init__(self):
        self.all = []
        self.wellknown = []
        self.char_exstnce = {}
        self.morp_exstnce = {}


    def __str__(self):
        return ''.join([str(i) + "\n" for i in self.all])
    
    def __repr__(self) -> str:
        return str(self.all)

    def append_main(self, word):
        self.all.append(word)
    
    def find(self, hanzi)->bool:
        for item in self.all:
            print(item)
            if hanzi == item.m:
                return True
        return False   

    def make_charx(self):

        for item in self.all:
            a = self.char_exstnce
            if item.m in a:
                a[item.m].append(item)
            else:
                a[item.m] = [item]

    def make_morphx(self):

        for item in self.all:
            for idx in range(len(item.m)):
                morp = item.m[idx]
                if morp not in self.morp_exstnce:
                    self.morp_exstnce[morp] = (item.py[idx], item.sh[idx])


                




    
    #def


class Word:

    def __init__(self, morpheme: str, pinyin: str, eng_sig: list[str], sh_yin: list[str], unicode = "", score = [0.0]): #idv_py: list[str]
        self.m = morpheme
        self.py = pinyin
        self.yw = eng_sig
        self.sh = sh_yin
        self.py_uu = unicode
        self._rate = score
        self.grammar = ""


    def pinyin_unicode(self):
        pinyin = self.py
        tone = self.sh
        full = ""
        
        for idx, a_string in enumerate(pinyin):

            pos = which_vowel(a_string)
            if pos == len(a_string):
                beg = a_string[:pos]
                vow = a_string[pos:pos+1]
                end = ""
            elif pos == 0:
                vow = a_string[0]
                #print(vow)
                end = a_string[1:]
                #print(end)
                beg = ""
            else:
                beg = a_string[:pos]
                end = a_string[pos+1:]
                vow = a_string[pos:pos+1]
            v = find_char(vow, tone[idx])

            full += beg + v + end
        self.py_uu = unicodedata.normalize('NFC', full)


    @property
    def score(self):
        return self._rate
    
    # @score.setter                         # I still dont really get this at all.
    # def append(self, score):
    #     return self._rate.append(score)
    

    def upd_score(self, test: bool):
        if test:
            self.score.append(1.0)
        else:
            self.score.append(0.0)
    
    def new_score(self):
        tot = len(self._rate)

        lot = sum(i for i in self._rate)
        # print(lot, "/", tot)
        return f"{round((lot/tot*100), 2)} %"


    def to_dict(self):
        return {
            'morpheme': self.m,
            'grammar': self.grammar,
            'unicode' : self.py_uu,
            'pinyin': self.py,
            'tone': self.sh,
            'eng_sig': self.yw,
            'score': self._rate
        }

    def __str__(self):
        return f"({self.grammar}) {self.m} - {self.py_uu} - {self.yw}"
    
    def __repr__(self):
        return f"({self.grammar}){self.m} - {self.py_uu}"



class Verb(Word):
    def __init__(self, morpheme: str, pinyin: str, eng_sig: list[str], sh_yin: list[str], unicode = "", score = [0.0]):
        super().__init__( morpheme, pinyin, eng_sig, sh_yin, unicode, score)
        self.grammar = "动词"

    def __str__(self):
        return super().__str__()  
        
    def __repr__(self):
        return super().__repr__()  


class Adverb(Word):
    def __init__(self, morpheme: str, pinyin: str, eng_sig: list[str], sh_yin: list[str], unicode = "", score = [0.0]): 
        super().__init__( morpheme, pinyin, eng_sig, sh_yin, unicode, score)
        self.grammar = "副词"

    def __str__(self):
        return super().__str__()  
        
    def __repr__(self):
        return super().__repr__()  


class Adjective(Word):
    def __init__(self, morpheme: str, pinyin: str, eng_sig: list[str], sh_yin: list[str], unicode = "", score = [0.0]): 
        super().__init__( morpheme, pinyin, eng_sig, sh_yin, unicode, score)
        self.grammar = "形容词"

    def __str__(self):
        return super().__str__()  
        
    def __repr__(self):
        return super().__repr__()  


class Noun(Word):
    def __init__(self, morpheme: str, pinyin: str, eng_sig: list[str], sh_yin: list[str], unicode = "", score = [0.0]): 
        super().__init__( morpheme, pinyin, eng_sig, sh_yin, unicode, score)
        self.grammar = "名词"

class Idiom(Word):
    def __init__(self, morpheme: str, pinyin: str, eng_sig: list[str], sh_yin: list[str], unicode = "", score = [0.0]):
        super().__init__( morpheme, pinyin, eng_sig, sh_yin, unicode, score)
        self.grammar = "成语"

    def __str__(self):
        return super().__str__()  
        
    def __repr__(self):
        return super().__repr__()  

      
class Classifier(Word):
    def __init__(self, morpheme: str, pinyin: str, eng_sig: list[str], sh_yin: list[str], unicode = "", score = [0.0]):
        super().__init__(morpheme, pinyin, eng_sig, sh_yin, unicode, score) 
        self.grammar = "量词"

    def __str__(self):
        return super().__str__()  
        
    def __repr__(self):
        return super().__repr__()  


class Conj(Word):
    def __init__(self, morpheme: str, pinyin: str, eng_sig: list[str], sh_yin: list[str], unicode = "", score = [0.0]):
        super().__init__(morpheme, pinyin, eng_sig, sh_yin, unicode, score)
        self.grammar = "连词"

    def __str__(self):
        return super().__str__()  
        
    def __repr__(self):
        return super().__repr__()  


class Interj(Word):
    def __init__(self, morpheme: str, pinyin: str, eng_sig: list[str], sh_yin: list[str], unicode = "", score = [0.0]):
        super().__init__(self, morpheme, pinyin, eng_sig, sh_yin, unicode, score)
        self.grammar = "叹词" 

    def __str__(self):
        return super().__str__()  
        
    def __repr__(self):
        return super().__repr__()  


class Num(Word):
    def __init__(self, morpheme: str, pinyin: str, eng_sig: list[str], sh_yin: list[str], unicode = "", score = [0.0]):
        super().__init__( morpheme, pinyin, eng_sig, sh_yin, unicode, score) 
        self.grammar = "数词"

    def __str__(self):
        return super().__str__()  
        
    def __repr__(self):
        return super().__repr__()  


class Pronoun(Word):
    def __init__(self, morpheme: str, pinyin: str, eng_sig: list[str], sh_yin: list[str], unicode = "", score = [0.0]):
        super().__init__( morpheme, pinyin, eng_sig, sh_yin, unicode, score) 
        self.grammar = "代词"

    def __str__(self):
        return super().__str__()  
        
    def __repr__(self):
        return super().__repr__()  


class Prep(Word):
    def __init__(self, morpheme: str, pinyin: str, eng_sig: list[str], sh_yin: list[str], unicode = "", score = [0.0]):
        super().__init__( morpheme, pinyin, eng_sig, sh_yin, unicode, score) 
        self.grammar = "介词"

    def __str__(self):
        return super().__str__()  
        
    def __repr__(self):
        return super().__repr__()  


class Onomat(Word):
    def __init__(self, morpheme: str, pinyin: str, eng_sig: list[str], sh_yin: list[str], unicode = "", score = [0.0]):
        super().__init__( morpheme, pinyin, eng_sig, sh_yin, unicode, score)
        self.grammar = "象声词"

    def __str__(self):
        return super().__str__()  
        
    def __repr__(self):
        return super().__repr__()  


class AuxW(Word):
    def __init__(self, morpheme: str, pinyin: str, eng_sig: list[str], sh_yin: list[str], unicode = "", score = [0.0]):
        super().__init__( morpheme, pinyin, eng_sig, sh_yin)
        self.grammar = "助词"

    def __str__(self):
        return super().__str__()  
        
    def __repr__(self):
        return super().__repr__()  


class AuxV(Word):
    def __init__(self, morpheme: str, pinyin: str, eng_sig: list[str], sh_yin: list[str], unicode = "", score = [0.0]):
        super().__init__( morpheme, pinyin, eng_sig, sh_yin, unicode, score) 
        self.grammar = "助动词"

    def __str__(self):
        return super().__str__()  
        
    def __repr__(self):
        return super().__repr__()  

class Phrase(Word):
    def __init__(self, morpheme: str, pinyin: str, eng_sig: list[str], sh_yin: list[str], unicode = "", score = [0.0]):
        super().__init__( morpheme, pinyin, eng_sig, sh_yin, unicode, score) 
        self.grammar = "短语"

    def __str__(self):
        return super().__str__()  
        
    def __repr__(self):
        return super().__repr__()


class PrNoun(Word):
    def __init__(self, morpheme: str, pinyin: str, eng_sig: list[str], sh_yin: list[str], unicode = "", score = [0.0]):
        super().__init__( morpheme, pinyin, eng_sig, sh_yin, unicode, score) 
        self.grammar = "专名词"

    def __str__(self):
        return super().__str__()  
        
    def __repr__(self):
        return super().__repr__()  



def which_vowel(string:str):

    if "a" in string:
        return(string.index("a"))
    elif "o" in string:
        return(string.index("o"))  
    elif "e" in string:
        return(string.index("e"))
    elif "i" in string:
        return(string.index("i")) 
    elif "u" in string:
        return(string.index("u"))  
    elif "v" in string:
        return(string.index("v"))
    else:
        return -1
                    
def find_char(vowel: str, tone: int) -> str:
    tones = {
        'a': [257, 225, 462, 224],
        'e': [275, 233, 283, 232],
        'i': [299, 237, 464, 236],
        'o': [333, 243, 466, 242],
        'u': [363, 250, 468, 249],
        'v': [470, 472, 474, 476]
    }
    #base_ord = ord(vowel)
    if vowel in tones:
        if 1 <= tone <= 4:
            return chr(tones[vowel][tone - 1])
        else:
            return vowel
    return vowel



# y = Verb( "要", ["yao"], ["to want"], [2])
# print(y)
# y.upd_score(True)

# print(y.new_score())
