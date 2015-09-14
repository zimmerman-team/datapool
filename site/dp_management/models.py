# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from ordered_model.models import OrderedModel
from xmlParse import xmlImport
from csvParse import CsvImport
from filegrabber import FileGrabber
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
import datetime

# Create your models here.

class DataConnection(models.Model):
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=512)
	host = models.GenericIPAddressField()
	port = models.IntegerField(default=2424)
	name = models.CharField(max_length=30)
	
	def __unicode__(self,):
		return "%s - %s" % (self.name, self.host)


class DataSourceFlags(models.Model):
	name = models.CharField(max_length=30)
	description = models.TextField()

	def __unicode__(self):
		return self.name

class DataSourceCategory(models.Model):
	name = models.CharField(max_length=30)
	description = models.TextField()
	class Meta:
   		verbose_name = "Category"
   		verbose_name_plural = "Categories"

	def __unicode__(self):
		return self.name

class DataSourceSubCategory(models.Model):
	category = models.ForeignKey(DataSourceCategory)
	name = models.CharField(max_length=30)
	description = models.TextField()
	class Meta:
   		verbose_name = "Sub Category"
   		verbose_name_plural = "Sub Categories"
	def __unicode__(self):
		return self.name

class DataSource(models.Model):

	DATATYPECHOICE = (
	    (0, 'CSV'),
	    (1, 'XML'),
	    (2, 'JSON'),
	    (3,'FROM QUERY')
	)

	OLDDATACHOICE = (
	    (0, 'REMOVE'),
	    (1, 'APPEND'),
	    (2, 'OVERWRITE'),
	)

	name = models.CharField(max_length=30) 
	url = models.URLField(null=True,blank=True)
	data_file = models.FileField(upload_to='data_files',blank=True,null=True)
	owner = models.ForeignKey(User)
	prefix = models.CharField(max_length=10)
	private = models.BooleanField(default=False)
	data_connection = models.ForeignKey(DataConnection)
	data_type = models.IntegerField(choices=DATATYPECHOICE, default=0) 
	old_data_choice = models.IntegerField(choices=OLDDATACHOICE, default=0) 
	csv_seprator = models.CharField(max_length=5,null=True,blank=True)
	new_row_on_number = models.BooleanField(default=False)
	new_row_on_number_name = models.CharField(max_length=30,null=True,blank=True)
	overwrite_fields = models.CharField(max_length=50,null=True,blank=True)
	#data_from_date = models.DateTimeField(null=True)
	#data_to_date = models.DateTimeField(null=True)
	date_last_update = models.DateTimeField(blank=True, null=True)
	sub_category = models.ForeignKey(DataSourceSubCategory,null=True)
	remove_prop_strings = models.TextField(null=True,blank=True) # possible values is more than 20 
	update_interval = models.CharField(
        max_length=20,
        choices=(
            ('day', 'Day'),
            ('week', 'Week'),
            ('month', 'Month'),
            ('year', 'Year'),
        ),
        default="month")
	quality_of_source = models.FloatField(default=5.0)#to be determened
	flags = models.ManyToManyField(DataSourceFlags)


	def __unicode__(self):
		return self.name
	
	
	def parse_status(self):
		return mark_safe("<a href='parse-source/?source_id=%i' class='parse-btn'>Parse</a>") % self.id
	parse_status.allow_tags =  True

	def django_models(self):
		return mark_safe("<a href='create-django-schema/?source_id=%i' class='parse-btn'>Parse</a>") % self.id
	django_models.allow_tags =  True
	
	def orient_models(self):
		return mark_safe("<a href='create-orient-schema/?source_id=%i' class='parse-btn'>Parse</a>") % self.id
	orient_models.allow_tags =  True

	def create_django_schema(self) :
		print 'in create django schema'
		if self.data_type == 1:
			parser = xmlImport()
		elif self.data_type == 0:
			parser = CsvImport()
		connection = self.data_connection
		parser.source = self
		parser.create_schema = True
		parser.connect(connection.name,connection.username,connection.password,connection.host,connection.port,self.prefix)
		#parser.connect_old()
		#get the file 

		for data_class in DataModelClass.objects.filter(data_source=self).all():
			data_class.delete()
		if self.data_file == None or self.data_file == '':
			file_grabber = FileGrabber()
			data_file = file_grabber.get_the_file(self.url)
		else:
			data_file = open(self.data_file.path, 'r')
			
			print 'parse fiel'
		if self.data_type == 1:
			parse_file = data_file.readlines()			
			parser.load_xml(parse_file)
			parser.parse_xml()
		if self.data_type == 0:
			#parser.delete_classes(drop_class=)
			parser.delimiter = self.csv_seprator
			parser.new_row_on_number = self.new_row_on_number
			parser.new_row_on_number_name = self.new_row_on_number_name
			parser.parse(data_file)

	def create_orient_schema(self):
		if self.data_type == 1:
			parser = xmlImport()
		elif self.data_type == 0:
			parser = CsvImport()
		
		connection = self.data_connection
		parser.source = self
		parser.connect(connection.name,connection.username,connection.password,connection.host,connection.port,self.prefix)
		parser.delete_classes(drop_class=True)
		parser.create_orient_schema()
		#parser.connect_old()

	def process(self):
		if self.data_type == 1:
			parser = xmlImport()
		elif self.data_type == 0:
			parser = CsvImport()
		connection = self.data_connection
		parser.source = self
		parser.connect(connection.name,connection.username,connection.password,connection.host,connection.port,self.prefix)
		parser.load_schema()
		if self.old_data_choice == 0:
			parser.delete_classes(drop_class=False)
		if self.data_file == None or self.data_file == '':
			file_grabber = FileGrabber()
			parse_file = file_grabber.get_the_file(self.url)
		else:
			parse_file = open(self.data_file.path, 'r')
			#parse_file = data_file.readlines()
		if self.data_type == 1:
			
			parser.load_xml(parse_file)
			parser.parse_xml()
		if self.data_type == 0:
			parser.delimiter = self.csv_seprator
			parser.new_row_on_number = self.new_row_on_number
			parser.new_row_on_number_name = self.new_row_on_number_name
			parser.parse(parse_file)



