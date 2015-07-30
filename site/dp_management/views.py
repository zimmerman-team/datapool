from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response

from django.core import serializers
from models import DollyData,TwitterUser,DataProject,DataSource,DataSourceCategory,DataSourceSubCategory,DataSetStream,DataProject
from django.db.models import Count
from django.db import connection
from django.contrib.auth.decorators import login_required


import json

# Create your views here.


def get_dolly_data(request):

	start_date = request.GET['start']
	end_date = request.GET['end']
	exclude_ids = []
	
	exclude_ids = request.GET.getlist('exclude_ids')
	include_ids = request.GET.getlist('include_ids')

	if 'search' in request.GET and request.GET['search'] != '':
		search_string = request.GET['search']
		data = DollyData.objects.filter(create_at__range=[start_date, end_date]).filter(text__search=search_string).exclude(u_id_id__in=exclude_ids)[:5000]
	else:
		data = DollyData.objects.filter(create_at__range=[start_date, end_date]).exclude(u_id_id__in=exclude_ids)[:5000]
	return HttpResponse(serializers.serialize("json", data))

def get_tweets_per_day(request):
	start_date = request.GET['start']
	end_date = request.GET['end']
	exclude_ids = request.GET.getlist('exclude_ids')
	include_ids = request.GET.getlist('include_ids')
	if 'search' in request.GET and request.GET['search'] != '':
		search_string = request.GET['search']
		data = DollyData.objects.filter(create_at__range=[start_date, end_date]).filter(text__search=search_string).exclude(u_id_id__in=exclude_ids).extra(select={'day': 'date( create_at )'}).values('day').annotate(tweets=Count('create_at')).order_by('day')
	else:
		data = DollyData.objects.filter(create_at__range=[start_date, end_date]).exclude(u_id_id__in=exclude_ids).extra(select={'day': 'date( create_at )'}).values('day').annotate(tweets=Count('create_at')).order_by('day')
	return_data = []
	for row in  data:
		return_data.append({'tweets':row['tweets'],'date': str(row['day'])})
	return HttpResponse(json.dumps(return_data))

def get_tweets_per_hour(request):
	start_date = request.GET['start']
	end_date = request.GET['end']
	exclude_ids = request.GET.getlist('exclude_ids')
	include_ids = request.GET.getlist('include_ids')
	if 'search' in request.GET and request.GET['search'] != '':
		search_string = request.GET['search']
		data = DollyData.objects.filter(create_at__range=[start_date, end_date]).filter(text__search=search_string).exclude(u_id_id__in=exclude_ids).extra(select={'hour': connection.ops.date_trunc_sql('hour', 'create_at')}).values('hour').annotate(tweets=Count('create_at')).order_by('hour')
	else:
		data = DollyData.objects.filter(create_at__range=[start_date, end_date]).exclude(u_id_id__in=exclude_ids).extra(select={'hour': connection.ops.date_trunc_sql('hour', 'create_at')}).values('hour').annotate(tweets=Count('create_at')).order_by('hour')
	return_data = []
	for row in  data:
		return_data.append({'tweets':row['tweets'],'hour': str(row['hour'])})
	return HttpResponse(json.dumps(return_data))

def get_top_twitter_users(request):
	data = TwitterUser.objects.all().order_by('-count')[:50]
	return HttpResponse(serializers.serialize("json", data))

@login_required
def add_data(request):
	categories = DataSourceCategory.objects.all()
	my_data_streams = DataSetStream.objects.all()


	return render_to_response('add_data.html',{'categories':categories})

@login_required
def add_project(request):

	data_set_stream = DataSetStream.objects.filter(user=request.user)
	if request.method == 'POST':
		data_project = DataProject()
		data_project.user = request.user
		data_project.name = request.post['name']
		data_project.description = request.post['description']
		data_project.save()
	my_projects = DataProject.objects.filter(user=request.user)
	return render_to_response('add_project.html',{'data_set_stream':data_set_stream,'my_projects':my_projects})	

@login_required
def add_datastream(request,name,stream_id):
	project_name =  request.post['name']
	data_stream_id = request.post['stream_id']
	return add_data(request)

@login_required
def get_categories(request):
	categories = DataSourceCategory.objects.all()
	cat_array = {}
	for cat in categories:
		cat_array[cat.id] = cat.name
	return HttpResponse(json.dumps(cat_array))

@login_required
def get_sub_categories(request,category_id):
	sub_categories = DataSourceSubCategory.objects.filter(category_id=category_id)
	cat_array = {}
	for cat in sub_categories:
		cat_array[cat.id] = cat.name
	return HttpResponse(json.dumps(cat_array))

@login_required
def get_data_streams(request,sub_category_id):
	sources = DataSource.objects.filter(sub_category_id=sub_category_id)
	streams_arr = {}
	for source in sources:
		streams_arr[source.id] = source.name 
	return HttpResponse(json.dumps(streams_arr))

