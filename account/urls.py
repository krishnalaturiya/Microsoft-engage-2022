from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    
    path("register",views.register,name="register"),
    path("login",views.login,name="login"),
    path("Attendance",views.Attendance,name="Attendance"),
    path("Statistics",views.Statistics,name="Statistics"),
    path("view_attendance",views.view_attendance,name="view_attendance"),
    path("Logout",views.Logout,name="Logout")
 
]
