from django.shortcuts import render
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = 'base.html'


class AboutView(TemplateView):
    template_name = 'about.html'
