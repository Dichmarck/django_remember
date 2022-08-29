from django.urls import path

from app import views

urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
]