class DataSourceComment(models.Model):

	data_source = models.ForeignKey(DataSource)
	comment = models.TextField()
	user = models.ForeignKey(User)



class DataModelClass(models.Model):
	data_source = models.ForeignKey(DataSource,related_name="classes")
	name = models.CharField(max_length=30)
	default_cluster_id = models.CharField(max_length=5)
	translated_name = models.CharField(max_length=30,null=True,blank=True)
	orient_name = models.CharField(max_length=30,null=True,blank=True)
	def __unicode__(self):
		return self.name

class DataModelGroup(models.Model):
	name = models.CharField(max_length=30)
	def __unicode__(self):
		return self.name

class DataModelSubGroup(models.Model):
	data_model_group = models.ForeignKey(DataModelGroup)
	name = models.CharField(max_length=30)
	def __unicode__(self):
		return self.name


class DataModelScript(models.Model):
	name = models.CharField(max_length=30)
	description = models.TextField()
	return_values =  models.TextField()
	script =  models.TextField()
	def __unicode__(self):
		return "%s" % (self.name)

class DataModelRegexp(models.Model):
	name = models.CharField(max_length=30)
	description = models.TextField()
	script =  models.TextField()
	def __unicode__(self):
		return "%s" % (self.name)


class DataModelProperty(models.Model):

	TYPECHOICE = (
	    (0, 'STRING'),
	    (1, 'INTEGER'),
	    (2, 'FLOAT'),
	    (3,	'TEXT'),
	    (4,	'DATE'),
	    (5,	'DATETIME'),
	    (6,'LAT'),
	    (7,'LONG'),
	    (8,'LAT LONG'),
	    (9,'SCRIPT'),
	    (10, 'TIMESTAMP'),
	    (11, 'TIMESTAMPMILLIS') 
	)
	data_model_class = models.ForeignKey(DataModelClass,related_name="properties")
	name = models.CharField(max_length=128)
	data_model_subgroup = models.ForeignKey(DataModelSubGroup, blank=True, null=True)
	translated_name = models.CharField(max_length=128)
	orient_name = models.CharField(max_length=128)
	property_type = models.IntegerField(choices=TYPECHOICE, default=0) 
	property_values = models.TextField(null=True,blank=True) # possible values is more than 20 
	defaul_value = models.CharField(max_length=30,null=True,blank=True)
	time_format = models.CharField(max_length=30,null=True,blank=True)
	script = models.ForeignKey(DataModelScript, blank=True, null=True)
	regexp = models.ManyToManyField(DataModelRegexp, blank=True,null=True)
	def __unicode__(self):
		return "%s.%s" % (self.data_model_class.name, self.name)

