#!/usr/bin/env python3
import argparse
import random

from conf import alphabet

DEBUG = True


if DEBUG:
    print('Welcome to Debug hell!')
    print(alphabet[random.randint(0,25)])


def parser():
    p = argparse.ArgumentParser()
    p.add_argument('dev', help='Dev')
    p.parse_args()


def ctx():
    p = parser()

if __name__ == '__main__':
    ctx()
