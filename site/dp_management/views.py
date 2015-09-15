from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import QueryDict

from django.core import serializers
from models import DollyData,TwitterUser,DataProject,DataSource,DataSourceCategory,DataSourceSubCategory,DataSetStream,DataProject,DataSetStreamProperty
from django.db.models import Count
from django.db import connection
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from genericDataPool import DataPool
import pprint



import json

# Create your views here.



@login_required
def add_data(request):
	categories = DataSourceCategory.objects.all()
	my_data_streams = DataSetStream.objects.filter(user=request.user).all()
	
	if request.method == 'POST':
		print 'in post'
		data_set_name =  request.POST['name']
		data_stream_id = request.POST['stream_id']
		data_stream = DataSource.objects.get(pk=data_stream_id)
		data_set = DataSetStream()
		data_set.name = data_set_name
		if data_set_name == '':
			data_set.name = data_stream.name
		data_set.user = request.user
		data_set.data_stream_id = data_stream_id
		data_set.save();
		
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


	if request.method == 'POST':
		pprint.pprint(request.POST)
		data_project = DataProject()
		data_project.user = request.user
		data_project.name = request.POST['name']
		data_project.sub_title = request.POST['sub_title']
		data_project.description = request.POST['description']
		data_project.save()
		#print 'data_Set = '+request.POST[u'data_set']
		
		data_project.save();

		page_vars = {'project':data_project}
		crsfcontext = RequestContext(request, page_vars)
		return render_to_response('show_project.html',crsfcontext)	
	else:
		return HttpResponse("");

@login_required
def projects(request):
	data_set_streams = DataSetStream.objects.filter(user=request.user).order_by('-id');
	categories = DataSourceCategory.objects.all()
	
	my_projects = DataProject.objects.filter(user=request.user).all().order_by('-id');
	page_vars = {'data_set_streams':data_set_streams,'my_projects':my_projects,'categories':categories}
	crsfcontext = RequestContext(request, page_vars)
	return render_to_response('projects.html',crsfcontext)	

@login_required
def save_project(request):


	if request.method == 'POST':
		pprint.pprint(request.POST)
		data_project = DataProject.objects.get(pk=request.POST['project-id'])
		data_project.user = request.user
		data_project.name = request.POST['name']
		#data_project.description = request.POST['description']
		data_project.data_streams.clear()
		#print 'data_Set = '+request.POST[u'data_set']
		for data_stream_id in dict(request.POST)['data_set']:
			if data_stream_id == '':
				continue
			data_project.data_streams.add(DataSetStream.objects.get(pk=int(data_stream_id)))
		data_project.save();

	return HttpResponse("{'success':'true'}")

@login_required
def add_dataset_to_project(request):

	if request.method == 'POST':
		data_set_name =  request.POST['name']
		data_stream_id = request.POST['stream_id']
		project_id = request.POST['project_id']
		print 'PROJECT ID = '+str(project_id)
		data_stream = DataSource.objects.get(pk=data_stream_id)
		project = DataProject.objects.get(pk=project_id)
		data_set = DataSetStream()
		data_set.name = data_set_name
		if data_set_name == '':
			data_set.name = data_stream.name
		data_set.user = request.user
		data_set.data_stream_id = data_stream_id
		data_set.data_project = project
		data_set.save();
		
		for data_stream_class in data_stream.classes.all():
			for data_stream_property in data_stream_class.properties.all():
				data_set_property = DataSetStreamProperty()
				data_set_property.data_set_stream = data_set
				data_set_property.data_stream_class = data_stream_class
				data_set_property.data_model_property = data_stream_property
				data_set_property.save()
		page_vars = {'data_stream':data_set}
		crsfcontext = RequestContext(request, page_vars)
		return render_to_response('show_datastream.html',crsfcontext)	
	else:
		return HttpResponse("error");

@login_required
def remove_dataset_from_project(request):
	if request.method == 'POST':
		data_project = DataProject()
		data_project.user = request.user
		data_project.name = request.post['name']
		data_project.description = request.post['description']
		data_project.save()
	return HttpResponse("{'success':'true'}")


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
def delete_data_project(request,id):
	data_project = DataProject.objects.get(pk=id)
	if data_project.user == request.user :
		data_project.delete()
	return HttpResponse("{'success':'true'}")

@login_required
def save_data_set(request):
	print 'in save_data_set'
	if request.method == 'POST':
		print 'in method post'
		data_set_stream = DataSetStream.objects.get(pk=request.POST['stream-id']);
		if data_set_stream.user == request.user :
			data_set_stream.name = request.POST['name']
			print request.POST['name']
			data_set_stream.chart_type = request.POST['chart-type']
			data_set_stream.x_axis_id = request.POST['x-axis']
			data_set_stream.save()
	return HttpResponse("{'success':'true'}")

@login_required
def save_property(request):
	print 'in save'
	if request.method == 'POST':
		data_set_property = DataSetStreamProperty.objects.get(pk=request.POST['property-id']);
		data_set_property.action = request.POST['property_action']
		data_set_property.filter_value = request.POST['filter_value']
		if 'show_filter_field' in request.POST :
			data_set_property.show_filter_field = True
		else:
			data_set_property.show_filter_field = False
		if 'use_property' in request.POST:
			data_set_property.use_property = True
		else:
			data_set_property.use_property = False
		data_set_property.save()
	return HttpResponse("{'success':'true'}")


def visualize_project(request,project_id):
	#get the datasets
	data_project = DataProject.objects.get(pk=project_id)
	data_set_streams = {}
	for data_stream in data_project.data_streams.all():
		if not data_stream.get_chart_type_display() in data_set_streams:
			data_set_streams[data_stream.get_chart_type_display()] = []
		data_set_streams[data_stream.get_chart_type_display()].append(data_stream)

	page_vars = {'data_project':data_project,'data_streams':data_set_streams}
	crsfcontext = RequestContext(request, page_vars)
	return render_to_response('view_data.html',crsfcontext)	


@login_required
def get_queries(request,data_set_id):
	data_set = DataSetStream.objects.get(pk=data_set_id)
	datapool = DataPool()
	query_data_set = datapool.get_query_data(data_set,request.POST)
	return HttpResponse(json.dumps(query_data_set))

@login_required
def get_project_chart_data(request,project_id,chart_type):
	project = DataProject.objects.get(pk=project_id)
	return_arr = []
	pprint.pprint(request.POST)
	print 'is post'
	datapool = DataPool()
	for data_set_stream in project.data_streams.all():
		if data_set_stream.get_chart_type_display() == chart_type:
			return_arr.append(datapool.get_query_data(data_set_stream,request.GET))
	return HttpResponse(json.dumps(return_arr))



