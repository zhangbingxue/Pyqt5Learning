from PyQt5.QtWidgets import *
from QstacklayoutUsage.ui.firstUi import Ui_firstForm #导入uic文件生成的py中的类名
from QstacklayoutUsage.ui.secondUi import Ui_secondForm

class Firstpage(QWidget,Ui_firstForm): #继承自QWidget和Ui_firstForm,将界面控件进行创建
    def __init__(self,parent=None):
        super(Firstpage, self).__init__(parent)
        self.firstpage = Ui_firstForm()
        self.firstpage.setupUi(self)

class Secondpage(QWidget,Ui_secondForm):
    def __init__(self,parent=None):
        super(Secondpage,self).__init__(parent)
        self.secondpage = Ui_secondForm()
        self.secondpage.setupUi(self)
