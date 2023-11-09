from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from .forms import UserRegisterForm
from .models import Request
from django.utils import timezone

def index(request):
   return render(request, 'main/index.html')

class BBLoginView(LoginView):
   template_name = 'main/login.html'


class BBLogoutView(LoginRequiredMixin, LogoutView):
   template_name = 'main/logout.html'


class RegistrateUser(CreateView):
   success_url = reverse_lazy('main:index')
   def get(self, request, *args, **kwargs):
      form = {'form': RegistrateUser()}
      return render(request, 'main/registration.html', {'form': form})

   def post(self, request, *args, **kwargs):
      form = UserRegisterForm(request.POST, request.FILES)

      if form.is_valid():
         form.save()
         return render(request, 'main/register_done.html', {'form': form})
      return render(request, 'main/registration.html', {'form': form})

class ViewRequests(ListView):
   model = Request
   template_name = 'main/profile.html'
   context_object_name = 'requests'

   def get_queryset(self):
      return Request.objects.filter(author=self.request.user)

class ViewAllRequests(ListView):
   model = Request
   template_name = 'main/index.html'
   context_object_name = 'requests'

   def get_context_data(self,  **kwargs):
      context = super().get_context_data(**kwargs)
      context["num_of_accepted_requests"] = Request.objects.filter(status__exact='Принято в работу').count
      return context


class DeleteRequest(DeleteView):
   model = Request
   template_name = 'main/delete_request.html'
   context_object_name = 'requests'
   success_url = reverse_lazy('index')