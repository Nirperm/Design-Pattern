import logging
from html_writer import HtmlWriter
from database import Database


class PageMaker():

    def make_welcome_page(self, mailaddr, filename):
        db = Database()
        try:
            user_name = db.get_properties('maildata')
            writer = HtmlWriter(open(filename, mode='w'))
            writer.title('Welcome to ' + user_name + 'is page!')
            writer.paragraph(user_name + 'のページへようこそ。')
            writer.paragraph('メール待っていますね。')
            writer.mailto(mailaddr, user_name)
            writer.close()
            print(filename + ' ' + 'is created for' + mailaddr + ' ' + '(' + user_name + ')')
        except IOError as e:
            logging.exception(e)
