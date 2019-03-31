import sys
import requests
import json
from PyQt5.QtWidgets import QApplication,QLabel, QWidget, QPushButton, QMessageBox, QLineEdit,QPlainTextEdit
from PyQt5.QtGui import QIcon
from random import randint
from modelu_zjy import*
'''
#获取位置信息
def position_name(data_list):
    i=0
    list_position=[]
    while i<len(data_list):
        list_position.append(data_list[i]['position_name'])
        i=i+1
    return list_position
#获取aqi
def aqi(data_list):
    i=0
    list_position=[]
    while i<len(data_list):
        list_position.append(data_list[i]['aqi'])
        i=i+1
    return list_position
#获取area
def area(data_list):
    i=0
    list_position=[]
    while i<len(data_list):
        list_position.append(data_list[i]['area'])
        i=i+1
    return list_position
#获取co_24h
def co24h(data_list):
    i=0
    list_position=[]
    while i<len(data_list):
        list_position.append(data_list[i]['co_24h'])
        i=i+1
    return list_position
#获取primary_pollutant
def primary_pollutant(data_list):
    i=0
    list_position=[]
    while i<len(data_list):
        list_position.append(data_list[i]['primary_pollutant'])
        i=i+1
    return list_position
#获取quality
def quality(data_list):
    i=0
    list_position=[]
    while i<len(data_list):
        list_position.append(data_list[i]['quality'])
        i=i+1
    return list_position
#获取time_point
def time_point(data_list):
    i=0
    list_position=[]
    while i<len(data_list):
        list_position.append(data_list[i]['time_point'])
        i=i+1
    return list_position
'''
class Example(QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()


    def initUI(self):

        self.setGeometry(510, 140, 900, 750)
        self.setWindowTitle('speed的pm2.5监控')

        #查询按钮设置
        self.bt1 = QPushButton('查询pm2.5监控', self)
        self.bt1.setGeometry(350, 115 , 200, 40)
        #鼠标移到这里，有文本显示
        self.bt1.setToolTip('<b>点击这里进行pm2.5指数查询</b>')
        self.bt1.clicked.connect(self.showMessage)#信号和槽的连接
        #标签
        self.label_aqi = QLabel("Aqi", self)
        self.label_aqi.move(43, 180)
        self.label_area=QLabel("Area",self)
        self.label_area.move(98,180)
        self.label_co24h = QLabel("CO_24h", self)
        self.label_co24h.move(153, 180)
        self.label_position = QLabel("Position", self)
        self.label_position.move(243, 180)
        self.label_primary_pollutant = QLabel("Primary_pollutant", self)
        self.label_primary_pollutant.move(410, 180)
        self.label_quality = QLabel("Quality", self)
        self.label_quality.move(610, 180)
        self.label_time_point = QLabel("Time_point", self)
        self.label_time_point.move(743, 180)
        #初始化的文本框显示
        self.text_search = QLineEdit('在这里输入城市拼音:(例如 长沙：changsha)', self)
        self.text_search.selectAll()
        self.text_search.setFocus()
        self.text_search.setGeometry(250, 50, 350, 50)
        # aqi文本框
        self.text_aqi = QPlainTextEdit('', self)
        #self.text_aqi.selectAll()
        #self.text_aqi.setFocus()
        self.text_aqi.setGeometry(30, 210, 50, 500)
        # area文本框
        self.text_area = QPlainTextEdit('', self)
        #self.text_area.selectAll()
        #self.text_area.setFocus()
        self.text_area.setGeometry(90, 210, 50, 500)
        # co_24h文本框
        self.text_co24h = QPlainTextEdit('', self)
        #self.text_co24h.selectAll()
        #self.text_co24h.setFocus()
        self.text_co24h.setGeometry(150, 210, 50, 500)
        # position文本框
        self.text_position = QPlainTextEdit('', self)
        #self.text_position.selectAll()
        #self.text_position.setFocus()
        self.text_position.setGeometry(210, 210, 150, 500)
        # primary_pollutant文本框
        self.text_primary_pollutant = QPlainTextEdit('', self)
        #self.text_primary_pollutant.selectAll()
        #self.text_primary_pollutant.setFocus()
        self.text_primary_pollutant.setGeometry(370, 210, 220, 500)
        # quality文本框
        self.text_quality = QPlainTextEdit('', self)
        #self.text_quality.selectAll()
        #self.text_quality.setFocus()
        self.text_quality.setGeometry(600, 210, 90, 500)
        # time_point文本框
        self.text_time_point = QPlainTextEdit('', self)
        #self.text_time_point.selectAll()
        #self.text_time_point.setFocus()
        self.text_time_point.setGeometry(700, 210, 180, 500)
        self.show()

    def showMessage(self):
        str1 = "http://www.pm25.in/api/querys/co.json?city="
        str3 = "&token=5j1znBVAsnSf5xQyNQyq"
        city_name = str(self.text_search.text())
        url=str1+city_name+str3
        print(url)
        # 获取API数据
        # r_original = requests.get('http://www.pm25.in/api/querys/co.json?city=changsha&token=5j1znBVAsnSf5xQyNQyq')
        r_original = requests.get(url)
        # data_list返回是一个列表
        data_list = json.loads(r_original.text)
        self.text_aqi = QPlainTextEdit(data, self)
        #显示地址,aqi,area,co_24h,primary_pollutant
        list_position=position_name(data_list)
        list_primary_pollutant= primary_pollutant(data_list)
        list_aqi=aqi(data_list)
        list_area=area(data_list)
        list_co24h=co24h(data_list)
        list_quality = quality(data_list)
        list_time_point = time_point(data_list)

        s=len(data_list)
        #每次查询清空列表
        self.text_position.clear()
        self.text_aqi.clear()
        self.text_area.clear()
        self.text_co24h.clear()
        self.text_primary_pollutant.clear()
        self.text_quality.clear()
        self.text_time_point.clear()
        print(list_aqi)
        print(type(list_aqi[0]))
        print(str(list_aqi[0]))
        for i in range(s):
            list_aqi[i]=str(list_aqi[i])
        print(list_aqi)
        print(type(list_aqi[0]))
        #循环显示列表中所有数据
        for i in range(s):
            self.text_aqi.appendPlainText("wuhuhuhu")
            self.text_aqi.appendPlainText("wuhuhu")
            self.text_area.appendPlainText(str(list_area[i]))
            self.text_co24h.appendPlainText(str(list_co24h[i]))
            self.text_position.appendPlainText(str(list_position[i]))
            self.text_primary_pollutant.appendPlainText(str(list_primary_pollutant[i]))
            self.text_quality.appendPlainText(str(list_quality[i]))
            self.text_time_point.appendPlainText(str(list_time_point[i]))
            #self.text_position.appendPlainText('\n')
        print(list_position)

    def closeEvent(self, event):

        reply = QMessageBox.question(self, '确认', '确认退出吗', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())