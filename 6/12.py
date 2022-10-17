# -*- coding: utf-8 -*-

import re
from string import punctuation


def find_i_words(string):
    string = re.sub(f'[{re.escape(punctuation)}]', '', string)
    return len(
        list(filter(lambda word: word.endswith('я'), list(string.split(' ')))))


print(find_i_words(input('Your string: ')))
