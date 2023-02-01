titleInput = input('Title: ')
authorInput = input('Author: ')
pagesInput = input('Page Count: ')
dateInput = input('Date Finished: ')

class Book:
    def __init__(self, title, author, pages, date):
        self.title = title
        self.author = author
        self.pages = pages
        self.date = date
    
    def write_info(self):
        with open('booksread.txt', 'a') as f:
             l = ['\n\t' + self.title + ' | ',
                    self.author + ' | ',
                    str(self.pages) + ' | ',
                    str(self.date) + ' | ']
             f.writelines(l)
             f.write('\n\t-----------------------------------------------------')
            
book = Book(titleInput, authorInput, pagesInput, dateInput)
book.write_info()