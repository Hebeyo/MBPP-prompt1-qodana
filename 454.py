import re
def text_match_wordz(text):
    patterns = '\w*z.\w*'
    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return('Not matched!')
