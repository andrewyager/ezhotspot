from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.contrib import messages

class HomePageView(TemplateView):
	template_name='hotspot/index.html'


class HelpPageView(TemplateView):
	template_name='hotspot/help.html'