class DataModelEdge(models.Model):
	data_source = models.ForeignKey(DataSource)
	name = models.CharField(max_length=128)
	class_in = models.ForeignKey(DataModelClass,related_name='class_in')
	class_out = models.ForeignKey(DataModelClass,related_name='class_out')

class DataModelEdgeProperty(models.Model):
	data_model_edge = models.ForeignKey(DataModelEdge)
	name = models.CharField(max_length=30)
	property_type = models.CharField(max_length=30)

	def __unicode__(self):
		return "%s.%s" % (self.data_model_edge.name, self.name)

class DataModelQuery(OrderedModel):

    class Meta(OrderedModel.Meta):
        verbose_name = "DataModel Query"
        verbose_name_plural = "DataModel Queries"
    data_source = models.ForeignKey(DataSource)
    name = models.CharField(max_length=30)
    query = models.TextField()
    run_after_update = models.BooleanField(default=False)

    def __str__(self):
        pass
    def __unicode__(self):
		return self.name

#pivot point extremely importand
class DataModelPivotPoint(models.Model):
	name = models.CharField(max_length=30)
	pivot_type = models.CharField(max_length=30)
	create_script = models.TextField(null=True,blank=True)





class DataProject(models.Model):

	user = models.ForeignKey(User)
	name = models.CharField(max_length=56)
	sub_title = models.CharField(max_length=56,null=True,blank=True)
	description = models.TextField(null=True,blank=True)

    
	

	def __unicode__(self):
   		return self.name


class DataSetStream(models.Model):
	CHART_CHOICE = (
	    (0, 'heat_map'),
	    (1, 'country_map'),
	    (2, 'bar_chart'),
	    (3,	'line_chart'),
	    #(4,	'MAX'),
	    #(5,	'SUM'),
	    #(6, 'AVG'),
	    #(7, 'FILTER'),
	    #(8, 'COUNT')
	)
	data_project = models.ForeignKey(DataProject,related_name='data_streams')
	user = models.ForeignKey(User)
	name = models.CharField(max_length=56)
	data_stream = models.ForeignKey(DataSource,related_name="data_set_streams")
	chart_type = models.IntegerField(choices=CHART_CHOICE, default=0) 
	x_axis = models.ForeignKey('DataSetStreamProperty',null=True,blank=True)
	extra_where_clause = models.TextField(null=True,blank=True)
   	class Meta:
   		verbose_name = "Data set stream"
   		verbose_name_plural = "Data set streams"

	def __unicode__(self):
		return self.data_stream.name+'-'+self.data_stream.name
	class Meta:
		ordering = ['-id']

class DataSetStreamProperty(models.Model):

	ACTIONCHOICE = (
	    (0, 'SELECT'),
	    (1, 'SEARCHBOX'),
	    (2, 'BETWEEN'),
	    (3,	'MIN'),
	    (4,	'MAX'),
	    (5,	'SUM'),
	    (6, 'AVG'),
	    (7, 'FILTER'),
	    (8, 'COUNT')
	)

	data_set_stream = models.ForeignKey(DataSetStream,related_name='properties')
	data_stream_class = models.ForeignKey(DataModelClass,related_name="my_properties")
	data_model_property = models.ForeignKey(DataModelProperty)
	use_property = models.BooleanField(default=False)
	action = models.IntegerField(choices=ACTIONCHOICE, default=0) 
	filter_value = models.CharField(max_length=512,null=True,blank=True)
	show_filter_field = models.BooleanField(default=False)

	def __unicode__(self):
		return self.data_model_property.translated_name

class Keyword(models.Model):
	keyword = models.CharField(max_length=128,null=True,blank=True)
	count = models.IntegerField()

class TwitterUser(models.Model):
	u_id = models.BigIntegerField(primary_key=True)
	count = models.IntegerField()


class DollyData(models.Model):

	id = models.BigIntegerField(primary_key=True)
	u_id = models.ForeignKey(TwitterUser)
	latitude = models.FloatField()
	longitude = models.FloatField()
	create_at = models.DateTimeField()
	text = models.CharField(max_length=200)

	def __unicode__(self):	
		return self.text 
    
    

    


    














