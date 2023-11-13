from django.urls import path
from .views import index
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', ViewAllRequests.as_view(), name='index'),
    path('register/', RegistrateUser.as_view(), name='registration'),
    path('login/', BBLoginView.as_view(), name='login'),
    path('logout/', BBLogoutView.as_view(), name='logout'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)