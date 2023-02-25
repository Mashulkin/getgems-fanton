# -*- coding: utf-8 -*-
"""
Real player position formatting
"""


__author__ = 'Vadim Arsenev'
__version__ = '1.0.0'
__data__ = '23.02.2023'


def formatPrice(price):
    try:
        price = '{:.2f}'.format(float(price) / 1000000000)
    except TypeError:
        price = ''
    except ValueError:
        price = ''
    
    return price
