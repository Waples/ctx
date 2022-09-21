import re
from itertools import cycle
from conf import alpha_a, alpha_b, key_len, rotations, num
from termcolor import cprint

DEBUG = True
TEST = True
if TEST:
    MSG = 'Mijn code werkt gewoon!'
    KEY = '538'


def rotation_calc(input_key, rotor=1):
    """Returns a new key based on the rotations"""
    for r in range(0, int(key_len)):
        key = []
        for i in input_key:
            i = int(i)/int(key_len)
            i = round(i)
            key.append(i)
    return key


def converter(l, k, state):
    """
    Gets the corresponding number for the letter from the `alpha` dict, adds the
    number with the `k` value and returns the corresponding letter.
    """
    initial_value = alpha_a[l]
    if state == 'encrypt':
        new_value = initial_value + int(k)
        if new_value > num:
            new_value = new_value-num
            if DEBUG:
                cprint(f'converter ==> set to {new_value} == {alpha_b[new_value]}', 'yellow')
    if state == 'decrypt':
        new_value = initial_value - int(k)
        if new_value < 0:
            new_value = new_value+num
            if DEBUG:
                cprint(f'converter ==> set to {new_value} == {alpha_b[new_value]}', 'yellow')
    if DEBUG:
        cprint(f'\t{l} =---> {alpha_b[new_value]}', 'cyan')
    return alpha_b[new_value]


def sanitize(msg):
    m =  re.sub(' ' , '', msg.upper())
    ret = re.sub(r'[^\w]', '', m)
    if DEBUG:
        cprint(f'Sanitized: {ret}', 'blue')
    return ret


def encrypt(msg, key, state, rotor=rotations):
    tmp = []
    m = sanitize(msg)
    key = cycle(key)
    for l in m:
        k = next(key)
        tmp.append(converter(l, k, state))
    return ''.join(tmp)


def decrypt(msg, key, state, rotor=rotations):
    tmp = []
    key = cycle(key)
    for l in msg:
        k = next(key)
        tmp.append(converter(l, k, state))
    return ''.join(tmp)


if TEST:
    cprint(f'Initial msg: "{MSG}"', 'green')
    cprint(f'Key: {KEY}', 'green')
    e = encrypt(msg=MSG, key=KEY, rotor=0, state='encrypt')
    cprint(f'Encrypted output: {e}', 'white', 'on_red', attrs=['bold'])
    d = decrypt(msg=e, key=KEY, rotor=0, state='decrypt')
    cprint(f'Decrypted output: {d}', 'white', 'on_blue', attrs=['bold'])

    k = rotation_calc(input_key=KEY, rotor=2)
    cprint(f'New key: {k}, based on 2 rotations', 'yellow')
