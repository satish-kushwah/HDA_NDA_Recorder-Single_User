# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HDA_NDA_calc.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
#importing stuff
from App_data import WeekKmData,SunKmData,SatKmData
from decimal import Decimal
import os,time

path=os.path.dirname(__file__)+"/App_data/"
HDA_NDA_path=os.path.dirname(__file__)+"/Your_HDA_NDA_Data/"
file=open(HDA_NDA_path+'HDA.csv','r'); l=len(file.readlines()); file.close()
#

class Ui_MainWindow(QtWidgets.QMainWindow): #change made in this line from designer's code
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(359, 568)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 40, 47, 13))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.duty_date = QtWidgets.QLineEdit(self.centralwidget)
        self.duty_date.setGeometry(QtCore.QRect(150, 40, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.duty_date.setFont(font)
        self.duty_date.setObjectName("duty_date")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 80, 51, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.duty_no = QtWidgets.QLineEdit(self.centralwidget)
        self.duty_no.setGeometry(QtCore.QRect(150, 80, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.duty_no.setFont(font)
        self.duty_no.setObjectName("duty_no")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 120, 47, 13))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.tt = QtWidgets.QComboBox(self.centralwidget)
        self.tt.setGeometry(QtCore.QRect(150, 120, 69, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tt.setFont(font)
        self.tt.setObjectName("tt")
        self.tt.addItem("")
        self.tt.addItem("")
        self.tt.addItem("")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 160, 41, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.duty_type = QtWidgets.QComboBox(self.centralwidget)
        self.duty_type.setGeometry(QtCore.QRect(150, 160, 69, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.duty_type.setFont(font)
        self.duty_type.setObjectName("duty_type")
        self.duty_type.addItem("")
        self.duty_type.addItem("")
        self.fetch_data = QtWidgets.QPushButton(self.centralwidget)
        self.fetch_data.setGeometry(QtCore.QRect(130, 200, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.fetch_data.setFont(font)
        self.fetch_data.setObjectName("fetch_data")
        self.hda_nda_data = QtWidgets.QTextEdit(self.centralwidget)
        self.hda_nda_data.setGeometry(QtCore.QRect(50, 250, 271, 161))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.hda_nda_data.setFont(font)
        self.hda_nda_data.setObjectName("hda_nda_data")
        self.save_data = QtWidgets.QPushButton(self.centralwidget)
        self.save_data.setGeometry(QtCore.QRect(130, 430, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.save_data.setFont(font)
        self.save_data.setObjectName("save_data")
        self.delete_data = QtWidgets.QPushButton(self.centralwidget)
        self.delete_data.setGeometry(QtCore.QRect(30, 480, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.delete_data.setFont(font)
        self.delete_data.setObjectName("delete_data")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 359, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #connecting buttons
        self.fetch_data.clicked.connect(self.LoadData)
        self.save_data.clicked.connect(self.SaveData)
        self.delete_data.clicked.connect(self.cleardata)
        #
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Date"))
        self.label_2.setText(_translate("MainWindow", "Duty#"))
        self.label_3.setText(_translate("MainWindow", "TT"))
        self.tt.setItemText(0, _translate("MainWindow", "WEEK"))
        self.tt.setItemText(1, _translate("MainWindow", "SAT"))
        self.tt.setItemText(2, _translate("MainWindow", "SUN"))
        self.label_4.setText(_translate("MainWindow", "Type"))
        self.duty_type.setItemText(0, _translate("MainWindow", "RUN"))
        self.duty_type.setItemText(1, _translate("MainWindow", "Other"))
        self.fetch_data.setText(_translate("MainWindow", "Fetch Data"))
        self.save_data.setText(_translate("MainWindow", "Save"))
        self.delete_data.setText(_translate("MainWindow", "Clear HDA_NDA DATA"))
        #inserting date
        self.duty_date.setText(str(l)+time.strftime('/%m/%Y'))
        #

    #defing button functions
    def LoadData(self):
        file=open(HDA_NDA_path+'HDA.csv','r'); l=len(file.readlines()); file.close(); QMessageBox.about(self,'Entry Saved',"Currently "+str(l-1)+" Entries in database")
        if self.duty_type.currentText()=='RUN':
            dutydate=self.duty_date.text(); dutyno=self.duty_no.text()
            if self.tt.currentText()=='WEEK':
                d=WeekKmData.weekkms; file=open(path+'WeekSignOnOff.txt','r'); SignOnOff=file.readlines(); file.close()         
            elif self.tt.currentText()=='SAT':
                d=SatKmData.satkms; file=open(path+'SatSignOnOff.txt','r'); SignOnOff=file.readlines(); file.close()
            elif self.tt.currentText()=='SUN':
                d=SunKmData.sunkms; file=open(path+'SunSignOnOff.txt','r'); SignOnOff=file.readlines(); file.close()
            
            SignOn=SignOnOff[int(dutyno)-1].split('\t')[1]; SignOff=SignOnOff[int(dutyno)-1].split('\t')[3]
            if len(SignOn)==4: SignOn='0'+SignOn
            if len(SignOff)==4: SignOff='0'+SignOff
            if '04:00'<=SignOn<='06:00':
                DutySignOnOff=SignOn+'/'+SignOnOff[int(dutyno)-1].split('\t')[2]
                DutySignOnOff='SignOn_Sched:  '+DutySignOnOff+'\nSignOn_Act:    '+DutySignOnOff
            else:
                DutySignOnOff=SignOff+'/'+SignOnOff[int(dutyno)-1].split('\t')[4][0:-1]
                DutySignOnOff='SignOff_Sched: '+DutySignOnOff+'\nSignOff_Act:   '+DutySignOnOff
            self.hda_nda_data.clear()
            self.hda_nda_data.setText('Date:          '+dutydate+'\nDutyNo:       '+dutyno+'\nDutyType:    RUN'+'\nKm:            '+\
                d[int(dutyno)]+'\nDeviation:    0\nRemarks:     -\n'+DutySignOnOff)
            
        elif self.duty_type.currentText()=='Other':
            dutydate=self.duty_date.text()
            self.hda_nda_data.clear()
            self.hda_nda_data.setText('Date:          '+dutydate+'\nDutyNo:        -\nDutyType:      Other\nKm:            0\nDeviation:     0\nRemarks:       -\nSignOff_Sched: NA/NA\nSignOff_Act:   NA/NA')

    def SaveData(self):
        dutydata=self.hda_nda_data.toPlainText()
        dutydate=dutydata.split('\n')[0].split()[1]
        dutyno=dutydata.split('\n')[1].split()[1]
        dutytype=dutydata.split('\n')[2].split()[1].upper()
        dutykm=dutydata.split('\n')[3].split()[1]
        deviation=dutydata.split('\n')[4].split()[1]
        remark=dutydata.split('\n')[5].split()[1]
        SignOnOffTimeSched=dutydata.split('\n')[6].split()[1].split('/')[0]
        SignOnOffTimeAct=dutydata.split('\n')[7].split()[1].split('/')[0]
        nda1='-'; nda2='-'; nda3='-'; nda4='-'
        if dutytype=='NIGHT': 
            nda1='Y'; nda='A'
        elif '00:00'<=SignOnOffTimeAct<='02:00': 
            nda2='Y'; nda='B'
        elif '04:00'<SignOnOffTimeAct<='05:00' or '23:01'<=SignOnOffTimeAct<='23:59': 
            nda3='Y'; nda='C'
        elif '05:01'<=SignOnOffTimeAct<='06:00' or '22:01'<=SignOnOffTimeAct<='23:00': 
            nda4='Y'; nda='D'
        else: 
            nda='NA'; ndastr='-,-,-,-,-,-,-,-,-,-,'+remark+'\n'
        
        res = QMessageBox.question(self,'Duty Data','Save following data?\n\n'+'Date:                 '+dutydate+'\nDutyNo:            '+dutyno+\
            '\nDutyType:        '+dutytype+'\nKm:                   '+dutykm+'\nDeviation:         '+deviation+'\nActualKm:        '+str(round(Decimal(dutykm)+Decimal(deviation),1))+\
            '\nRemark:             '+remark+'\n'+dutydata.split('\n')[6]+'\n'+dutydata.split('\n')[7]+'\nNDA:                  '+nda, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if res==QMessageBox.Yes:
            file=open(HDA_NDA_path+'HDA.csv','a')
            file.write(dutydate+','+dutyno+','+dutytype+','+dutykm+','+deviation+','+str(round(Decimal(dutykm)+Decimal(deviation),1))+'\n')
            file.close()
            file=open(HDA_NDA_path+'NDA.csv','a')
            if nda=='NA':
                file.write(ndastr)
            else:
                file.write(dutydate+','+dutyno+','+dutydata.split('\n')[6].split()[1].split('/')[0]+','+dutydata.split('\n')[6].split()[1].split('/')[1]+\
                ','+dutydata.split('\n')[7].split()[1].split('/')[0]+','+dutydata.split('\n')[7].split()[1].split('/')[1]+','+nda1+','+nda2+','+nda3+','+nda4+','+remark+'\n')
            file.close()
            QMessageBox.about(self,'Data Saved','Data saved successfully')
            file=open(HDA_NDA_path+'HDA.csv','r'); l=len(file.readlines()); file.close(); self.duty_date.clear(); self.duty_date.setText(str(l)+time.strftime('/%m/%Y'))

    def cleardata(self):
        res1=QMessageBox.question(self,'Confirmation','All HDA/NDA data will be deleted, \nhave you taken backup of your data?',QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if res1==QMessageBox.Yes:
            res2=QMessageBox.question(self,'Confirm again','CLear and reset all HDA/NDA data, \nI have taken backup!',QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if res2==QMessageBox.Yes:
                hdafile=open(HDA_NDA_path+'HDA.csv','w'); hdafile.write('Date,Duty no,Duty Type,Km,Deviation,Actual Km\n'); hdafile.close()
                ndafile=open(HDA_NDA_path+'NDA.csv','w'); ndafile.write('Date,Duty no,SignOn/Off Time Schuled,SignOn/Off Place Scheuled,SignOn/Off Time Actual,SignOn/Off Place Actual,Full Night,Before 0400 or after 0000,0401-0500 or 2301-2359,0501-0600 or 2201-2300,Remarks\n'); ndafile.close()
                QMessageBox.about(self,'Cleared successfully',"Your HDA/NDA data cleared successfully, \nready to accept new month's data")
                self.duty_date.clear(); self.duty_date.setText('1'+time.strftime('/%m/%Y'))
    #

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

