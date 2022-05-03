import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

from test2 import Ui_MainWindow as welcome_ui
from choose_phone2 import Ui_Dialog as choose_ui
from add_phone2 import Ui_Dialog as add_ui
from phoneresult import Ui_Dialog as phone_result

import expert_system
import phone_class

price_option = 0
argu_case = []

class MainWindow(QtWidgets.QMainWindow, welcome_ui):
    '''
    运行主界面
    '''
    choose_signal = QtCore.pyqtSignal()
    all_signal = QtCore.pyqtSignal()
    add_signal = QtCore.pyqtSignal()
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.show_choose) # 将按钮连接到发送信号
        self.pushButton_3.clicked.connect(self.add_phone)
    def show_choose(self):
        self.choose_signal.emit() # 发出信号
    def show_all(self):
        self.all_signal.emit()
    def add_phone(self):
        self.add_signal.emit()


class AddWindow(QtWidgets.QDialog,add_ui):
    name = ""
    price = ""
    power = ""
    ram = ""
    rom = ""
    screen_size = ""
    cpuname_mark = ""
    resolution = ""
    charge = ""
    refresh_rate = ""
    thick = ""
    weight= ""
    brand = ""
    remark = ""
    add_case = [0,0,0,0,0] # 5G,曲面屏，NFC，typec, 游戏款
    tmp_list = []
    def __init__(self):
        super(AddWindow,self).__init__()
        self.setupUi(self)
        '''
        绑定选项和局部变量
        '''
        self.checkBox.toggled.connect(lambda:self.feature(self.checkBox))
        self.checkBox_2.toggled.connect(lambda:self.feature(self.checkBox_2))
        self.checkBox_3.toggled.connect(lambda:self.feature(self.checkBox_3))
        self.checkBox_4.toggled.connect(lambda:self.feature(self.checkBox_4))
        self.checkBox_5.toggled.connect(lambda:self.feature(self.checkBox_5))
        self.textEdit.textChanged.connect(lambda:self.text_changed(self.textEdit))
        self.textEdit_2.textChanged.connect(lambda:self.text_changed(self.textEdit_2))
        self.textEdit_3.textChanged.connect(lambda:self.text_changed(self.textEdit_3))
        self.textEdit_4.textChanged.connect(lambda:self.text_changed(self.textEdit_4))
        self.textEdit_5.textChanged.connect(lambda:self.text_changed(self.textEdit_5))
        self.textEdit_6.textChanged.connect(lambda:self.text_changed(self.textEdit_6))
        self.textEdit_7.textChanged.connect(lambda:self.text_changed(self.textEdit_7))
        self.textEdit_8.textChanged.connect(lambda:self.text_changed(self.textEdit_8))
        self.textEdit_9.textChanged.connect(lambda:self.text_changed(self.textEdit_9))
        self.textEdit_10.textChanged.connect(lambda:self.text_changed(self.textEdit_10))
        self.textEdit_11.textChanged.connect(lambda:self.text_changed(self.textEdit_11))
        self.textEdit_12.textChanged.connect(lambda:self.text_changed(self.textEdit_12))
        self.textEdit_13.textChanged.connect(lambda:self.text_changed(self.textEdit_13))
        self.textEdit_14.textChanged.connect(lambda:self.text_changed(self.textEdit_14))

    def feature(self,btn):
        if btn.objectName() == "checkBox":
            AddWindow.add_case[0]^=1
            print("0 choosed: 0 is %d" % AddWindow.add_case[0])
        if btn.objectName() == "checkBox_2":
            AddWindow.add_case[1]^=1
        if btn.objectName() == "checkBox_3":
            AddWindow.add_case[2]^=1
        if btn.objectName() == "checkBox_4":
            AddWindow.add_case[3]^=1
        if btn.objectName() == "checkBox_5":
            AddWindow.add_case[4]^=1
    def text_changed(self,btn):
        if btn.objectName() == "textEdit":
            self.name = btn.toPlainText()
            # print(self.name)
        elif btn.objectName() == "textEdit_2":
            self.price = btn.toPlainText()
        elif btn.objectName() == "textEdit_3":
            self.power = btn.toPlainText()
        elif btn.objectName() == "textEdit_4":
            self.ram = btn.toPlainText()
        elif btn.objectName() == "textEdit_5":
            self.rom = btn.toPlainText()
        elif btn.objectName() == "textEdit_6":
            self.screen_size = btn.toPlainText()
        elif btn.objectName() == "textEdit_7":
            self.resolution = btn.toPlainText()
        elif btn.objectName() == "textEdit_8":
            self.charge = btn.toPlainText()
        elif btn.objectName() == "textEdit_9":
            self.refresh_rate = btn.toPlainText()
        elif btn.objectName() == "textEdit_10":
            self.thick = btn.toPlainText()
        elif btn.objectName() == "textEdit_11":
            self.weight = btn.toPlainText()
        elif btn.objectName() == "textEdit_12":
            self.brand = btn.toPlainText()
        elif btn.objectName() == "textEdit_13":
            self.cpuname_mark = btn.toPlainText()
        elif btn.objectName() == "textEdit_14":
            self.remark = btn.toPlainText()




