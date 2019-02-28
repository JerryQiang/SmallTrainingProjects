# 学生成绩管理器——记录一个班级的学生（创建一个Student类，记录他们的名字、平均分和考试分数）和他们的成绩等级。根据学生的测验和作业的分数计算出平均分和成绩等级。
# 复杂一点可以将数据画在贝尔曲线上
class Student(object):
    def __init__(self):
        self.students_name =[]
        self.students_score={}
        self.students_grade={}
        self.students_average = 0

    def add_student(self):
        names = input('请输入学生姓名，以逗号隔开：')
        names=names.split('，')
        for name in names:
            self.students_name.append(name)

    def input_score(self):
        for name in self.students_name:
            score =  input('请输入%s同学的成绩:' %name)
            self.students_score[name] = score

    def get_score(self):
        name = input('请输入学生姓名:')
        print('%s同学的分数为：'%self.students_score[name])


    def get_average(self):
        numberOfStudents = 0
        sumOfScores = 0
        for score in self.students_score.values():
            sumOfScores += int(score)
            numberOfStudents += 1
        self.students_average = sumOfScores/numberOfStudents
        print('同学们的总成绩为%.1f' %self.students_average)

studentOfSEU = Student()
studentOfSEU.add_student()
studentOfSEU.input_score()
studentOfSEU.get_average()


