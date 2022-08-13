from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
from App_data import WeekKmData,SunKmData,SatKmData
from decimal import Decimal
import os,time

path=os.path.dirname(__file__)+"/App_data/"
HDA_NDA_path=os.path.dirname(__file__)+"/Your_HDA_NDA_Data/"
file=open(HDA_NDA_path+'HDA.csv','r'); l=len(file.readlines()); file.close()

def LoadData():
	file=open(HDA_NDA_path+'HDA.csv','r'); l=len(file.readlines()); file.close(); messagebox.showinfo('Entry Saved','Currently '+str(l-1)+' Entries in database')
	if combo1.get()=='RUN':
		dutydate=txt1.get(); dutyno=txt.get()
		if combo.get()=='WEEK':
			d=WeekKmData.weekkms; file=open(path+'WeekSignOnOff.txt','r'); SignOnOff=file.readlines(); file.close()			
		elif combo.get()=='SAT':
			d=SatKmData.satkms; file=open(path+'SatSignOnOff.txt','r'); SignOnOff=file.readlines(); file.close()
		elif combo.get()=='SUN':
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
		tbox.delete(1.0,END)
		tbox.insert(INSERT,'Date:          '+dutydate+'\nDutyNo:        '+dutyno+'\nDutyType:      RUN'+'\nKm:            '+\
			d[int(dutyno)]+'\nDeviation:     0\nRemarks:       -\n'+DutySignOnOff)
		
	elif combo1.get()=='Other':
		dutydate=txt1.get()
		tbox.delete(1.0,END)
		tbox.insert(INSERT,'Date:          '+dutydate+'\nDutyNo:        -\nDutyType:      Other\nKm:            0\nDeviation:     0\nRemarks:       -\nSignOff_Sched: NA/NA\nSignOff_Act:   NA/NA')

def SaveData():
	dutydata=tbox.get(1.0, END)
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

	res=messagebox.askyesno('Duty Data','Save following data?\n\n'+'Date:                 '+dutydate+'\nDutyNo:            '+dutyno+\
		'\nDutyType:        '+dutytype+'\nKm:                   '+dutykm+'\nDeviation:         '+deviation+'\nActualKm:        '+str(round(Decimal(dutykm)+Decimal(deviation),1))+\
		'\nRemark:             '+remark+'\n'+dutydata.split('\n')[6]+'\n'+dutydata.split('\n')[7]+'\nNDA:                  '+nda)
	if res:
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
		messagebox.showinfo('Data Saved','Data saved successfully')
		file=open(HDA_NDA_path+'HDA.csv','r'); l=len(file.readlines()); file.close(); txt1.delete(0,END); txt1.insert(INSERT,str(l)+time.strftime('/%m/%Y'))

def cleardata():
	res1=messagebox.askyesno('Confirmation','All HDA/NDA data will be deleted, \nhave you taken backup of your data?')
	if res1:
		res2=messagebox.askyesno('Confirm again','CLear and reset all HDA/NDA data, \nI have taken backup!')
		if res2:
			hdafile=open(HDA_NDA_path+'HDA.csv','w'); hdafile.write('Date,Duty no,Duty Type,Km,Deviation,Actual Km\n'); hdafile.close()
			ndafile=open(HDA_NDA_path+'NDA.csv','w'); ndafile.write('Date,Duty no,SignOn/Off Time Schuled,SignOn/Off Place Scheuled,SignOn/Off Time Actual,SignOn/Off Place Actual,Full Night,Before 0400 or after 0000,0401-0500 or 2301-2359,0501-0600 or 2201-2300,Remarks\n'); ndafile.close()
			messagebox.showinfo('Cleared successfully',"Your HDA/NDA data cleared successfully, \nready to accept new month's data")
			txt1.delete(0,END); txt1.insert(INSERT,'1'+time.strftime('/%m/%Y'))

window = Tk()
f1=Frame(window)
lbl1 = Label(f1, text="Date "); lbl1.pack(side=LEFT)
txt1 = Entry(f1,width=10); txt1.pack(side=LEFT,padx=5); txt1.insert(INSERT,str(l)+time.strftime('/%m/%Y'))
f1.pack(pady=20)
f2=Frame(window)
lbl = Label(f2, text="Duty#"); lbl.pack(side=LEFT)
txt = Entry(f2,width=9); txt.pack(side=LEFT,padx=5)
f2.pack(pady=20)
f3=Frame(window)
lbl2 = Label(f3, text="TT    "); lbl2.pack(side=LEFT)
combo = Combobox(f3,width=5); combo['values']= ('WEEK','SAT','SUN'); combo.current(0); combo.pack(side=LEFT)
f3.pack(pady=20)
f4=Frame(window)
lbl3 = Label(f4, text="Type"); lbl3.pack(side=LEFT)
combo1 = Combobox(f4,width=5); combo1['values']= ('RUN','Other'); combo1.current(0); combo1.pack(side=LEFT)
f4.pack(pady=20)
btn1=Button(window, text="Fetch Data",width=10,command=LoadData); btn1.pack(pady=10)
tbox = ScrolledText(window, height=10,width=30) ; tbox.pack()
btn = Button(window, text="Save",width=7,command=SaveData	); btn.pack(pady=10)
btn2 = Button(window, text="Clear HDA_NDA Data",width=20,command=cleardata); btn2.pack(pady=100)
window.mainloop()
