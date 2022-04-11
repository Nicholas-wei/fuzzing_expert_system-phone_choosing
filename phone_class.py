import xlrd
MAXPHONE=100 # 最多支持100部手机
from functools import cmp_to_key


def cmp(a,b):
    if a.final_score < b.final_score:
        return -1
    else:
        return 1


class phone_class():
    name = ""
    price = 0
    power = 0
    RAM = 0
    ROM = 0
    screen_size = 0.0
    unlock_location = ""
    resolution = 0
    charging = 0
    time = ""
    band_width = ""
    refresh_rate = 0
    curve = 0
    thick = 0
    weight = 0
    icon = ""
    CPU_brand = ""
    CPU_mark = ""
    NFC = 0
    typec = 0
    game = 0
    special = ""

    X = 0
    Y = 0
    Z = 0

    

    
    final_score = 0



    def init_phone_data(self,index):
        '''
        读取当前手机的excel数据，记录在本地.index代表行数
        '''
        data = xlrd.open_workbook('E:\data.xls')
        table = data.sheet_by_name('Sheet1')
        info_index = table.row_values(index)
        self.name = info_index[0]
        self.price = info_index[1]
        self.power = info_index[2]
        self.RAM = info_index[3]
        self.ROM = info_index[4]
        self.screen_size = info_index[5]
        self.unlock_location = info_index[6]
        self.resolution = info_index[7]
        self.charging = info_index[8]
        self.time = info_index[9]
        self.band_width = info_index[10]
        self.refresh_rate = info_index[11]
        self.curve = info_index[12]
        self.thick = info_index[13]
        self.weight = info_index[14]
        self.icon = info_index[15]
        self.CPU_brand = info_index[16]
        self.CPU_mark = info_index[17]
        self.NFC = info_index[18]
        self.typec = info_index[19]
        self.game = info_index[20]
        self.special = info_index[21]

   
    def getresult():
        return self.final_score

    def calculate_score(self):
        '''
        静态计算手机自身得分，储存在本地变量X，Y，Z里面
        X 代表性能
        Y 代表外观
        Z 代表实用性
        计算方法: 
        X = (RAM/中位数)*100 + (CPU/中位数)*(100+game*10)
        Y = (screen_size/中位数)*100 + (refresh_rate/中位数)*100 + (thick/中位数)^(-1)*100 + (weight/中位数)^(-1)*100
        Z = (power/中位数)*100 + (ROM/中位数)*100 + (resolution/中位数)*100 + (charging/中位数)*100
        其他参数:
        刷新率(当选定游戏)
        曲面屏(外观)
        time(上市时间)
        price: 用户特指
        unlock location: 用户特指(后面看要不要删掉)
        NFC: 用户特指
        '''
        

    def show(self):
        print("手机名:" + self.name)
        print("手机价格" + self.price)


