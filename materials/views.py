from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import MaterialInfo

class MaterialListView(ListView):
    model = MaterialInfo

class MaterialDetailView(DetailView):
    model = MaterialInfo

class MaterialCreateView(CreateView):
    model = MaterialInfo
    fields = ['MaterialName','maker','category','ChemName','TechInfo']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'

class MaterialUpdateView(UpdateView):
    model = MaterialInfo
    fields = ['MaterialName','maker','category','ChemName','TechInfo']
    success_url = reverse_lazy('list')
    template_name_suffix = '_update'

class MaterialDeleteView(DeleteView):
    model = MaterialInfo
    fields = ['MaterialName','maker','category','ChemName','TechInfo']
    success_url = reverse_lazy('list')
    template_name_suffix = '_delete'