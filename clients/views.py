from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import ClientCreationForm
from .models import Client



class CreateClient(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientCreationForm
    template_name = 'client/client_create.html'
    success_url = reverse_lazy('clients')


class Clients(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'client/clients_list.html'
    context_object_name = 'clients'


