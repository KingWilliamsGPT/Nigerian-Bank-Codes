import string


def v(text):
    # used to make arbitrary strings into variable names
    pp = ''
    if text[0].isdigit():
        pp = '_'
    for i in text:
        if i not in string.ascii_letters+ ' ' + '0123456789':
            i = ' '
        if True:
            if pp and (pp[-1] == ' ' and i == ' '):
                continue
            pp += i
    return pp.strip().upper().replace(' ', '_')