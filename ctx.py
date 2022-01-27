#!/usr/bin/env python3
import argparse
import cipher
import random


def parser():
    p = argparse.ArgumentParser()
    p.add_argument('-k', '--key', help='Cipher key.')
    p.add_argument('-m', '--message', help='Your message.')
    p.parse_args()


def ctx():
    p = parser()


if __name__ == '__main__':
    ctx()
