from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings 
from django.contrib.auth import views as auth

urlpatterns = [
    path("", views.index, name="index"),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',auth.LogoutView.as_view(template_name='login.html'),name='logout'),
    path('phaseA/',views.phaseA,name="phaseA"),
    path('phaseA/phaseA2/',views.phaseA2,name="phaseA2"),
    path('phaseB/',views.phaseB,name="phaseB"),
    path('phaseC/',views.phaseC,name="phaseC"),
    path('phaseD/',views.phaseD,name="phaseD"),
    path('phaseE/',views.phaseE,name="phaseE"),
]