# 电影商店——管理录像带租借，记录借出时间、到期时间、逾期费用。复杂一点可以生成逾期用户的账号报告。
import time
class movieshop(object):
    def __init__(self,lending_time,due_time):
        self.lending_time = lending_time
        self.due_time = due_time
        self.return_time = time.strftime("%Y/%m/%d")
    #借出时间
    def print_lending_time(self):
        print('借出时间为：%s' %self.lending_time)
    #到期时间
    def print_due_time(self):
        print('到期时间为：%s' %self.due_time)
    #y逾期费用
    def overdue_expense(self):
        due_time = self.due_time.split('/')
        return_time = self.return_time.split('/')
        year,month,day = int(return_time[0])- int(due_time[0]),int(return_time[1])-int(due_time[1]),int(return_time[2])-int(due_time[2])
        days = year*365 + month*12 + day
        overdue_expenses = days*0.1
        print('逾期费用为：%s元' %overdue_expenses)

custom1 = movieshop('2017/02/15','2019/01/01')
custom1.overdue_expense()

