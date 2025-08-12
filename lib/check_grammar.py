def check_grammar(string):
    if string != "":
        return string[-1] in ".?!" and string[0].isupper()
    raise Exception("I have nothing to check")