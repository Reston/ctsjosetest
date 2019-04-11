from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import User


class UserListView(ListView):
    model = User


class UserDetailView(DetailView):
    """View user details"""
    model = User
    pk_url_kwarg = 'uuid'


class UserCreateView(CreateView):
    """Create a new user"""
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    success_url = reverse_lazy('user:user-list')


class UserUpdateView(UpdateView):
    """Update the user"""
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    pk_url_kwarg = 'uuid'


class UserDeleteView(DeleteView):
    """Delete the given user"""
    model = User
    success_url = reverse_lazy('user:user-list')
    pk_url_kwarg = 'uuid'
