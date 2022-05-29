
# Attendance - Emotion Tracker

This is a facial-recognition based attendance-emotion tracker web app. It is a great tool to track sentiments at the same time while taking their attendance of people working in same environment. 
## Tech Stack

Python

Django framework

HTML

CSS

Javascript

Node.js


# Modules and Libraries required

1.Deepface

2.pandas

3.numpy

4.cv2

5.face_recognition

6.os

7.datetime

8.deepface

9.csv

10.matplotlib

11.dilib
## How to run the project

1.Install and setup django (You can refer this: https://youtu.be/VuETrwKYLTM)

2.Install all the dependencies stated above using : pip install 'library_name'

3.In the command line locate to the folder you cloned this repository in and then run "python manage.py runserver".
(If using a virtual environment do not forget to switch to that)

4.A link like " http://127.0.0.1:8000/ " will be generated.Click on it and you are ready to see the web app.
## How to use this project
It is supposed to be used for taking attendance of a a bunch of people working togeter on daily basis. 
User who is head of the organization needs to register himself/herself first and then login using those credentials.
In the back-end that user needs to add the images of all the employees in the folder /account/Images_attendance in jpg/jpeg form for the model to refer to encodings of those images and compare to the one currently in front of camera.
If the minimum face distance is > 0.5 then the person is marked unknown and the head would need to interfere.
If the minimum face distance is < 0.5 ,it marks date,name,time,emotion of a person standing in front of frame and stores it in total_attendance.csv folder in static folder.

## Corner cases:
1.When a code is run once,it will mark his/her attendance only once , no matter how many times the person comes in front of the camera.
2.If a person's picture is not stored in Images_attendance folder the person's attendance would not be marked and he/she would appear unknown.

## Conclusion
This way a tedious task becomes hassle-free using this project

#Thank You
