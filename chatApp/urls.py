from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('',views.ChatPage.as_view(),name='chatPage'),
]