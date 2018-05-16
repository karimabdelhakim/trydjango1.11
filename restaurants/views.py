from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.views.generic import (
	TemplateView,
	ListView,
	DetailView,
	CreateView
)
from .models import RestaurantLocation
from .forms import RestaurantCreateForm, RestaurantLocationCreateForm

def restaurant_createview(request):
	form = RestaurantLocationCreateForm(request.POST or None)
	errors = None
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/restaurants/')
	else:
		errors = form.errors
		
	template_name = 'restaurants/form.html'
	context = {'form': form,'errors':errors}
	return render(request, template_name, context)


def restaurant_listview(request):
	template_name = 'restaurants/restaurants_list.html'
	queryset = RestaurantLocation.objects.all()
	print(queryset)
	context = {
		"object_list": queryset
	}
	return render(request, template_name, context)

class RestaurantListView(ListView):
	#template_name = 'appname/modelnamelowercase_list.html' #default

	def get_queryset(self):
		slug = self.kwargs.get('slug')
		if slug:
			queryset = RestaurantLocation.objects.filter(
				Q(category__iexact=self.kwargs['slug']) |
				Q(category__icontains=self.kwargs['slug'])
			)
		else:
			queryset = RestaurantLocation.objects.all()
		return queryset

	
class RestaurantDetailView(DetailView):
	queryset = RestaurantLocation.objects.all()
	
	#to use url param other than pk or slug
	# def get_object(self,*args,**kwargs):
	# 	rest_id = self.kwargs.get('rest_id')
	# 	obj = get_object_or_404(RestaurantLocation,id=rest_id)
	# 	return obj


class RestaurantCreateView(CreateView):
	form_class = RestaurantLocationCreateForm
	template_name = 'restaurants/form.html'
	success_url = '/restaurants/'