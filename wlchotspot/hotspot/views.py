from django.shortcuts import redirect
from django.http import HttpResponse

from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.contrib import messages

class HomePageView(TemplateView):
	template_name='hotspot/index.html'

def redirectLogin(request):
	""" Handler to receive the initial request from the WLC """
	request.session['portal_ip'] = request.GET['portal_ip']
	request.session['client_id'] = request.GET['client_id']
	request.session['ssid'] = request.GET['ssid']
	request.session['bssid'] = request.GET['bssid']
	request.session['wbaredirect'] = request.GET['wbaredirect']
	redirect('hotspot.index')

class HelpPageView(TemplateView):
	template_name='hotspot/help.html'
