import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

from test import Ui_MainWindow as welcome_ui
from choose_phone import Ui_Dialog as choose_ui



price_option = 0


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
        self.pushButton_2.clicked.connect(self.show_all)
        self.pushButton_3.clicked.connect(self.add_phone)
    def show_choose(self):
        self.choose_signal.emit() # 发出信号
    def show_all(self):
        self.all_signal.emit()
    def add_phone(self):
        self.add_signal.emit()


class ChooseWindow(QtWidgets.QDialog,choose_ui):
    '''
    运行choose window
    '''
    def __init__(self):
        super(ChooseWindow,self).__init__()
        self.setupUi(self)
    def finish(self):
        print(self.radioButton.isChecked())
        '''
        这里需要先把获得的数据储存在全局变量里面再emit
        '''
        self.buttonBox.accepted.emit()
    def back(self):
        self.buttonBox.rejected.emit()
        
        


class Controller:
    '''
    将信号和对应动作绑定,界面切换控制器
    '''
    def __init__(self):
        pass
    def show_welcome(self):
        self.main = MainWindow()
        self.main.choose_signal.connect(self.show_choose)
        self.main.all_signal.connect(self.show_all)
        self.main.add_signal.connect(self.add_phone)
        self.main.show()

    def show_choose(self):
        self.choose = ChooseWindow()
        self.main.close()
        self.choose.show()
        # 下面是两个buttonbox关联的信号，可以不用自己初始化
        self.choose.buttonBox.accepted.connect(self.compute_score) # 计算得分，进行推荐
        self.choose.buttonBox.rejected.connect(self.show_welcome) # 返回上一层

    def show_all(self):
        pass
    
    def add_phone(self):
        pass

    def compute_score(self):
        # 每次点击的时候会自动发出信号
        print("you pressed ok")
        pass



def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller() # 控制器实例
    controller.show_welcome() # 默认展示的是 hello 页面
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
