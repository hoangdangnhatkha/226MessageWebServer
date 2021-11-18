
from django.shortcuts import render
from django.http import HttpResponse
from hello.models import msgserver
from hello.models import List
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.http import JsonResponse
# Create your views here.
def hello(request):
	get_object = msgserver.objects.values('Key', 'Message')
	glist = list(get_object)  # important: convert the QuerySet to a list object
	return JsonResponse(glist, safe=False)
def get(request, id):
	get_key = msgserver.objects.filter(Key=id)
	return HttpResponse(get_key)

class create(CreateView):
	model = msgserver
	fields = '__all__'
	success_url = reverse_lazy('hello')

class update(UpdateView):
	model = msgserver
	fields = ['Message']
	success_url = reverse_lazy('hello')

