from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Meeting

def index(request):
	meeting_list = Meeting.objects.order_by('-meeting_name')
	context = {
		'meeting_list': meeting_list,
	}
	return render(request, 'Home/index.html', context)

def meetings(request, meeting_count):
	return HttpResponse("stuff %s" % meeting_count)
