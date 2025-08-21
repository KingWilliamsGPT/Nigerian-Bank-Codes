import string
import json


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


def save_dict(d, f_name):
    with open(f_name, 'w') as f:
        f.write(json.dumps(d))


def paystack_save_dict(d: dict, f_name: str):
     data = d['data']
     k = {}
     for bank in data:
         k[bank['id']] = {
             'bank_name': bank['name'],
             'label': v(bank['name']),
             'paystack_exact_data': bank
         }
     save_dict(k, f_name)