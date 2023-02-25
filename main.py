# -*- coding: utf-8 -*-
"""
Getting information about the NFT cards
"""
import addpath
from simple_settings import settings

from common_modules.csv_w import write_csv
from common_modules.txt_r import read_txt
from common_modules.headline import print_headline
from common_modules.my_remove import remove_file

from functions.nft import get_nft_cards
from functions.format import formatPrice


__author__ = 'Vadim Arsenev'
__version__ = '1.0.0'
__data__ = '25.02.2023'


ORDER = list(map(lambda x: x.split(':')[0].strip(), \
    read_txt(settings.COLUMNS).split('\n')))


def nftCollectionItems(cards):
    """
    The main module for performing all operations of a request
       and writing to a file
    """
    print_headline(settings.RESULT_FILE[0], settings.COLUMNS, ORDER)
    for item in cards['data']['nftCollectionItems']['items']:
        # ***** Main query *****
        tokenId = item['index']
        playerName = item['name']
        cardNftAddress = item['address']
        cardNftFullAddress = f'{settings.COLLECTION_URL}/{cardNftAddress}'

        try:
            price = item['sale']['fullPrice']
        except KeyError:
            price = ''
        except TypeError:
            price = ''
        
        try:
            if item['rarityAttributes'][0]['traitType'] == 'Tier':
                cardTier = item['rarityAttributes'][0]['value']
                cardRarity = item['rarityAttributes'][1]['value']
            else:
                cardTier = item['rarityAttributes'][1]['value']
                cardRarity = item['rarityAttributes'][0]['value']
        except IndexError:
            cardTier = ''
            cardRarity = ''
          
        ownerName = item['owner']['name']
        ownerWallet = item['owner']['wallet']
        ownerWalletFull = f'{settings.WALLET_URL}/{ownerWallet}'

        price = formatPrice(price)

        # Data generation and writing to file
        data_nft_cards = {
            'tokenId': tokenId,
            'playerName': playerName,
            'cardNftAddress': cardNftAddress,
            'cardNftFullAddress': cardNftFullAddress,
            'price': price,
            'cardRarity': cardRarity,
            'cardTier': cardTier,
            'ownerName': ownerName,
            'ownerWallet': ownerWallet,
            'ownerWalletFull': ownerWalletFull,
        }

        write_csv(settings.RESULT_FILE[0], \
            data_nft_cards, ORDER)


def main():
    """
    Request information about the players. General request
    """
    nft_cards = get_nft_cards()
    nftCollectionItems(nft_cards)


if __name__ == '__main__':
    remove_file(settings.RESULT_FILE[0])
    main()
