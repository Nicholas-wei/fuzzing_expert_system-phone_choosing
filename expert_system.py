class expert:
    budget = 0
    main_usage = []
    exclude_v = []
    special_v = []
    focus_num = 0

    main_u_game = 0
    main_u_appea = 0
    main_u_usage = 0

    special_game = 0
    special_appea = 0
    special_usage = 0

    focus_game = 0
    focus_appea = 0
    focus_usage = 0

    X = 0 # 性能
    Y = 0 # 外观
    Z = 0 # 实用

    G5 = 0
    NFC = 0
    TIME_PRI = 0
   
    #def __init__(self):
    #    self.budget = 0
    #    self.main_usage = []
    #    self.exclude_v = []
    #    self.special_v = []
    #    self.focus_num = 0

    def myinit(self,budget,usage,exclude,special,focus):
        self.budget = budget
        self.main_usage = usage
        self.exclude_v = exclude
        self.special_v = special
        self.focus_num = focus

    def init_expert_argu(self,usage,special,focus):
        '''
        处理usage函数
        '''
        if usage[0] == 1:
            self.main_u_game +=2
            self.main_u_usage +=1
        if usage[1] == 1:
            self.main_u_appea +=1
            self.main_u_game +=1
        if usage[2] == 1:
            self.main_u_usage +=1
        if usage[3] == 1:
            self.main_u_usage +=2
        if usage[4] == 1:
            self.main_u_usage +=1

        if special[0] == 1:
            self.special_game +=1
            self.special_usage+=1
        if special[1] == 1:
            self.special_appea +=1
        if special[2] == 1:
            self.special_usage +=1
        if special[3] == 1:
            self.special_appea +=1
        if special[4] == 1:
            self.special_usage +=1
        if special[5] == 1:
            self.special_appea +=1
            self.special_game +=1
        if special[6] == 1:
            self.special_usage +=1
            self.G5 = 1
        if special[7] == 1:
            self.special_game +=1
            self.special_usage +=1
        if special[8] == 1:
            self.special_usage +=1
            self.special_game +=1
        if special[9] == 1:
            self.special_usage+=1
            self.NFC = 1
        if special[10] == 1:
            self.special_appea +=1
        if special[11] == 1:
            self.TIME_PRI = 1

        if focus == 0:
            self.focus_game = 1
        elif focus == 1:
            self.focus_appea = 1
        elif focus == 2:
            self.focus_usage = 1

    def __part_1_func(self,end,num):
        '''
        分段函数第一部分 y=-kx+1
        end参数代表和X轴交点
        '''
        k = -(1/end)
        result = k*num + 1
        if(result<0):
            result = 0
        return result

    def __part_2_func(self,start,mid,num):
        '''
        分段函数第二部分 包括了两个子函数
        start表示起始位置，mid表示中点位置，两边对称
        num表示要取的数值，返回对应函数值
        '''
        # 以下为第一个函数参数
        k1 = 1/(mid-start)
        b1 = -(start/(mid-start))
        # 以下为第二个函数参数
        k2 = -(1/(mid-start))
        b2 = 1+(mid)/(mid-start)

        # 根据num位置计算函数取值
        if num <= start:
            return 0
        if num >=(mid+(mid-start)):
            return 0
        if num<=mid:
            # 进入第一个分段函数
            result = k1*num+b1
            return result
        elif num > mid and num < mid+(mid-start):
            # 进入第二个分段函数
            result = k2*num+b2
            return num

    def __part_3_func(self,start,num,max):
        '''
        第三个函数
        start表示起始位置
        num表示数值
        max表示横坐标最大值
        '''
        k = 1/(max-start)
        b = -(start/(max-start))
        if num < start:
            return 0
        elif num > max:
            return 1
        result = k*num+b
        return result

    def __part_func_all(self,num):
        '''
        将上面三个分段函数组合起来，返回一个list，包含每种情况的趋向程度
        max代表最大横坐标
        numcase代表三种情况的横坐标
        '''
        result1 = self.__part_1_func(0.5,num)
        result2 = self.__part_2_func(0.33,0.5,num)
        result3 = self.__part_3_func(0.5,num,1)
        return [result1,result2,result3]
        
    def compute_whole(self):
        '''
        三分段函数，用来推理
        参数一表示当前数值
        参数二表示最大数值
        '''
        # 计算方法: 每种情况的得分*每种情况的权重
        game_score = 0
        appea_score = 0
        usage_score = 0
        whole_game = 0
        whole_appea = 0
        whole_usage = 0

        whole_game = self.main_u_game*30+self.special_game*20+self.focus_game*50
        whole_appea = self.main_u_appea*30 + self.special_appea*20+self.focus_appea*50
        whole_usage = self.main_u_usage*30 + self.special_usage*20+self.focus_usage*50
        whole_score = whole_game + whole_appea + whole_usage

        # 得到每一种分类占总分类的占比
        game_score = whole_game/whole_score
        appea_score = whole_appea/whole_score
        usage_score = whole_usage/whole_score

        # 接下来将每一种分类放到三种分段函数，计算取值
        return [game_score,appea_score,usage_score]

    def process_expert_argu(self):
        '''
        处理专家系统的内部变量，专家系统推理核心算法
        输出prefer_case作为三种方面的偏好值
        '''
        score = self.compute_whole() # 每一个分量X值
        pre_game = self.__part_func_all(score[0])
        pre_appea = self.__part_func_all(score[1])
        pre_usage = self.__part_func_all(score[2])
        # 得到了关于性能、外观、实用性的低中高评价之后，开始设计参数
        # 这里用到if-else推理
        '''
        规则集见专家系统报告
        '''
        pref_case = [0,0,0] # 存放了偏好值的数组,[性能、外观、实用]
        pref_case_wrap = [0,0,0,0,0,0] # U,UA,A,PA,P,PU
        pref_case_wrap[0] += min(pre_game[0],pre_appea[0],pre_usage[0])
        pref_case_wrap[0] += min(pre_game[0],pre_appea[0],pre_usage[1])
        pref_case_wrap[0] += min(pre_game[0],pre_appea[0],pre_usage[2])
        pref_case_wrap[1] += min(pre_game[0],pre_appea[1],pre_usage[0])
        pref_case_wrap[2] += min(pre_game[0],pre_appea[1],pre_usage[1])
        pref_case_wrap[1] += min(pre_game[0],pre_appea[1],pre_usage[2])
        pref_case_wrap[2] += min(pre_game[0],pre_appea[2],pre_usage[0])
        pref_case_wrap[1] += min(pre_game[0],pre_appea[2],pre_usage[1])
        pref_case_wrap[1] += min(pre_game[0],pre_appea[2],pre_usage[2])

        pref_case_wrap[5] += min(pre_game[1],pre_appea[0],pre_usage[0])
        pref_case_wrap[5] += min(pre_game[1],pre_appea[0],pre_usage[1])
        pref_case_wrap[0] += min(pre_game[1],pre_appea[0],pre_usage[2])
        pref_case_wrap[4] += min(pre_game[1],pre_appea[1],pre_usage[0])
        pref_case_wrap[3] += min(pre_game[1],pre_appea[1],pre_usage[1])
        pref_case_wrap[5] += min(pre_game[1],pre_appea[1],pre_usage[2])
        pref_case_wrap[3] += min(pre_game[1],pre_appea[2],pre_usage[0])
        pref_case_wrap[2] += min(pre_game[1],pre_appea[2],pre_usage[1])
        pref_case_wrap[1] += min(pre_game[1],pre_appea[2],pre_usage[2])

        pref_case_wrap[4] += min(pre_game[2],pre_appea[0],pre_usage[0])
        pref_case_wrap[5] += min(pre_game[2],pre_appea[0],pre_usage[1])
        pref_case_wrap[5] += min(pre_game[2],pre_appea[0],pre_usage[2])
        pref_case_wrap[4] += min(pre_game[2],pre_appea[1],pre_usage[0])
        pref_case_wrap[4] += min(pre_game[2],pre_appea[1],pre_usage[1])
        pref_case_wrap[5] += min(pre_game[2],pre_appea[1],pre_usage[2])
        pref_case_wrap[3] += min(pre_game[2],pre_appea[2],pre_usage[0])
        pref_case_wrap[3] += min(pre_game[2],pre_appea[2],pre_usage[1])
        pref_case_wrap[5] += min(pre_game[2],pre_appea[2],pre_usage[2])
        
        max_vec = pref_case_wrap.index(max(pref_case_wrap))
        
        pref_case[0] = pref_case_wrap[5]*0.5+pref_case_wrap[4] + pref_case_wrap[3]*0.5
        pref_case[1] = pref_case_wrap[1]*0.5+pref_case_wrap[2] + pref_case_wrap[3]*0.5
        pref_case[2] = pref_case_wrap[0] + pref_case_wrap[1]*0.5+pref_case_wrap[5]*0.5

        # 这里输出的prefer_case就是最后专家系统的输出参数。

        return pref_case

    def smooth(self,case):
        ''' 
        对结果进行平滑处理。这里采用add-one平滑
        '''
        sum = 0
        for i in case:
            sum+=i
        sum +=3 # add_one平滑
        result = [(case[0]+1)/sum,(case[1]+1)/sum,(case[2]+1)/sum]
        return result


    def expert_interface(self,budget,usage,exclude,special,focus):
        '''
        接受外部输入,整合内部函数
        '''
        self.myinit(budget,usage,exclude,special,focus)
        self.init_expert_argu(usage,special,focus)
        result = self.process_expert_argu()
        result = self.smooth(result)
        return result # 返回系数矩阵
        

    

