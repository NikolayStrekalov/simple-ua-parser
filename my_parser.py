# -*- coding: utf-8 -*-

from ua_parser import user_agent_parser

PLATFORM_WORDS = ['X11',
                  'Macintosh',
                  'Windows',
                  'compatible',
                  'Android',
                  'BlackBerry',
                  'Windows Phone',
                  'iPhone',
                  'iPad',
                  'iPod'
                  ]

BROWSER_WORDS = ['Safari',
                 'Opera',
                 'Firefox',
                 'Chrome',
                 'MSIE',
                 'Opera Mini',
                 'Opera Mobi',
                 'IEMobile'
                 ]

def _get_browser(brs):
    """
    По массиву, говорящему входит ли слово из BROWSER_WORDS в строку user-agetn,
    возвращает тип браузера.

    Порядок условий существенен.
    """
    if brs[7]:
        return 'IEMobile'
    elif brs[6]:
        return 'OperaMobile'
    elif brs[5]:
        return 'OperaMini'
    if brs[3]:
        return 'Chrome'
    elif brs[4]:
        return 'MSIE'
    elif brs[1]:
        return 'Opera'
    elif brs[2]:
        return 'Firefox'
    else:
        return 'Safari'

def parse(user_agent_str):
    """
    По строке user-agent возвращает словарь с указанием браузера и платформы.
    """
    platforms = [word in user_agent_str for word in PLATFORM_WORDS]
    browsers = [word in user_agent_str for word in BROWSER_WORDS]
    if not (any(browsers) and any(platforms)):
        ua = user_agent_parser.Parse(user_agent_str)
        return { 'browser' : ua['user_agent']['family'],
                 'platform' : ua['os']['family']
                }
    if platforms[9] or platforms[8] or platforms[7]:
        platform = 'iOS'
    elif platforms[6]:
        platform = 'WindowsPhone'
    elif platforms[5]:
        platform = 'BlackBerry'
    elif platforms[4]:
        platform = 'Android'
    elif platforms[2] or platforms[3]:
        platform = 'Windows'
    elif platforms[1]:
        platform = 'Mac'
    elif platforms[0]:
        platform = 'Linux'
    return { 'browser' : _get_browser(browsers),
             'platform': platform
           }

