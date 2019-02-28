# 航空/酒店预订系统——创建一套预订航班或酒店的预订系统。不同的航班座位和酒店房间收费不一样。
# 譬如头等舱要比经济舱贵。带阁楼的套间要更贵些。记录下何时有空房可供预订。
class book_system(object):
    def __init__(self,priceOfFirstclasscabins,priceOfEconomyclasscabins,numberofhotelwithattic,priceofhotelwithattic,numberofhotelwithoutattic,priceofhotelwithoutattic):
        self.priceOfFirstclasscabins = priceOfFirstclasscabins
        self.priceOfEconomyclasscabins = priceOfEconomyclasscabins
        self.numberofhotelwithattic = numberofhotelwithattic
        self.priceofhotelwithattic=priceofhotelwithattic
        self.numberofhotelwithoutattic = numberofhotelwithoutattic
        self.priceofhotelwithoutattic = priceofhotelwithoutattic

    def book_Firstclasscabins(self):
        pass

    def book_Economyclasscabins(self):
        pass

    def book_hotelwithattic(self):
        self.numberofhotelwithattic = self.numberofhotelwithattic - 1

    def book_hotelwithoutattic (self):
        self.numberofhotelwithoutattic = self.numberofhotelwithoutattic -1

    def wether_has_vacancies(self):
        if self.numberofhotelwithattic == 0 and self.numberofhotelwithoutattic==0:
            print('无房间可预订')
        if self.numberofhotelwithattic !=0 and self.numberofhotelwithoutattic == 0:
            print('有带阁楼的房间可预订，无套件可预订')
        if self.numberofhotelwithattic ==0 and self.numberofhotelwithoutattic != 0:
            print('无带阁楼的房间可预订，有套件可预订')
        if self.numberofhotelwithattic !=0 and self.numberofhotelwithoutattic != 0:
            print('有带阁楼的房间可预订，有套件可预订')


book_system_1 = book_system(1500,1000,50,150,100,100)
book_system_1.book_Firstclasscabins()
book_system_1.book_hotelwithattic()
book_system_1.wether_has_vacancies()