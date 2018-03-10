# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui, uic
import mainwindow,sys,al,p,time
import urllib,re
import sqlite3,thread
form_class = mainwindow.Ui_MainWindow
form_class2=al.Ui_Form
form_class3=p.Ui_Form
global bu
bu=[]
class MyWindowClass(QtGui.QMainWindow, form_class):
    
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.s_details.clicked.connect(self.al)
        self.s_enq.clicked.connect(self.ol)
        self.s_enq.clicked.connect(self.ol)
        #self.ex_details.clicked.connect(self.exam_details)
 
        self.form_widget = alclass(self)
        self.form_widget2 = proclass(self)
        #self.form_widget2 = details_exam_class(self)

    def res(self,index):
        link='http://www.doenets.lk/result/alresult.jsf?frm=frm&frm%3Ausername='+index+'&frm%3AbtnSubmit=&javax.faces.ViewState=H4sIAAAAAAAAALVVzWsTQRR%2FzUc%2FYr9sVfzAj0NRirrB%2BoFYxEbb0mCqxbRiVaiTzbSZONkdZ2bTjYeiF3vwoqgHoaIHDx568y8QD4JQQcGLJ%2FGuNxE8ObNdN9uaUqV2IG%2Ffzr6Zeb%2Ff%2B73J%2FFeIM8FhYxGVkeFIQo0hJArDiMUbPr16veXa%2ByhEBiFBbZQfRKa0eRqaZIFjUbBp3mWn%2BkCP5ulGZdvVr1FC8yQvnXAE5hYqYYdD55WMtztF1pRxPlfEpuy99%2B7S03bRTSMALlPLYkwNCfXFCZKXx5wbMANRNR0JvLgOqL7NcDD0pq4xiUwsDNMuMdvCljTG0md%2B%2B10j3GaYy8pZXBHgjw51IofWakYDllMKf1RpJJCUnOQciYXiprPKTYpzVMkQId3bH3Y%2BfoOeRKEuDTFBbmIPRnQ6pq1atLd2dlmJJB5S1GGeRWXMx9%2B%2BPPlgbmE4ApEMNJkUCXFOsSahw%2BMsqTNMZlUy1lRvBhJCrcl7e0jYshhB7GQWc4IouYlyFPe6jJU1TSC0bVNodqnjDeFYfjLaUiyFkRoZyaQH%2Bv04lfPRFQJJiVGjH08ih8rBxcmuFGO0Mmpfx9b3FwfG5%2FqKfc2au%2Blt0JZEVOlDxRpuQZYoQN3YfTI777qqaEf%2FrWgjnJQV2HB5dLYJCZuqJRotIJniOKtS1R9btG68OkR8aB4fLf6LtptdLba4FtuRGlqrX6K1Bu1sCLaOe1vHQ7t1Bkw3UJLjiFeCiQTjpIQ9tMFcTLdF8NZSjTCKwkO3PTjrt5yqZ%2B0K%2BftD%2Fj53Rj%2BaVPdxbCl1YT5aYUolO8KEq7LYDjexkTU5YTLoe68PTts2xcha2MNvfZz7%2BS0CdZchXkbU0dLWm%2B8JGvTw6g26lLQ%2FgXSGyxHyty6jYGkll1MQKuShVXOKKv0dXEl%2FFwmevmDbK98Zvu7qVYvKdH4pdWlL4inMO748e%2F7j9uzxiL4UfOo4tFfjzjmlHOZ35h%2Ft3PDw893Q3edj6Pl%2FYvREEfK7awhHQmtIfaZYi%2Fy07ZGwu7bcZIWqfwyMpQ47pk1Gnb7NC57wgieobSJJbGtiaCDV%2F3fo109VHpoyh1jZJnmoDpcFAK76NavVC%2Btas%2FbiDQfzSnLxsbZLw8OpzZEAV4G5vwCpPXfjFQgAAA%3D%3D'
        sock = urllib.urlopen(link) 
        htmlSource = sock.read()                            
        sock.close()
        exam=re.findall ('<div class="rightre">(.*?)</div>',re.findall ( '<div class="lefttx">Examination :</div>(.*?)<div class="aclear"></div>', htmlSource, re.DOTALL)[0], re.DOTALL)[0].strip()
        year=re.findall ('<div class="rightre">(.*?)</div>',re.findall ( '<div class="lefttx">Year :</div>(.*?)<div class="aclear"></div>', htmlSource, re.DOTALL)[0], re.DOTALL)[0].strip()
        name=re.findall ('<div class="rightre">(.*?)</div>',re.findall ( '<div class="lefttx">Name :</div>(.*?)<div class="aclear"></div>', htmlSource, re.DOTALL)[0], re.DOTALL)[0].strip()
        index=re.findall ('<div class="rightre">(.*?)</div>',re.findall ( '<div class="lefttx">Index Number :</div>(.*?)<div class="aclear"></div>', htmlSource, re.DOTALL)[0], re.DOTALL)[0].strip()
        stream=re.findall ('<div class="rightre">(.*?)</div>',re.findall ( '<div class="lefttx">Stream :</div>(.*?)<div class="aclear"></div>', htmlSource, re.DOTALL)[0], re.DOTALL)[0].strip()
        zscore=re.findall ('<div class="rightre">(.*?)</div>',re.findall ( '<div class="lefttx">Z-Score :</div>(.*?)<div class="aclear"></div>', htmlSource, re.DOTALL)[0], re.DOTALL)[0].strip()
        drank=re.findall ('<div class="rightre">(.*?)</div>',re.findall ( '<div class="lefttx">District Rank :</div>(.*?)<div class="aclear"></div>', htmlSource, re.DOTALL)[0], re.DOTALL)[0].strip()
        irank=re.findall ('<div class="rightre">(.*?)</div>',re.findall ( '<div class="lefttx">Island Rank :</div>(.*?)<div class="aclear"></div>', htmlSource, re.DOTALL)[0], re.DOTALL)[0].strip()
        irank=re.findall ('<div class="rightre">(.*?)</div>',re.findall ( '<div class="lefttx">Island Rank :</div>(.*?)<div class="aclear"></div>', htmlSource, re.DOTALL)[0], re.DOTALL)[0].strip()
        return (exam,year,name,index,stream,zscore,drank,irank)

    def clear_layout(self):
        for i in reversed(range(self.horizontalLayout_2.count())): 
                self.horizontalLayout_2.itemAt(i).widget().setParent(None)
        
        
        
        #self.setCentralWidget(self.form_widget)
    def al(self):
        global bu
        self.clear_layout()
        for i in bu:
            exec """self.%s.setStyleSheet('border: none;font: 75 10pt "Arial";font-weight: bold;text-align: left;')"""%(i)
        bu=[]
        bu+=['s_details']
        self.s_details.setStyleSheet('''QPushButton
{
  border: 1px solid red;
  font: 75 10pt "Arial";
 font-weight: bold;
}''')
        self.form_widget.pushButton.clicked.connect(self.b_al)
        self.horizontalLayout_2.addWidget(self.form_widget)
        
    def ol(self):
        global bu
        self.clear_layout()
        for i in bu:
            exec """self.%s.setStyleSheet('border: none;font: 75 10pt "Arial";font-weight: bold;text-align: left;')"""%(i)
        bu=[]
        bu+=['s_enq']
        self.s_enq.setStyleSheet('''QPushButton
{
  border: 1px solid red;
  font: 75 10pt "Arial";
 font-weight: bold;
}''')

        self.horizontalLayout_2.addWidget(self.form_widget)
    def b_al(self):
        thread.start_new_thread( self.proal,('a','b'))


        

    def proal(self,a,b):
        self.clear_layout()
        self.horizontalLayout_2.addWidget(self.form_widget2)
        val=0
        val2=0
        self.form_widget2.progressBar.setValue(val)
        self.form_widget2.label_2.setText('')
        lst=str(self.form_widget.plainTextEdit.toPlainText()).split('\n')

        suc,fail=[],[]
        for i in lst:
          if '-'in i:
              hh=map(int,i.split('-'))
              lst+=[str(i) for i in range(hh[0],hh[1]+1)]
          else:
            try:
                k=100.0/len(lst)
                val2=val2+k
                val=int(val2)
                self.form_widget2.progressBar.setValue(val)
                self.form_widget2.label_2.setText('Getting data for index number '+i)
                data=self.res(i)
                self.form_widget2.label_2.setText('Data received for index number '+i+'\nName - '+data[2])
                self.form_widget2.label_2.setText('')
                print data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7]
                conn.execute(fg)
                conn.commit()
                suc+=[i]
            except Exception as e:
                print e
                fail+=[i]
        self.clear_layout()
        self.horizontalLayout_2.addWidget(self.form_widget2)
        v='Successfully grabbed results for All %s index numbers!'%(len(lst)) if len(fail)==0 else 'Successfully grabbed results for  %s/%s index numbers!\nFailed with %s indexes '%(len(suc),len(lst),len(fail))
        self.form_widget2.label_2.setText(v)
        self.form_widget2.label.setText('Done Grabbing!' )
        self.form_widget2.progressBar.setValue(100)
class alclass(QtGui.QMainWindow, form_class2):
    def __init__(self, parent=None):
        global fn
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
class proclass(QtGui.QMainWindow, form_class3):
    def __init__(self, parent=None):
        global fn
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)

app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
ret=app.exec_()
sys.exit(ret)


