from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,TemplateView
from django.urls import reverse,reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin



# Create your views here.
class Dashboard(TemplateView):
    template_name = 'dashboard/base/base.html'