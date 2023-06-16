from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('',views.HomePage.as_view(),name='homePage'),
    path('createroom/',views.CreateRoom.as_view(),name='createRoom'),
    path('room/<int:pk>/',views.RoomChat.as_view(),name='room'),
    path('joinroom/',views.JoinRoom.as_view(),name='joinRoom'),
    path('chat/',views.ChatPage.as_view(),name='chatPage'),
    path('signin/',views.LoginPage.as_view(),name='signin'),
    path('signout/',views.LogoutView.as_view(),name='signout'),
    path('signup/',views.RegisterPage.as_view(),name='signup'),

]
