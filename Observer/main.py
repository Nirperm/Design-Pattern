from digit_observer import DigitObserver
from graph_observer import GraphObserver
from random_number_generator import RandomNumberGenerator


def main():
    generator = RandomNumberGenerator()
    observer1 = DigitObserver()
    observer2 = GraphObserver()
    generator.add_observer(observer1)
    generator.add_observer(observer2)
    generator.execute()


if __name__ == "__main__":
    main()
