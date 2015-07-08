from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from models import DollyData,TwitterUser
# Create your views here.


def get_dolly_data(request):

	start_date = request.GET['start']
	end_date = request.GET['end']
	search_string = request.GET['search']
	data = DollyData.objects.filter(create_at__range=[start_date, end_date]).filter(text__search=search_string)
	return HttpResponse(serializers.serialize("json", data))
