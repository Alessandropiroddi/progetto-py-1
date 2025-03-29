
class Preprocessor:
    def __init__(self,language):

        if language in ["it", "en", "es"]:
            self.language = language
        else:
            language = "en"

