import xlrd
MAXPHONE=100 # 最多支持100部手机
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
if __name__ == "__main__":
    all_phone_class = all_phone()
    all_phone_class.read_all_phone()
    # print(all_phone_class._all_phone__CPU_medium())
    all_phone_class.set_all_medium()
    all_phone_class.calculate_all_argument()
    all_phone_class.output_mark()

