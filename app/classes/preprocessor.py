import re

class Preprocessor:
    def __init__(self,language):

        if language in ["it", "en", "es"]:
            self.language = language
        else:
            self.language = "en"

    def clean_string(self,string):

       string = re.sub(r"[^A-Za-z 28]",'',string)

       return string
