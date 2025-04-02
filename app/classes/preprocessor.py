import re

class Preprocessor:
    def __init__(self,language):

        if language in ["it", "en", "es"]:
            self.language = language
        else:
            self.language = "en"

    def clean_string(self,string):

       string = re.sub(r"[^A-Za-z 28]",'',string)      #Ho usato re.sub in modo che sostituisca con '' (perciò rimuova)
       return string                                               #qualsiasi carattere che non sia una lettera o uno spazio o i numeri 2 e 8
