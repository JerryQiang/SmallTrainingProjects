# 馆藏目录——创建一个图书类，记录书名、页数、国际标准书号、是否借出。用它来管理各种书籍，允许用户进行借出和归还操作。
# 复杂一点的话，可以生成逾期图书和逾期费用的报告。也可以让用户进行预约操作。
class book(object):
    def __init__(self,name,pages,ISBN,islend=False):
        self.name = name
        self.pages = pages
        self.ISBN = ISBN
        self.islend = islend

    def lend_book(self):
        self.islend = True

    def return_book(self):
        self.islend = False

    def state(self):
        if self.islend == True:
            print('《%s》状态：已经借出' %self.name)
        else:
            print('《%s》状态：未借出' % self.name)
book1 = book('三体2-黑暗森林',474,9787229100612)
book1.lend_book()
book1.state()