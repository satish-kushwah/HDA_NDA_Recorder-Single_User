import urllib.request,os,time
path=os.path.dirname(__file__)+"/App_data/" 
c=int(input('Enter 1 to update WeekData, 2 to update SatData, 3 to update SunData: '))
print('Updating databse, please wait...')
if c==1:
  try:    
    link= "https://drive.google.com/uc?id=1yFSfYm5Bx6w1hOGwAmQc_pfgWiZtsDTa&export=download"
    request_url = urllib.request.urlopen(link)
    f=open(path+'WeekTripsData.py','w') 
    f.write(request_url.read().decode('utf-8').replace('\r\n','\n'))
    f.close()
    link= "https://drive.google.com/uc?id=1V9rOUSyuQrYxisnqANZRHtx0NI_64r53&export=download"
    request_url = urllib.request.urlopen(link)
    f=open(path+'WeekKmData.py','w') 
    f.write(request_url.read().decode('utf-8').replace('\r\n','\n'))
    f.close()
    link= "https://drive.google.com/uc?id=1PCup_pbVkgyVKKtukOnpIVOTISlLkQwk&export=download"
    request_url = urllib.request.urlopen(link)
    f=open(path+'WeekSignOnOff.txt','w') 
    f.write(request_url.read().decode('utf-8').replace('\r\n','\n'))
    f.close()
  except:
    input('Could not connect to database, check your connection, press enter to exit')
    quit()
elif c==2:
  try:
    link= "https://drive.google.com/uc?id=12Oq6aR0PDcrxkzDyzsF-4rnztT-GZIXa&export=download"
    request_url = urllib.request.urlopen(link)
    f=open(path+'SatTripsData.py','w') 
    f.write(request_url.read().decode('utf-8').replace('\r\n','\n'))
    f.close()
    link= "https://drive.google.com/uc?id=1q1UrR7KSmPOm5dbc1WhKv_U8ac2eVGxM&export=download"
    request_url = urllib.request.urlopen(link)
    f=open(path+'SatKmData.py','w') 
    f.write(request_url.read().decode('utf-8').replace('\r\n','\n'))
    f.close()
    link= "https://drive.google.com/uc?id=1QXo-jApdcRcWHO_mCB7JGdEuqavzMIiZ&export=download"
    request_url = urllib.request.urlopen(link)
    f=open(path+'SatSignOnOff.txt','w') 
    f.write(request_url.read().decode('utf-8').replace('\r\n','\n'))
    f.close()
  except:
    input('Could not connect to database, check your connection, press enter to exit')
    quit()
elif c==3:
  try:
    link= "https://drive.google.com/uc?id=1HGevb4belecQqfqoBGAxA2SSQtkrpV77&export=download"
    request_url = urllib.request.urlopen(link)
    f=open(path+'SunTripsData.py','w') 
    f.write(request_url.read().decode('utf-8').replace('\r\n','\n'))
    f.close()
    link= "https://drive.google.com/uc?id=12nXAUGA6eU78DEdmJeFEL4oBnMpkGYFG&export=download"
    request_url = urllib.request.urlopen(link)
    f=open(path+'SunKmData.py','w') 
    f.write(request_url.read().decode('utf-8').replace('\r\n','\n'))
    f.close()
    link= "https://drive.google.com/uc?id=1D2-bZu57jFaEKawssR75m3u2QmK_tosc&export=download"
    request_url = urllib.request.urlopen(link)
    f=open(path+'SunSignOnOff.txt','w') 
    f.write(request_url.read().decode('utf-8').replace('\r\n','\n'))
    f.close()
  except:
    input('Could not connect to database, check your connection, press enter to exit')
    quit()
else:
  input('Wrong choice, Press enter to exit')
  quit()

input('Database successfully updated, Press enter to exit')