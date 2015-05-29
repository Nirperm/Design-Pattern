import logging
from html_writer import HtmlWriter
from file_writer import FileWriter


class PageMaker():

    def make_welcome_page(self, mailaddr, filename):
        try:
            """
            mailprop = database.get_properties(maildata)
            username = mailprop.get_properties(mailaddr)
            writer = HtmlWriter(FileWriter(filename))
            writer.title('Welcome to ' + username + 'is page!')
            writer.paragraph(username + 'のページへようこそ。')
            writer.paragraph('メール待っていますね。')
            writer.mailto(mailaddr, username)
            writer.close()
            print(filename + 'is created for ' + mailaddr + ' ( ' + username + ' +')
        except IOError as e:
            logging.excepttion(e)
            """


