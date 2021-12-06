from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('data/', views.data, name="data"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),
]