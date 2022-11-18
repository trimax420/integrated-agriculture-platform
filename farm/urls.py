from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login_page,name='login'),
    path('registration/',views.role_registrations,name='role_registration'),
    path('index/',views.index,name='index'),
    path('crop-recommendation',views.croprec,name='croprec'),
    path('health/',views.crophel,name='health'),
    path('warehouse/',views.warehouse,name='warehouse'),
    path('weather/',views.weather,name='weather')
]
