from django.shortcuts import render
from django.views.generic.base import RedirectView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from .models import *
from django.contrib.auth.models import User
from django.views.generic import *
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
class SignUpView(generic.CreateView):
    form_class    = UserCreationForm
    success_url   = reverse_lazy('login')
    template_name = 'signup.html'

class BooksDetailView(DetailView):
    model = User
    template_name = 'dashboard.html'



class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user  # Pass the current user object to the template
        return context

class CustomLogoutView(LogoutView):
    @method_decorator(csrf_exempt)  # Exempt CSRF protection for POST requests
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            # Handle logout for POST requests
            return self.post(request, *args, **kwargs)
        else:
            # Allow GET requests to be handled by parent class
            return super().dispatch(request, *args, **kwargs)


class AdminView(RedirectView):
    url = reverse_lazy('admin:index')