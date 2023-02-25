# -*- coding: utf-8 -*-
"""
Additional requests
"""
from simple_settings import settings
from common_modules.parser import ParserPost


__author__ = 'Vadim Arsenev'
__version__ = '1.0.0'
__data__ = '23.02.2023'


def get_nft_cards():
    payload = settings.BODY_NFT_CARDS
    requests_data = ParserPost(settings.API_URL, payload)
    cards = requests_data.parser_graphql_result()

    return cards
