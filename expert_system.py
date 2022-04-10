class expert:
    budget = 0
    main_usage = []
    exclude_v = []
    special_v = []
    focus_num = 0

    X = 0 # 性能
    Y = 0 # 外观
    Z = 0 # 实用
   
    def init(self,budget,usage,exclude,special,focus):
        expert.budget = budget
        expert.main_usage = usage
        expert.exclude_v = exclude
        expert.special_v = special
        expert.focus_num = focus

