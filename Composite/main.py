import logging
from directory import Directory
from file_treatment_exception import FileTreatmentException
from my_file import MyFile


if __name__ == "__main__":
    try:
        print('Making root entries')
        rootdir = Directory('root')
        bindir = Directory('bin')
        tmpdir = Directory('tmp')
        usrdir = Directory('usr')
        rootdir.add(bindir)
        rootdir.add(tmpdir)
        rootdir.add(usrdir)
        bindir.add(MyFile('vi', 10000))
        bindir.add(MyFile('latex', 20000))
        rootdir.print_list()

        print('')
        print('Making user entries')
        yuki = Directory('yuki')
        hanako = Directory('hanako')
        tomura = Directory('tomura')
        usrdir.add(yuki)
        usrdir.add(hanako)
        yuki.add(MyFile('diary.html', 100))
        yuki.add(MyFile('Composite.py', 200))
        hanako.add(MyFile('memo.txt', 300))
        tomura.add(MyFile('game.doc', 400))
        tomura.add(MyFile('junk.mail', 500))
        rootdir.print_list()
    except FileTreatmentException as e:
        logging.exception('FileTreatmentException: {0}'.format(e))
