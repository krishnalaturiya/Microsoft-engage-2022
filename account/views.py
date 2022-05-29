from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User , auth
# Create your views here.

def view_attendance(request):
    return render(request,"view_attendance.html")

def Logout(request):
    return redirect('/')


def register(request):
   if request.method =='POST':
       first_name=request.POST['first_name']
       last_name=request.POST['last_name']
       username=request.POST['username']
       password1=request.POST['password1']
       password2=request.POST['password2']
       email=request.POST['email']

       if password1==password2:
          if User.objects.filter(username=username).exists():
            messages.info(request,'Username taken')
            return render(request,'register.html')
          elif User.objects.filter(email=email).exists():
            messages.info(request,'email taken')
            return render(request,'register.html')
          else:

            user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
            user.save();
            messages.info(request,'user created Now login!')
       else:
         messages.info(request,"password not matching ")
         return render(request,'register.html')
       return render(request,'register.html')

   else:
      return render(request,'register.html')
      

def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,"sample.html")
        else:
           messages.info(request,'Inavalid Credentials!!')
           messages.info(request,'Try registering first.')
           return render(request,'index.html')

    else:
      return render(request,'index.html')

def Attendance(request):

  import time
  import pandas as pd
  import cv2
  import numpy as np
  import face_recognition
  import os
  from datetime import datetime
  from datetime import date
  from deepface import DeepFace

  import csv
  base_path=os.getcwd()
  print(base_path)
  
  path2=os.path.join(base_path,"static","total_attendance.csv")
#   f=open(path1,'r+')
  fi=open(path2,'a+')
  def find_encodings(images):
      encodelist=[]
      for img in images:
          img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
          encode=face_recognition.face_encodings(img)[0]
          encodelist.append(encode)
      return encodelist
  namelist = []
  def markattendance(name,emo):
    

    if name not in namelist:
        namelist.append(name)
        now = datetime.now()
        dtString = now.strftime('%H: %M: %S')
        today = date.today()
        d2 = today.strftime("%b-%d-%Y")
        # f.writelines(f'{d2}, {name}, {dtString}, {emo}\n')
        fi.writelines(f'{d2}, {name}, {dtString}, {emo}\n')

  print(base_path)
  path=os.path.join(base_path,"account","Images_attendance")
  images=[]
  classNames=[]
  myList=os.listdir(path)
  #print(myList)
  names=[]
  time=[]
  emotion=[]


  for cls in myList:
      curimg=cv2.imread(f'{path}/{cls}')
      images.append(curimg)
      classNames.append(os.path.splitext(cls)[0])



  encodelistknown=find_encodings(images)
  print("Encoding complete")

  cap = cv2.VideoCapture(0)

  while True:
      success,img = cap.read()
      imgS = cv2.resize(img , (0 , 0) , None , 0.25 , 0.25)
      imgS = cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)

      facescurrframe = face_recognition.face_locations(imgS)
      encodecurrframe = face_recognition.face_encodings(imgS,facescurrframe)

      for encodeface,faceloc in zip(encodecurrframe,facescurrframe):
          matches=face_recognition.compare_faces(encodelistknown,encodeface)
          facedis=face_recognition.face_distance(encodelistknown,encodeface)

          matchindex=np.argmin(facedis)
          if facedis[matchindex]>0.5:
            y1,x2,y2,x1=faceloc
            y1, x2, y2, x1=4*y1,4*x2,4*y2,4*x1
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img,'UNKNOWN !',(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            break
          
          if matches[matchindex]:
              predictions = DeepFace.analyze(imgS, actions=["emotion"], enforce_detection=False)
              name=classNames[matchindex].upper()
              y1,x2,y2,x1=faceloc
              y1, x2, y2, x1=4*y1,4*x2,4*y2,4*x1
              cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
              cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
              cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
              font = cv2.FONT_HERSHEY_SIMPLEX
              cv2.putText(img, predictions['dominant_emotion'], (50, 50), font, 3, (0, 0, 255), 2, cv2.LINE_4)
              print(predictions['dominant_emotion'])
              markattendance(name,predictions['dominant_emotion'])


      cv2.imshow('Webcam',img)
      if cv2.waitKey(2) & 0xFF == ord('q'):
          break

      cv2.waitKey(1)

  cv2.destroyAllWindows()
  cap.release()
#   f.close()
  fi.close()
 



  print("complete")
  return render(request,"sample.html")

    
def Statistics(request):
    import csv
    import matplotlib.pyplot as plt
    import os
    l=[]
    l_date=[]
    filename = 'total_attendance.csv'
    base_path=os.getcwd()
    path=os.path.join(base_path,"static","total_attendance.csv")


    with open(path, 'r') as csvfile:
        datareader = csv. reader(csvfile)
        for row in datareader:
            #print(row)
            if row:
                l.append(row[3])
                l_date.append(row[0])

    # print(l)
    d={}
    for i in range(1,len(l)):
        if l[i] in d:
            d[l[i]]+=1
        else:
            d[l[i]]=1
    
    d_date={}
    for i in range(1,len(l)):
        if l_date[i] in d_date:
            d_date[l_date[i]]+=1
        else:
            d_date[l_date[i]]=1

    dates=list(d_date.keys())
    count_emp=list(d_date.values())

    emo = list(d.keys())
    count = list(d.values())

    fig = plt.figure(figsize=(10, 5))
    
    # creating the bar plot
    plt.subplot(1,2,1)
    plt.bar(emo, count, color='maroon',width=0.4)
    plt.xlabel("Expression analysis ")
    plt.ylabel("No. of employees")
    
    plt.subplot(1,2,2)
    plt.bar(dates,count_emp,color="blue",width=0.4)
    plt.xlabel("Dates ")
    plt.ylabel("No. of employees")
    plt.show()

    return render(request,"sample.html")

