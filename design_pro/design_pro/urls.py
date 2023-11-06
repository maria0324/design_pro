from django.urls import path
from .views import index

app_name = 'designpro'

urlpatterns = [
    path('', index, name='index'),
]