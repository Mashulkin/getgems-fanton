
__author__ = 'Vadim Arsenev'
__version__ = '1.0.2'
__data__ = '26.02.2023'


API_URL = 'https://api.getgems.io/graphql'
COLLECTION_URL = 'https://getgems.io/collection/EQBpBsShOF1EvuX3nOKwNuzr5YWlJjdpCH_2n8ybizF479Tg'
WALLET_URL = 'https://getgems.io/user'

# for NFT cards only
COLUMNS = './settings/nft_cards.txt'
RESULT_FILE = ['./data/nft_cards1.csv', './data/nft_cards2.csv', './data/nft_cards3.csv']
MAX_ROW = 5000

BODY_NFT_CARDS = \
"""
query {
  nftCollectionItems (address: "EQBpBsShOF1EvuX3nOKwNuzr5YWlJjdpCH_2n8ybizF479Tg", first: 15000) {
    items {
      name
      address
      index
      sale {
        ... on NftSaleFixPrice {
          fullPrice
        }
      }
      rarityAttributes {
        traitType
        value
      }
      owner {
        name
        wallet
        socialLinks {
          url
        }
        description
      }
    }
  }
}
"""

BODY_NFT_USERS = \
"""
query {
  ownerStatsNftCollection (collectionAddress: "EQBpBsShOF1EvuX3nOKwNuzr5YWlJjdpCH_2n8ybizF479Tg", first: 100000) {
    items {
      ownerUser {
        name
        wallet
        socialLinks {
          url
        }
        description
      }
    }
  }
}
"""
