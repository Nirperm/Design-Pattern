import sys
from winning_strategy import WinningStrategy
from prob_strategy import ProbStrategy
from player import Player
from hand import Hand


def main():
        if len(sys.argv) != 2:
            print('Check args size, does not work')
            print('usage: python main random_seed1 random_seed2')
            print('Example: python main.py 314 15')
        # FIXME args are over 3, raise IndexError due to Hand class zyankenn_list permit under 2
        seed1 = int(sys.argv[1])
        seed2 = int(sys.argv[2])
        player1 = Player('Taro', WinningStrategy(seed1))
        player2 = Player('Hana', ProbStrategy(seed2))
        for i in range(1, 10):  # 10000
            next_hand1 = player1.next_hand()
            next_hand2 = player2.next_hand()
            next_hand1 = Hand(next_hand1)
            next_hand2 = Hand(next_hand2)
            if next_hand1.is_stronger_than(next_hand2):
                print('Winner + ({0})'.format(player1))
                player1.win()
                player2.lose()
            elif next_hand2.is_stronger_than(next_hand1):
                print('Winner + ({0})'.format(player2))
                player1.lose()
                player2.win()
            else:
                print('Even')
                player1.even()
                player2.even()
        print('Total result:')
        print(player1.to_stirng())
        print(player2.to_stirng())

if __name__ == "__main__":
    main()
