from app.classes.preprocessor import Preprocessor


def main():
    preprocessor = Preprocessor("it")
    result = preprocessor.language
    print(result)

    result1 = preprocessor.clean_string("...C+òòèiao s0ono C1111arlo e ho 28 ann+++++++i")
    print(result1)

if __name__ == "__main__":
    main()