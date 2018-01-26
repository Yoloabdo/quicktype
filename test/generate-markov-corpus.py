#!/usr/bin/env python

import random

with open('/usr/share/dict/words') as f:
    words = f.read().splitlines()

with open('acronyms.txt') as f:
    acronyms = f.read().splitlines()

def all_lower([word, _]):
    return word.lower()

def all_upper([word, _]):
    return word.upper()

def capitalize([word, _]):
    return word[:1].upper() + word[1:].lower()

def cap_and_upper_acro(w):
    [word, is_acro] = w
    if is_acro:
        return all_upper(w)
    else:
        return capitalize(w)

def choice(items):
    total = sum([n for [n, _] in items])
    x = random.random()
    s = 0
    for [n, item] in items:
        s += n
        if x <= s / total:
            return item
    raise Exception()

formats = [
    [3, [all_lower, all_lower, "_"]],
    [1, [all_upper, all_upper, "-"]],
    [1, [all_lower, all_lower, " "]],
    [5, [all_lower, capitalize, ""]],
    [5, [all_lower, cap_and_upper_acro, ""]]
]

prefixes = [
    [10, ""],
    [1, "_"]
]
