
import re
import json

class Preprocessor:
    def __init__(self,language):
        if language in ["it", "en", "es"]:
            self.language = language
        else:
            self.language = "en"

# ISSUE 1
    def clean_string(self, string):

       string = re.sub(r"[^A-Za-z 28]",'',string)      #Ho usato re.sub in modo che sostituisca con '' (perciò rimuova)
       return string                                               #qualsiasi carattere che non sia una lettera o uno spazio o i numeri 2 e 8


#ISSUE 2
#Creare un metodo della classe Preprocessor che prenda in ingresso una stringa e la "ripulisca" dalle stopwords. Le stopwords saranno all'interno di un set. In base alla lingua bisogna selezionare le stopwords corrette.

    def clean_stopwords(self,string) :
         with open(f"app/classes/stopwords/{self.language}.json", 'r', encoding = "utf-8") as f:         #apro il file json in lettura, uso "with ...as f" in modo che si chiuda automaticamente, e uso "f" prima del path in modo che venga letto valore di "self.language" in tempo reale
             stopw = json.load (f)                                                                       #carico il file, che è una lista, nella variabile stopwords
         words = string.split()                                                                          #creo una lista "words" con le parole della stringa
         words_lower = (w.lower() for w in words if w != "IE")                                           #creo una lista "words_lower" con le parole di words in minuscolo tranne "IE", in modo da poterle confrontare con le stopwords

         clean_words = (w for w_l,w in zip(words_lower,words) if w_l not in stopw)                       #creo una lista uguale a words, tranne per le stopwords, che vengono trovate confrontando "words_lower" con "stopw"
         new_string = " ".join(clean_words)                                                              #riassemblo le parole in "new_string"

         return new_string