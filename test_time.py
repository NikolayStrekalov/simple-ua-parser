#!/usr/bin/env python
# -*- coding: utf-8 -*-

import timeit

from ua_parser.user_agent_parser import Parse
from my_parser import parse

FILES = ['test_desktop_ua.txt',
          'test_mobile_ua.txt',
          'samples.txt'
         ]

def test1():
    """
    Тест показывает во сколько раз собственная функция (my_parser.parse)
    работает быстрее "коробочного" парсера (ua_parser.user_agent_parser.Parse)
    на примерах из первого файла из списка FILES
    """
    f = open(FILES[0], 'r')
    number = 10 ** 3
    count = 0
    summa = 0
    for line in f.readlines():
        if line[0] == '#':
            continue
        line = line.strip()
        my_parser = timeit.timeit(setup="from my_parser import parse; s='" + line + "'",
                                  stmt="parse(s)", number = number)
        default_parser = timeit.timeit(setup="from ua_parser.user_agent_parser import Parse; s='" + line + "'",
                                  stmt="Parse(s)", number = number)
        count += 1
        summa += default_parser / my_parser
    print "custom parser is " + str(summa / count) +\
          " times faster on most common examples"
    f.close()

if __name__ == '__main__':
    test1()

