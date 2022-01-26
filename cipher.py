import re
from conf import alpha, key_len, rotations, num

DEBUG = True

def cnt(cipher, number):
    ret = number+cipher
    if ret > 25:
        print('ERROR')
    return res

def conv_num(l, k=1):
    """Returns a number for given letter"""
    i = alpha[l]
    i = i + k
    return i

def conv_let(x):
    """convert value of V to a letter"""
    for k, v in alpha:
        if v == x:
            return k


def encrypt(msg, key, rotor=rotations):
    # convert to uppercase
    m =  re.sub(' ' , '', msg.upper())
    for l in m:
        l = conv_num(l)
        ret = conv_let(l)
        print(ret)

def decrypt(key, rotor=rotations):
    pass

if DEBUG:
    encrypt(msg='hello world', key=538, rotor=0)
