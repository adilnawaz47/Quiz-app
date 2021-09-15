from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('login', login_attempt, name = 'login_attempt'),
    path('register', register_attempt, name = 'register_attempt'),
    path('logout_view', logout_view, name = 'logout_view'),
    path('thanks', thanks, name='thanks')

]