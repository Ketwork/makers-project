def check_sentance_grammar(text):
    if text[0].isupper() and text[-1] in ".?!":
        return True
    else:
        return False