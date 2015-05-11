# from Framework import factory as Factory
# from Framework import product as Product
from IDCard import id_card_factory as IDCardFactory
# from IDCard import idcard as IDCard


if __name__ == '__main__':
    factory = IDCardFactory()
    card1 = factory.create('結城浩')
    card2 = factory.create('とむら')
    card3 = factory.create('佐藤花子')

    card1.use()
    card2.use()
    card3.use()
