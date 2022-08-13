# HDA_NDA_Recorder-Single_User
GUI app for recording HDA_NDA data of TO

1. Date is auto filled, edit if required, If you are given a duty no from CC just enter duty no 
   in Duty# text box, select TimeTable from TT leave duty type to RUN, click on Fetch data buttton,
   data will be fetched from database, when you click Fetch Data button number of entries already made by
   you will be displayed

2. In the bottom text box, you can edit data if actual data varies from fetched one, 
   like duty no is WD/NIGHT/PRT (mind the spellings) instead of RUN then edit if required, 
   you can also put some remark in case of late sitting or deviation, you can change Km data 
   and deviation in Km with + or - sign  also actual SignOnOff Time/Place, dont forget to keep 
   the format hh:mm/Place

3. Then click save button, you will see data which will be saved and NDA you will get 
   e.g. A/B/C/D or NA if no NDA to be given, if you want to save data click YES or NO if you 
   want to edit again. When data is saved, a mesaage will pop up that Data is saved successfully otherwise Data is not saved

4. Data once saved can not be edited, so be sure before saving and clicking YES.

5. If you are on Rest/CR/CL/EL/Other, enter date and select duty type Other, click Fetch Data, 
   now edit duty type as Rest/CR/CL/EL/Other

6. Your data is being saved to 2 files HDA.csv and NDA.csv, dont edit these files with any other app,
   although you can open these files with other apps but dont edit them with other apps

7. Run create_excel_v1.11 to create excel in "Your_HDA_NDA_Data" folder

8. For saving next months data click bottom button Clear_HDA_NDA_Data, when you click this button
   your existing HDA.csv and NDA.csv file data will be cleared, take backup of these files if you need them later