class ChooseWindow(QtWidgets.QDialog,choose_ui):
    '''
    运行choose window界面
    '''
    budget_pre = 0 # 预算选择,分为[1,2,3,4,5]代表五个等级，问题1
    main_usage = [0,0,0,0,0] # 一个向量，[娱乐活动、日常使用、外出接收消息、备用机、拍照]，问题2
    exclude_v = [0,0,0,0,0,0] # 用向量表示去除的品牌[小米、apple、华为、中兴、VIVO、samsung]
    special_v = [0,0,0,0,0,0,0,0,0,0,0,0] # 向量表示[ram, 厚度, rom, 重量, 相机质量, 刷新率, 5G, CPU, 续航/快充，NFC, 曲面屏，发行时间]
    focus_num = 0 # 用1，2，3代表性能、外观、实用性
    exclude_name_list = []
    def __init__(self):
        super(ChooseWindow,self).__init__()
        self.setupUi(self)
        '''
        将budget中的radiobutton的toggled信号和槽函数绑定,注意每次取消选中也会导致connect被激活，但是结果是正确的
        '''
        # 第一个问题的按钮状态
        self.radioButton.toggled.connect(lambda:self.budget(self.radioButton))
        self.radioButton_2.toggled.connect(lambda:self.budget(self.radioButton_2))
        self.radioButton_3.toggled.connect(lambda:self.budget(self.radioButton_3))
        self.radioButton_4.toggled.connect(lambda:self.budget(self.radioButton_4))
        self.radioButton_5.toggled.connect(lambda:self.budget(self.radioButton_5))
        # 第二个问题的按钮状态
        self.checkBox.toggled.connect(lambda:self.usage(self.checkBox))
        self.checkBox_2.toggled.connect(lambda:self.usage(self.checkBox_2))
        self.checkBox_3.toggled.connect(lambda:self.usage(self.checkBox_3))
        self.checkBox_4.toggled.connect(lambda:self.usage(self.checkBox_4))
        self.checkBox_11.toggled.connect(lambda:self.usage(self.checkBox_11))
        # 第三个问题的按钮状态
        self.checkBox_5.toggled.connect(lambda:self.exclude(self.checkBox_5))
        self.checkBox_6.toggled.connect(lambda:self.exclude(self.checkBox_6))
        self.checkBox_7.toggled.connect(lambda:self.exclude(self.checkBox_7))
        self.checkBox_8.toggled.connect(lambda:self.exclude(self.checkBox_8))
        self.checkBox_9.toggled.connect(lambda:self.exclude(self.checkBox_9))
        self.checkBox_10.toggled.connect(lambda:self.exclude(self.checkBox_10))
        # 第四个问题的按钮状态
        self.checkBox_12.toggled.connect(lambda:self.special(self.checkBox_12))
        self.checkBox_13.toggled.connect(lambda:self.special(self.checkBox_13))
        self.checkBox_14.toggled.connect(lambda:self.special(self.checkBox_14))
        self.checkBox_15.toggled.connect(lambda:self.special(self.checkBox_15))
        self.checkBox_16.toggled.connect(lambda:self.special(self.checkBox_16))
        self.checkBox_17.toggled.connect(lambda:self.special(self.checkBox_17))
        self.checkBox_18.toggled.connect(lambda:self.special(self.checkBox_18))
        self.checkBox_19.toggled.connect(lambda:self.special(self.checkBox_19))
        self.checkBox_20.toggled.connect(lambda:self.special(self.checkBox_20))
        self.checkBox_21.toggled.connect(lambda:self.special(self.checkBox_21))
        self.checkBox_22.toggled.connect(lambda:self.special(self.checkBox_22))
        self.checkBox_23.toggled.connect(lambda:self.special(self.checkBox_23))
        # 第五个问题
        self.radioButton_11.toggled.connect(lambda:self.focus(self.radioButton_11))
        self.radioButton_12.toggled.connect(lambda:self.focus(self.radioButton_12))
        self.radioButton_13.toggled.connect(lambda:self.focus(self.radioButton_13))
    
    def budget(self,btn):
        '''
        接收并处理radio_button信号
        '''
        if btn.objectName() == "radioButton":
            ChooseWindow.budget_pre = 1
            print("pre: " + str(ChooseWindow.budget_pre))
        elif btn.objectName() == "radioButton_2":
            ChooseWindow.budget_pre = 2
            print("pre: " + str(ChooseWindow.budget_pre))
        elif btn.objectName() == "radioButton_3":
            ChooseWindow.budget_pre = 3   
            print("pre: " + str(ChooseWindow.budget_pre))
        elif btn.objectName() == "radioButton_4":
            ChooseWindow.budget_pre = 4  
            print("pre: " + str(ChooseWindow.budget_pre))
        elif btn.objectName() == "radioButton_5":
            ChooseWindow.budget_pre = 5  
            print("pre: " + str(ChooseWindow.budget_pre))

    def usage(self,btn):
        '''
        接收并处理第二个问题的信号，异或上每一个向量，得到点击或者没有点击的结果
        '''
        if btn.objectName() == "checkBox":
            ChooseWindow.main_usage[0] = ChooseWindow.main_usage[0]^1
            print("usage[1]: " + str(ChooseWindow.main_usage[0]) )
        elif btn.objectName() == "checkBox_2":
            ChooseWindow.main_usage[1] = ChooseWindow.main_usage[1]^1
            print("usage[1]: " + str(ChooseWindow.main_usage[1]) )
        elif btn.objectName() == "checkBox_3":
            ChooseWindow.main_usage[2] = ChooseWindow.main_usage[2]^1
            print("usage[1]: " + str(ChooseWindow.main_usage[2]) )
        elif btn.objectName() == "checkBox_4":
            ChooseWindow.main_usage[3] = ChooseWindow.main_usage[3]^1
            print("usage[1]: " + str(ChooseWindow.main_usage[3]) )
        elif btn.objectName() == "checkBox_11":
            ChooseWindow.main_usage[4] = ChooseWindow.main_usage[4]^1
            print("usage[1]: " + str(ChooseWindow.main_usage[4]) )

    def exclude(self,btn):
        '''
        处理第三个问题的按钮点击
        '''
        if(btn.objectName() == "checkBox_5"):
            ChooseWindow.exclude_v[0] = ChooseWindow.exclude_v[0]^1
        elif btn.objectName() == "checkBox_6":
            ChooseWindow.exclude_v[1] = ChooseWindow.exclude_v[1]^1
        elif btn.objectName() == "checkBox_7":
            ChooseWindow.exclude_v[2] = ChooseWindow.exclude_v[2]^1
        elif btn.objectName() == "checkBox_8":
            ChooseWindow.exclude_v[3] = ChooseWindow.exclude_v[3]^1
        elif btn.objectName() == "checkBox_9":
            ChooseWindow.exclude_v[4] = ChooseWindow.exclude_v[4]^1
            print("exclude[4]: " + str(ChooseWindow.exclude_v[4]))
        elif btn.objectName() == "checkBox_10":
            ChooseWindow.exclude_v[5] = ChooseWindow.exclude_v[5]^1

    def special(self,btn):
        '''
        处理special事件
        '''
        if(btn.objectName() == "checkBox_12"):
            ChooseWindow.special_v[0] = ChooseWindow.special_v[0]^1
        elif btn.objectName() == "checkBox_13":
            ChooseWindow.special_v[1] = ChooseWindow.special_v[1]^1
        elif btn.objectName() == "checkBox_14":
            ChooseWindow.special_v[2] = ChooseWindow.special_v[2]^1
        elif btn.objectName() == "checkBox_15":
            ChooseWindow.special_v[3] = ChooseWindow.special_v[3]^1
        elif btn.objectName() == "checkBox_16":
            ChooseWindow.special_v[4] = ChooseWindow.special_v[4]^1
        elif btn.objectName() == "checkBox_17":
            ChooseWindow.special_v[5] = ChooseWindow.special_v[5]^1
        elif btn.objectName() == "checkBox_18":
            ChooseWindow.special_v[6] = ChooseWindow.special_v[6]^1
        elif btn.objectName() == "checkBox_19":
            ChooseWindow.special_v[7] = ChooseWindow.special_v[7]^1
        elif btn.objectName() == "checkBox_20":
            ChooseWindow.special_v[8] = ChooseWindow.special_v[8]^1
        elif btn.objectName() == "checkBox_21":
            ChooseWindow.special_v[9] = ChooseWindow.special_v[9]^1
        elif btn.objectName() == "checkBox_22":
            ChooseWindow.special_v[10] = ChooseWindow.special_v[10]^1
        elif btn.objectName() == "checkBox_23":
            ChooseWindow.special_v[11] = ChooseWindow.special_v[11]^1

    def focus(self,btn):
        '''
        处理第五个问题,focus事件
        '''
        if(btn.objectName() == "radioButton_11"):
            ChooseWindow.focus_num = 0
        elif(btn.objectName() == "radioButton_12"):
            ChooseWindow.focus_num = 1
        elif(btn.objectName() == "radioButton_13"):
            ChooseWindow.focus_num = 2


    def finish(self):
        print(self.radioButton.isChecked())
        '''
        这里需要先把获得的数据储存在全局变量里面再emit
        '''
        self.buttonBox.accepted.emit()
    def back(self):
        self.buttonBox.rejected.emit()
        
        

