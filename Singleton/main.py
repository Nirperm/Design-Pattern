from singleton import Singleton


def main():
    s1 = Singleton('aaa')
    s2 = Singleton('bbb')
    if s1 is s2:
        print(id(s1), id(s2))
        print(s1.get_name())
        print(s2.get_name())
    else:
        print('s1 is NOT s2')


if __name__ == '__main__':
    main()
