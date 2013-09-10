#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from ua_parser import user_agent_parser
from my_parser import parse


class TestUA(object):

    ua_samples = ''
    platform = ''
    browser = ''

    def test_uas(self):
        f = open(self.ua_samples)

        for line in f.readlines():
            if line[0] == '#':
                self.platform, self.browser = line[1:].strip().split()
            else:
                ua = parse(line)
                self.assertEqual(ua['platform'], self.platform,
                                 msg = ' ' .join([self.platform, 'expected,',
                                                  ua['platform'], 'parsed'])
                        )
                self.assertEqual(ua['browser'], self.browser,
                                 msg = ' ' .join([self.browser, 'expected,',
                                                  ua['browser'], 'parsed'])
                        )
        f.close()

class TestDesktopUA(unittest.TestCase, TestUA):
    ua_samples = 'test_desktop_ua.txt'

class TestMobileUA(unittest.TestCase, TestUA):
    ua_samples = 'test_mobile_ua.txt'

if __name__ == '__main__':
    unittest.main()

