# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui, uic
import mainwindow,sys,al,p,time,save
import urllib,re
import sqlite3,thread
form_class = mainwindow.Ui_MainWindow
form_class2=al.Ui_Form
form_class3=p.Ui_Form
form_class4=save.Ui_Form
global bu
bu=[]
class MyWindowClass(QtGui.QMainWindow, form_class):
    
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.s_details.clicked.connect(self.al)
        self.s_enq_2.clicked.connect(self.save)
        self.s_enq.clicked.connect(self.ol)
        #self.ex_details.clicked.connect(self.exam_details)
 
        self.form_widget = alclass(self)
        self.form_widget2 = proclass(self)
        self.form_widget3 = saveclass(self)
        #self.form_widget2 = details_exam_class(self)
        self.html='''
<html>
<head>
<style>

body {
	background: #fafafa url(http://jackrugile.com/images/misc/noise-diagonal.png);
	color: #444;
	font: 100%/30px 'Helvetica Neue', helvetica, arial, sans-serif;
	text-shadow: 0 1px 0 #fff;
}

strong {
	font-weight: bold; 
}

em {
	font-style: italic; 
}

table {
	background: #f5f5f5;
	border-collapse: separate;
	box-shadow: inset 0 1px 0 #fff;
	font-size: 12px;
	line-height: 24px;
	margin: 30px auto;
	text-align: left;
	width: 800px;
}	

th {
	background: url(http://jackrugile.com/images/misc/noise-diagonal.png), linear-gradient(#777, #444);
	border-left: 1px solid #555;
	border-right: 1px solid #777;
	border-top: 1px solid #555;
	border-bottom: 1px solid #333;
	box-shadow: inset 0 1px 0 #999;
	color: #fff;
  font-weight: bold;
	padding: 10px 15px;
	position: relative;
	text-shadow: 0 1px 0 #000;	
}

th:after {
	background: linear-gradient(rgba(255,255,255,0), rgba(255,255,255,.08));
	content: '';
	display: block;
	height: 25%;
	left: 0;
	margin: 1px 0 0 0;
	position: absolute;
	top: 25%;
	width: 100%;
}

th:first-child {
	border-left: 1px solid #777;	
	box-shadow: inset 1px 1px 0 #999;
}

th:last-child {
	box-shadow: inset -1px 1px 0 #999;
}

td {
	border-right: 1px solid #fff;
	border-left: 1px solid #e8e8e8;
	border-top: 1px solid #fff;
	border-bottom: 1px solid #e8e8e8;
	padding: 10px 15px;
	position: relative;
	transition: all 300ms;
}

td:first-child {
	box-shadow: inset 1px 0 0 #fff;
}	

td:last-child {
	border-right: 1px solid #e8e8e8;
	box-shadow: inset -1px 0 0 #fff;
}	

tr {
	background: url(http://jackrugile.com/images/misc/noise-diagonal.png);	
}

tr:nth-child(odd) td {
	background: #f1f1f1 url(http://jackrugile.com/images/misc/noise-diagonal.png);	
}

tr:last-of-type td {
	box-shadow: inset 0 -1px 0 #fff; 
}

tr:last-of-type td:first-child {
	box-shadow: inset 1px -1px 0 #fff;
}	

tr:last-of-type td:last-child {
	box-shadow: inset -1px -1px 0 #fff;
}	

tbody:hover td {
	color: transparent;
	text-shadow: 0 0 3px #aaa;
}

tbody:hover tr:hover td {
	color: #444;
	text-shadow: 0 1px 0 #fff;
}
</style>
</head>
<body>

'''

    def findkey(self):
        link='http://www.doenets.lk/result/alresult.jsf'
        sock = urllib.urlopen(link) 
        htmlSource = sock.read()                            
        sock.close()
        key=re.findall ('<input type="hidden" name="javax.faces.ViewState" id="javax.faces.ViewState" value="(.*?)" autocomplete="off" />',htmlSource, re.DOTALL)[0].strip()
        return key
        
    def res(self,index):
        ky=self.findkey()
        ky=urllib.quote_plus(self.findkey())
        link=r'http://www.doenets.lk/result/alresult.jsf?frm=frm&frm%3Ausername='+index+'&frm%3AbtnSubmit=&javax.faces.ViewState='+ky
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
        h1=re.findall ('<tbody(.*?)</tbody>',htmlSource, re.DOTALL)[0]
        sub1=re.findall ('<td role="gridcell">(.*?)</td>',re.findall ('<tr data-ri="0" class="ui-widget-content ui-datatable-even" role="row">(.*?)</tr>',h1,re.DOTALL)[0], re.DOTALL)
        sub2=re.findall ('<td role="gridcell">(.*?)</td>',re.findall ('<tr data-ri="1" class="ui-widget-content ui-datatable-odd" role="row">(.*?)</tr>',h1,re.DOTALL)[0], re.DOTALL)
        sub3=re.findall ('<td role="gridcell">(.*?)</td>',re.findall ('<tr data-ri="2" class="ui-widget-content ui-datatable-even" role="row">(.*?)</tr>',re.findall ('<tbody(.*?)</tbody>',htmlSource, re.DOTALL)[0],re.DOTALL)[0], re.DOTALL)
        sub4=re.findall ('<td role="gridcell">(.*?)</td>',re.findall ('<tr data-ri="3" class="ui-widget-content ui-datatable-odd" role="row">(.*?)</tr>',re.findall ('<tbody(.*?)</tbody>',htmlSource, re.DOTALL)[0],re.DOTALL)[0], re.DOTALL)
        sub5=re.findall ('<td role="gridcell">(.*?)</td>',re.findall ('<tr data-ri="4" class="ui-widget-content ui-datatable-even" role="row">(.*?)</tr>',re.findall ('<tbody(.*?)</tbody>',htmlSource, re.DOTALL)[0],re.DOTALL)[0], re.DOTALL)


        return (exam,year,name,index,stream,zscore,drank,irank,sub1,sub2,sub3,sub4,sub5)

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

    def save(self):
        global bu
        self.form_widget3.pushButton.clicked.connect(self.b_save_al)
        self.form_widget3.pushButton_3.clicked.connect(self.b_save_sub_al)
        self.form_widget3.pushButton_5.clicked.connect(self.b_save_all_al)
        self.form_widget3.pushButton_6.clicked.connect(self.b_save_with_grade_al)
        
        self.clear_layout()
        for i in bu:
            exec """self.%s.setStyleSheet('border: none;font: 75 10pt "Arial";font-weight: bold;text-align: left;')"""%(i)
        bu=[]
        bu+=['s_enq_2']
        self.s_enq_2.setStyleSheet('''QPushButton
{
  border: 1px solid red;
  font: 75 10pt "Arial";
 font-weight: bold;
}''')


        self.horizontalLayout_2.addWidget(self.form_widget3)
        
    def b_al(self):
        thread.start_new_thread( self.proal,('a','b'))

    def b_save_al(self):  
        conn = sqlite3.connect('results.db')
        fg="select distinct stream from result"
        data=conn.execute(fg)
        x=data.fetchall()
        print x
        for i in x:
            hh=self.html[:-1]+'''<table><caption><h1>Advanced Level Results of %s stream Order By Z-Score</h1></caption>
  <thead>
    <tr>
      <th>Index Number</th>
      <th>Name</th>
      <th>Stream</th>
      <th>Z-Score</th>
      <th>District Rank</th>
      <th>Island Rank</th>
    </tr>
  </thead>
   <tbody>
<p>'''%(i[0])
            c="select * from result where stream='%s' order by irank ASC"%(i[0])
            data=conn.execute(c)
            data=data.fetchall() 
            for j in data:
                hh+='''
<tr>
      <td><strong>%s</strong></td>
      <td>%s</td>
      <td>%s</td>
      <td>%s</td>
      <td>%s</td>
      <td>%s</td>

</tr>

'''%(j[0],j[3],j[4],j[5],j[6],j[7])

            hh+='''</tbody>
</table></body></html>'''
            f=open('%s.html'%(i[0]),'w')
            f.write(hh)
            f.close()
        self.form_widget3.label_2.setText('Saved Successfully!')
  
    def b_save_sub_al(self):
        conn = sqlite3.connect('results.db')
        fg="select distinct stream from result"
        data=conn.execute(fg)
        x=data.fetchall()
        for i in x:
            conn = sqlite3.connect('results.db')
            fg="select distinct(subname) from subs where stream='%s'"%(i[0])
            data=conn.execute(fg)
            y=data.fetchall()
            hh=self.html[:-1]+'''<table><caption><h1>Advanced Level Results of subjects for %s stream</h1> </caption>
  <thead>
    <tr>
      <th>Suject Name</th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>S</th>
    </tr>
  </thead>
   <tbody>
<p>'''%(i[0])
            for j in y:
                count="select count(pass) from subs where stream='%s' and subname='%s' and pass='A'"%(i[0],j[0])
                data=conn.execute(count)
                A=data.fetchall()[0][0]
                count="select count(pass) from subs where stream='%s' and subname='%s' and pass='B'"%(i[0],j[0])
                data=conn.execute(count)
                B=data.fetchall()[0][0]
                count="select count(pass) from subs where stream='%s' and subname='%s' and pass='C'"%(i[0],j[0])
                data=conn.execute(count)
                C=data.fetchall()[0][0]
                count="select count(pass) from subs where stream='%s' and subname='%s' and pass='S'"%(i[0],j[0])
                data=conn.execute(count)
                S=data.fetchall()[0][0]
                hh+='''
<tr>
      <td><strong>%s</strong></td>
      <td>%s</td>
      <td>%s</td>
      <td>%s</td>
      <td>%s</td>
</tr>

'''%(j[0],A,B,C,S)

            hh+='''</tbody>
</table></body></html>'''
            f=open('%s stream results by subjects.html'%(i[0]),'w')
            f.write(hh)
            f.close()
        self.form_widget3.label_2.setText('Saved Successfully!')

    def b_save_all_al(self):
        conn = sqlite3.connect('results.db')
        hh=self.html[:-1]+'''<table><caption><h1>Advanced Level Results of all streams Order By Z-Score</h1></caption>
  <thead>
    <tr>
      <th>Index Number</th>
      <th>Name</th>
      <th>Stream</th>
      <th>Z-Score</th>
      <th>District Rank</th>
      <th>Island Rank</th>
    </tr>
  </thead>
   <tbody>
<p>'''
        c="select * from result order by zscore DESC"
        data=conn.execute(c)
        data=data.fetchall() 
        for j in data:
                hh+='''
<tr>
      <td><strong>%s</strong></td>
      <td>%s</td>
      <td>%s</td>
      <td>%s</td>
      <td>%s</td>
      <td>%s</td>

</tr>

'''%(j[0],j[3],j[4],j[5],j[6],j[7])

        hh+='''</tbody>
</table></body></html>'''
        f=open('All streams results order by Z score.html','w')
        f.write(hh)
        f.close()
        self.form_widget3.label_2.setText('Saved Successfully!')

    def b_save_with_grade_al(self):
        conn = sqlite3.connect('results.db')
        fg="select distinct stream from result"
        data=conn.execute(fg)
        x=data.fetchall()
        print x
        for i in x:
            hh=self.html[:-1]+'''<table><caption><h1>Advanced Level Results of %s stream with Grades Obtained Order By Z-Score</h1></caption>
  <thead>
    <tr>
      <th>Index Number</th>
      <th>Name</th>
      <th>Stream</th>
      <th>Sub 1</th>
      <th>Sub 2</th>
      <th>Sub 3</th>
      <th>Sub 4</th>
      <th>Sub 5</th>
      <th>Z-Score</th>
      <th>District Rank</th>
      <th>Island Rank</th>
      
    </tr>
  </thead>
   <tbody>
<p>'''%(i[0])
            c="select * from result where stream='%s' order by irank ASC"%(i[0])
            data=conn.execute(c)
            data=data.fetchall() 
            for j in data:
                c="select subname,pass from subs where `index`='%s'"%(j[0])
                data=conn.execute(c)
                res=data.fetchall()
                c= res
                hh+='''
<tr>
      <td><strong>%s</strong></td>
      <td>%s</td>
      <td>%s</td>
      <td>%s- <br><b><font color="red">%s</font></b></td>
      <td>%s- <br><b><font color="red">%s</font></b></td>
      <td>%s- <br><b><font color="red">%s</font></b></td>
      <td>%s- <br><b><font color="red">%s</font></b></td>
      <td>%s- <br><b><font color="red">%s</font></b></td>
      <td>%s</td>
      <td>%s</td>
      <td>%s</td>

</tr>

'''%(j[0],j[3],j[4], c[1][0],c[1][1],c[-1][0],c[-1][1],c[-2][0],c[-2][1],c[-3][0],c[-3][1],c[0][0],c[0][1],j[5],j[6],j[7])

            hh+='''</tbody>
</table></body></html>'''
            f=open('%s resutls with Grades Obtained.html'%(i[0]),'w')
            f.write(hh)
            f.close()
        self.form_widget3.label_2.setText('Saved Successfully!')
          

    def proal(self,a,b):
        self.s_details.setEnabled(False)
        self.s_enq.setEnabled(False)
        self.s_enq_2.setEnabled(False)
        conn = sqlite3.connect('results.db')

        conn.execute('CREATE TABLE IF NOT EXISTS result(`index` varchar(10)primary key,`exam` varchar (100),`year` int(5),`name` varchar (100),`stream` varchar(50), `zscore` varchar(10),`drank` int(5),`irank` int(6))')
        conn.execute('CREATE TABLE IF NOT EXISTS subs(`index` varchar(10),`stream` varchar(50),`subname` varchar(50),`pass` varchar(3) ,primary key(`index`,`subname`))')
        conn.commit()
        self.clear_layout()
        self.horizontalLayout_2.addWidget(self.form_widget2)
        val=0
        val2=0
        self.form_widget2.progressBar.setValue(val)
        self.form_widget2.label_2.setText('')
        lst=str(self.form_widget.plainTextEdit.toPlainText()).split('\n')
        f=open('result.txt','w')
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
                fg="insert into result(`exam`,`year`,`name`,`index`,`stream`,`zscore`,`drank`,`irank`) values ('%s','%s','%s','%s','%s','%s','%s','%s')"%(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7])
                conn.execute(fg)

                conn.commit()
                data='''
Name- %s\n
Index number- %s\n
Stream- %s\n
Z Score- %s\n
District Rank- %s\n
Island Rank- %s\n\n
'''%(data[2],data[3],data[4],data[5],data[6],data[7])
                f.write(data)
                suc+=[i]
            except:
                fail+=[i]
            try:
                data=self.res(i)
                for i in range(1,6):
                    fg="insert into subs(`index`,`stream`,`subname`,`pass`) values ('%s','%s','%s','%s')"%(data[3],data[4],data[-1*i][0],data[-1*i][1])
                    conn.execute(fg)
                    conn.commit()
            except:
                pass
        self.clear_layout()
        self.horizontalLayout_2.addWidget(self.form_widget2)
        v='Successfully grabbed results for All %s index numbers!'%(len(lst)) if len(fail)==0 else 'Successfully grabbed results for  %s/%s index numbers!\nFailed with %s indexes '%(len(suc),len(lst),len(fail))
        self.form_widget2.label_2.setText(v)
        self.form_widget2.label.setText('Done Grabbing!' )
        self.form_widget2.progressBar.setValue(100)
        self.s_details.setEnabled(True)
        self.s_enq.setEnabled(True)
        self.s_enq_2.setEnabled(True)



    

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

class saveclass(QtGui.QMainWindow, form_class4):
    def __init__(self, parent=None):
        global fn
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)

app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
ret=app.exec_()
sys.exit(ret)


