from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Computer, OS, Producer


# Create your views here.
class ComputerList(ListView):
    model = Computer


class ComputerCreate(CreateView):
    model = Computer
    model2 = OS
    fields = ['name', 'description', 'price']
    success_url = reverse_lazy('computers_app:computer_list')


class ComputerUpdate(UpdateView):
    model = Computer
    fields = ['name', 'description', 'price']
    success_url = reverse_lazy('computers_app:computer_list')


class ComputerDelete(DeleteView):
    model = Computer
    success_url = reverse_lazy('computers_app:computer_list')