def form_reason(phone_list):
    buf = ""
    buf+="您的最佳推荐：\n"
    buf+="手机名: " + phone_list[0].name + '\n'
    buf+="价格: " + str(phone_list[0].price) + '元\n'
    buf+="CPU 品牌: " + phone_list[0].CPU_brand + '\n'
    buf+="CPU 跑分: " + str(phone_list[0].CPU_mark) + '\n'
    buf+="像素: " + str(phone_list[0].resolution) + '\n'
    buf+="电量: " + str(phone_list[0].power) + '\n'
    buf+="充电功率: " + str(phone_list[0].charging)+'W\n'
    buf+=phone_list[0].special
    return buf


def form_formula(phone_list,pref_result):
    buf = ""
    buf+="您的喜好指数为: " + '\n'
    buf+="性能:" + str(pref_result[0]) + '\n'
    buf+="外观: " + str(pref_result[1]) + '\n'
    buf+="实用: " + str(pref_result[2]) + '\n'
    print(buf)
    return buf



class Controller:
    '''
    将信号和对应动作绑定,界面切换控制器
    '''
    def __init__(self):
        pass
    def show_welcome(self):
        self.main = MainWindow()
        self.main.choose_signal.connect(self.show_choose)
        # self.main.all_signal.connect(self.show_all)
        self.main.add_signal.connect(self.add_phone)
        self.main.show()

    def show_choose(self):
        self.choose = ChooseWindow()
        self.main.close()
        self.choose.show()
        # 下面是两个buttonbox关联的信号，可以不用自己初始化
        self.choose.buttonBox.accepted.connect(self.compute_score) # 计算得分，进行推荐
        self.choose.buttonBox.rejected.connect(self.show_welcome) # 返回上一层
        

    def show_reference(self):
        self.ref = reference_window()
        self.choose.close()
        self.ref.show()

    def show_all(self):
        pass
    
    def add_phone(self):
        self.add = AddWindow()
        self.main.close()
        self.add.show()
        self.add.buttonBox.accepted.connect(self.write_argu)
        self.add.buttonBox.rejected.connect(self.show_welcome)

    
    def write_argu(self):
        '''
        将结果写入excel文档
        用类参数作为参数传递
        '''
        feature = self.add
        phone_class.all_phone.add_phone(feature.name,feature.price,feature.power,feature.ram,feature.rom,feature.screen_size,feature.cpuname_mark,feature.resolution,feature.charge,feature.refresh_rate,feature.thick,feature.weight,feature.brand,feature.remark,feature.add_case)
        self.main.show()

        
    def compute_score(self):
        # 每次点击的时候会自动发出信号
        print("you pressed ok") # 点击选择界面的ok按钮触发
        # 处理一下exclude_name_list
        # expert = expert_system.expert()
        window_argu = ChooseWindow()
        if(window_argu.exclude_v[0] == 1):
            window_argu.exclude_name_list.append("Redmi")
            window_argu.exclude_name_list.append("Xiaomi")
        if(window_argu.exclude_v[1] == 1):
            window_argu.exclude_name_list.append("Apple")
        if(window_argu.exclude_v[2] == 1):
            window_argu.exclude_name_list.append("Huawei")
        if(window_argu.exclude_v[3] == 1):
            window_argu.exclude_name_list.append("ZTE")
        if(window_argu.exclude_v[4] == 1):
            window_argu.exclude_name_list.append("iQOO")
        if(window_argu.exclude_v[5] == 1):
            window_argu.exclude_name_list.append("Samsung")
        
        # 专家系统处理
        expert = expert_system.expert()
        pref_result = expert.expert_interface(window_argu.budget_pre,window_argu.main_usage,window_argu.exclude_v,window_argu.special_v,window_argu.focus_num)
        # 关闭choose界面
        phone_choose = phone_class.all_phone()
        recommend_list = phone_choose.wrap_arrange(pref_result,window_argu.budget_pre,window_argu.special_v[6],window_argu.special_v[10],window_argu.exclude_name_list,window_argu.special_v[9])
        self.choose.close()
        # 这里需要给reference_window传递参数，用于动态显示 **TODO tomorrow**
        global argu_case
        argu_case.append(recommend_list[0].name)
        recommend_reason = form_reason(recommend_list)
        formula = form_formula(recommend_list,pref_result)
        argu_case.append(recommend_reason)
        argu_case.append(formula)
        self.refer_window = reference_window(argu_case)
        self.refer_window.show()
        self.refer_window.back_signal.connect(self.show_welcome) # 返回主界面
        # self.refer_window.close()

class reference_window(QtWidgets.QDialog,phone_result):
    '''
    手机推荐界面
    '''
    back_signal = QtCore.pyqtSignal()
    def __init__(self,argu_case):
        super(reference_window,self).__init__()
        # setup UI这里传入(self,图片名，推荐原因，推荐公式)
        self.setupUi(self,argu_case[0],argu_case[1],argu_case[2])
        self.pushButton.clicked.connect(self.back_main)

    def back_main(self):
        self.back_signal.emit()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller() # 控制器实例
    controller.show_welcome() # 默认展示的是 hello 页面
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
