
__author__ = 'Vadim Arsenev'
__version__ = '1.0.0'
__data__ = '23.02.2023'


API_URL = 'https://api.getgems.io/graphql'

# for NFT cards only
COLUMNS = './settings/nft_cards.txt'
RESULT_FILE = ['./data/nft_cards.csv']

BODY_NFT_CARDS = \
"""
query {
  nftCollectionItems (address: "EQBpBsShOF1EvuX3nOKwNuzr5YWlJjdpCH_2n8ybizF479Tg", first: 7500) {
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