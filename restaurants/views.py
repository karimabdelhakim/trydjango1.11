from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView
from .models import RestaurantLocation

def restaurant_listview(request):
	template_name = 'restaurants/restaurants_list.html'
	queryset = RestaurantLocation.objects.all()
	print(queryset)
	context = {
		"object_list": queryset
	}
	return render(request, template_name, context)
