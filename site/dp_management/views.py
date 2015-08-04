from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response

from django.core import serializers
from models import DollyData,TwitterUser,DataProject,DataSource,DataSourceCategory,DataSourceSubCategory,DataSetStream,DataProject,DataSetStreamProperty
from django.db.models import Count
from django.db import connection
from django.contrib.auth.decorators import login_required
from django.template import RequestContext



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
	if request.method == 'POST':
		print 'in post'
		data_set_name =  request.POST['name']
		data_stream_id = request.POST['stream_id']
		data_set = DataSetStream()
		data_set.name = data_set_name
		data_set.user = request.user
		data_set.data_stream_id = data_stream_id
		data_set.save();
		data_stream = DataSource.objects.get(pk=data_stream_id)
		for data_stream_class in data_stream.classes.all():
			for data_stream_property in data_stream_class.properties.all():
				data_set_property = DataSetStreamProperty()
				data_set_property.data_set_stream = data_set
				data_set_property.data_stream_class = data_stream_class
				data_set_property.data_model_property = data_stream_property
				data_set_property.save()

	
	page_vars = {'categories':categories,'my_data_streams':my_data_streams}
	crsfcontext = RequestContext(request, page_vars)
	return render_to_response('add_data.html',crsfcontext)

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
def add_datastream(request):

	
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

@login_required
def delete_data_stream(request,id):
	data_set_stream = DataSetStream.objects.get(pk=id)
	if data_set_stream.user == request.user :
		data_set_stream.delete();
	return HttpResponse("{'success':'true'}")

@login_required
def save_property(request):
	print 'in save'
	if request.method == 'POST':
		print 'in post'
		data_set_property = DataSetStreamProperty.objects.get(pk=request.POST['property-id']);
		data_set_property.action = request.POST['property_action']
		data_set_property.filter_value = request.POST['filter_value']
		if 'use_property' in request.POST:
			data_set_property.use_property = True
		else:
			data_set_property.use_property = False
		data_set_property.save()
	return HttpResponse("{'success':'true'}")
