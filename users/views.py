from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render

from django.contrib.auth import login
from django.views.generic import FormView
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import LoginForm, SignupForm
from .models import User

#UPDATED
from polls.models import Vote, Question, Choice

class SignupView(FormView):
    template_name = 'users/singup.html'
    form_class = SignupForm

    def form_valid(self, form):
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        raw_password = form.cleaned_data['password1']
        user = User.objects.create_user(username, email, raw_password)
        login(self.request, user)
        #return HttpResponseRedirect(reverse('main_page:indexUn_log_sing'))
        return HttpResponseRedirect(reverse('main_page:index'))

class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'

class UserLogoutView(LogoutView):
    template_name = 'users/logged_out.html'

def index(request):
    return render(request, 'users/register.html')

def account(request):
    #UPDATED
    vote = Vote.objects.filter(user= request.user)
    return render(request, 'users/account.html', {'vote' : vote})