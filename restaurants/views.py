from django.http import HttpResponse
from django.shortcuts import render
import random
# Create your views here.
def home(request):
	html_var = 'f strings'
	some_list = [1,2,3,4]
	context = {
		"html_var":html_var,
		"num":random.randint(0,10000),
		"some_list":some_list
	}
	return render(request, 'base.html',context)