
from django.urls import path
from .views import *
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/', SignUpView.as_view(), name = 'signup'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('dashboard/<int:pk>/', BooksDetailView.as_view(), name='dashboard'),
    path('accounts/logout/', CustomLogoutView.as_view(), name='logout'),
    path('admin/', AdminView.as_view(), name='admin'),
]