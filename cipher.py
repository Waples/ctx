import re
from itertools import cycle
from conf import alpha_a, alpha_b, key_len, rotations, num
from termcolor import cprint

DEBUG = True
if DEBUG:
    MSG = 'Mijn code werkt gewoon!'
    KEY = '538'

def converter(l, k=1):
    """
    Gets the corresponding number for the letter from the `alpha` dict, adds the
    number with the `k` value and returns the corresponding letter.
    """
    initial_value = alpha_a[l]
    new_value = initial_value + int(k)
    if new_value > num:
        new_value = new_value-num
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


def encrypt(msg, key, rotor=rotations):
    tmp = []
    m = sanitize(msg)

    # FIXME
    #for _ in range(rotations):
    key = cycle(key)
    for l in m:
        k = next(key)
        tmp.append(converter(l, k))
    return ''.join(tmp)


def decrypt(key, rotor=rotations):
    pass


if DEBUG:
    cprint(f'Initial msg: "{MSG}"', 'green')
    cprint(f'Key: {KEY}', 'green')
    e = encrypt(msg=MSG, key=KEY, rotor=0)
    cprint(f'Encrypted output: {e}', 'white', 'on_green', attrs=['bold'])