class all_phone:
    all = []
    med_ram = 0
    med_cpu = 0
    med_screen_size = 0
    med_refresh_rate = 0
    med_thick = 0
    med_weight = 0
    med_power = 0
    med_rom = 0
    med_resolution = 0
    med_charging = 0
    def read_all_phone(self):
        ''' 
        从excel文件中读取所有行中的手机，储存在all数组中
        '''
        data = xlrd.open_workbook('E:\data.xls')
        table = data.sheet_by_name('Sheet1')
        all_row = table.nrows
        for i in range (1,all_row):
            tmp_phone = phone_class()
            tmp_phone.init_phone_data(i) # 逐行读取并保存
            all_phone.all.append(tmp_phone)
        all_phone.all.pop(0) # 去除头部元素重复出现的bug
        print("数据库读取完成")

    def median(data):
        # print(data)
        data.sort()
        half = len(data) // 2
        return (data[half] + data[~half])/2

    def __RAM_medium(self):
        '''
        计算所有手机RAM中位数
        '''
        ram_sum = []
        for item in all_phone.all:
            ram_sum.append(int(item.RAM))
        med = all_phone.median(ram_sum)
        return med

    def __CPU_medium(self):
        '''
        计算所有手机CPU中位数
        '''
        cpu_sum = []
        for item in all_phone.all:
            cpu_sum.append(int(item.CPU_mark))
        med = all_phone.median(cpu_sum)
        return med

    def __SCREEN_SIZE_medium(self):
        '''
        屏幕尺寸中位数
        '''
        cpu_sum = []
        for item in all_phone.all:
            cpu_sum.append(int(item.screen_size))
        med = all_phone.median(cpu_sum)
        return med

    def __RESOLUTION_medium(self):
        cpu_sum = []
        for item in all_phone.all:
            cpu_sum.append(int(item.resolution))
        med = all_phone.median(cpu_sum)
        return med
    
    def __refresh_rate_medium(self):
        cpu_sum = []
        for item in all_phone.all:
            cpu_sum.append(int(item.refresh_rate))
        med = all_phone.median(cpu_sum)
        return med

    def __THICK_medium(self):
        cpu_sum = []
        for item in all_phone.all:
            cpu_sum.append(int(item.thick))
        med = all_phone.median(cpu_sum)
        return med

    def __WEIGHT_medium(self):
        cpu_sum = []
        for item in all_phone.all:
            cpu_sum.append(int(item.weight))
        med = all_phone.median(cpu_sum)
        return med

    def __POWER_medium(self):
        cpu_sum = []
        for item in all_phone.all:
            cpu_sum.append(int(item.power))
        med = all_phone.median(cpu_sum)
        return med

    def __ROM_medium(self):
        cpu_sum = []
        for item in all_phone.all:
            cpu_sum.append(int(item.ROM))
        med = all_phone.median(cpu_sum)
        return med

    def __RESOLUTION_medium(self):
        cpu_sum = []
        for item in all_phone.all:
            cpu_sum.append(int(item.resolution))
        med = all_phone.median(cpu_sum)
        return med

    def __CHARGING_medium(self):
        cpu_sum = []
        for item in all_phone.all:
            cpu_sum.append(int(item.charging))
        med = all_phone.median(cpu_sum)
        return med

    def set_all_medium(self):
        all_phone.med_charging = self.__CHARGING_medium()
        all_phone.med_cpu = self.__CPU_medium()
        all_phone.med_power = self.__POWER_medium()
        all_phone.med_ram = self.__RAM_medium()
        all_phone.med_refresh_rate = self.__refresh_rate_medium()
        all_phone.med_resolution = self.__RESOLUTION_medium()
        all_phone.med_rom = self.__ROM_medium()
        all_phone.med_screen_size = self.__SCREEN_SIZE_medium()
        all_phone.med_thick = self.__THICK_medium()
        all_phone.med_weight = self.__WEIGHT_medium()


    def calculate_all_argument(self):
        '''
        计算all里面每个手机的xyz参数
        '''
        for item in all_phone.all:
            item.X = (int(item.RAM)/self.med_ram)*50 + (int(item.CPU_mark)/self.med_cpu)*(50+int(item.game)*10)
            item.Y = (int(item.screen_size)/self.med_screen_size)*25 + (int(item.refresh_rate/self.med_refresh_rate))*25\
                +(1/(int(item.thick)/self.med_thick))*25 + (1/(int(item.weight)/self.med_weight))*25
            item.Z = (int(item.power)/self.med_power)*25 + (int(item.ROM)/self.med_rom)*25 + (int(item.resolution)/self.med_resolution)*25\
                 + (int(item.charging)/self.med_charging)*25

    def output_mark(self):
        for item in all_phone.all:
            print(item.name)
            print("性能指数: " + str(item.X))
            print("外观指数: " + str(item.Y))
            print("实用指数:" + str(item.Z))
            print("\n")
    def recommand_index(self,case):
        '''
        根据专家系统算出来的结果计算推荐系数,case为传入的专家系统的参数
        '''
        for item in all_phone.all:
            item.X = item.X * case[0] # 性能
            item.Y = item.Y * case[1] # 外观指数
            item.Z = item.Z * case[2] # 实用指数
        print("处理推荐指数完成")

    


    def wrap_arrange(self,case,budget,G5,curve,icon_case,nfc):
        '''
        对已经计算好推荐指数的手机做最后的筛选，根据用户输入的是否需要5G，nfc,品牌，曲面屏等参数
        '''
        self.read_all_phone()
        self.set_all_medium()
        self.calculate_all_argument()
        self.recommand_index(case) # case 是专家系统传来的参数
        result_case = []
        for item in self.all:
            # 根据用户特定需求筛选价格
            if(budget == 1):
                # 0到1000
                if(item.price < 1000):
                    result_case.append(item)
            elif(budget == 2):
                # 2000以下
                if(item.price < 2000):
                    result_case.append(item)
            elif(budget == 3):
                # 3000以下
                if(item.price < 3000):
                    result_case.append(item)
            elif(budget == 4):
                # 3000以下
                if(item.price < 4000):
                    result_case.append(item)
            elif(budget == 5):
                result_case.append(item)

        # 在价格需求中选择包含5G
        for item in result_case:
            if(G5 == 1):
                # 要求5G
                if(item.band_width != '5G'):
                    result_case.remove(item)

            if(curve == 1):
                # 要求曲面屏
                if(item.curve!=1):
                    result_case.remove(item)

            if(nfc == 1):
                # 要求nfc
                if(item.NFC !=1):
                    result_case.remove(item)

            if(len(icon_case)!=0):
                # 去除相应品牌
                if(item.icon in icon_case):
                    result_case.remove(item)

        # 最后得到result_case，将其按照得分高度排序,只推荐得分最高的
        for item in result_case:
            item.final_score = item.X + item.Y + item.Z
        result_case.sort(key=cmp_to_key(cmp))
        result_case.reverse()

        return result_case





if __name__ == "__main__":
    all_phone_class = all_phone()
    all_phone_class.read_all_phone()
    # print(all_phone_class._all_phone__CPU_medium())
    all_phone_class.set_all_medium()
    all_phone_class.calculate_all_argument()
    all_phone_class.output_mark()

