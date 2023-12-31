from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Gadget

class GadgetListView(ListView):
    model = Gadget
    template_name = 'gadgets/gadget_list.html'
    context_object_name = 'gadgets'
    paginate_by = 10  

class GadgetDetailView(DetailView):
    model = Gadget
    template_name = 'gadgets/gadget_detail.html'
    context_object_name = 'gadget'
