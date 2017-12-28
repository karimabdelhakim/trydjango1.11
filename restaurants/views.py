from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView

import random
# Create your views here.

class HomeView(TemplateView):
	template_name = 'home.html'

	def get_context_data(self,*args, **kwargs):
		context = super(HomeView,self).get_context_data(*args,**kwargs)
		html_var = 'f strings'
		some_list = [1,2,3,4]
		context = {
			"html_var":html_var,
			"num":random.randint(0,10000),
			"some_list":some_list
		}
		return context    

