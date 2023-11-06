from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView

from .models import Request
from django.utils import timezone

def index(request):
   return render(request, 'main/index.html')

class BBLoginView(LoginView):
   template_name = 'main/login.html'


class BBLogoutView(LoginRequiredMixin, LogoutView):
   template_name = 'main/logout.html'