from PyQt5.QtWidgets import *
from QstacklayoutUsage.ui.mainwindow import Ui_MainWindow
from stackitems import Firstpage,Secondpage #导入需要放入Qstacklayout布局中的类
import sys

class StackWin(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(StackWin, self).__init__(parent)
        self.main_ui=Ui_MainWindow()
        self.main_ui.setupUi(self)
        self.init()

    def init(self):
        self.stackwidget = QStackedLayout() #声明使用Qstacklayout布局
        self.first = Firstpage()  #实例化界面一
        self.second = Secondpage() #实例化界面二
        self.stackwidget.addWidget(self.first.firstpage.widgetfirst) #Qstacklayout布局添加第一个widget，注意添加的widgetfirst是ui文件中总的控件
        self.stackwidget.addWidget(self.second.secondpage.widgetsecond)#Qstacklayout布局添加第二个widget

        self.main_ui.frame_2.setLayout(self.stackwidget) #将Qstacklayout布局摆放在frame_2中
        self.main_ui.pushButton_1.clicked.connect(self.btn1)
        self.main_ui.pushButton_2.clicked.connect(self.btn2)
        self.main_ui.pushButton_3.clicked.connect(self.btn3)

    def btn1(self):
        self.stackwidget.setCurrentIndex(0) #按钮一的槽函数，设置stackwidget显示为第一个widget页面

    def btn2(self):
        self.stackwidget.setCurrentIndex(1)#按钮二的槽函数，设置stackwidget显示为第二个widget页面

    def btn3(self):
        self.second.secondpage.progressBar.setValue(90) #按钮三的槽函数，第二个页面中的进度条为90

if __name__ =="__main__":
    app = QApplication(sys.argv)
    win = StackWin()
    win.show()
    sys.exit(app.exec_())