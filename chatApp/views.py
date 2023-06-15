from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView

class ChatPage(TemplateView):
    template_name = 'base.html'
    
class LoginPage(LoginView):
    pass

class RegisterPage(CreateView):
    pass