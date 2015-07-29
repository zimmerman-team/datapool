from django.db import models
from django.contrib.auth.models import User
from ordered_model.models import OrderedModel
from xmlParse import xmlImport
from csvParse import CsvImport
from filegrabber import FileGrabber
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe


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
	url = models.URLField(null=True)
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
	data_from_date = models.DateTimeField(null=True)
	data_to_date = models.DateTimeField(null=True)
	date_last_update = models.DateTimeField(default=None, null=True)
	sub_category = models.ForeignKey(DataSourceSubCategory,null=True)
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
	
	def process(self):
		if self.data_type == 1:
			parser = xmlImport()
		elif self.data_type == 0:
			parser = CsvImport()
		connection = self.data_connection
		parser.source = self
		parser.connect(connection.name,connection.username,connection.password,connection.host,connection.port,self.prefix)
		#parser.connect_old()
		#get the file 
		parser.load_schema()
		
		file_grabber = FileGrabber()
		parse_file = file_grabber.get_the_file(self.url)
		if self.data_type == 1:
			#parser.delete_classes()
			
			parser.load_xml(parse_file)
			parser.parse_xml()
		if self.data_type == 0:
			parser.delete_classes(drop_class=False)
			parser.delimiter = self.csv_seprator
			parser.new_row_on_number = self.new_row_on_number
			parser.new_row_on_number_name = self.new_row_on_number_name
			parser.parse(parse_file)



class DataSourceComment(models.Model):

	data_source = models.ForeignKey(DataSource)
	comment = models.TextField()
	user = models.ForeignKey(User)



class DataModelClass(models.Model):
	data_source = models.ForeignKey(DataSource)
	name = models.CharField(max_length=30)
	default_cluster_id = models.CharField(max_length=5)
	translated_name = models.CharField(max_length=30)
	def __unicode__(self):
		return self.name

class DataModelGroup(models.Model):
	data_model_class = models.ForeignKey(DataModelClass)
	name = models.CharField(max_length=30)
	def __unicode__(self):
		return self.name

class DataModelSubGroup(models.Model):
	data_model_group = models.ForeignKey(DataModelGroup)
	name = models.CharField(max_length=30)
	def __unicode__(self):
		return self.name



class DataModelProperty(models.Model):
	data_model_class = models.ForeignKey(DataModelClass)
	name = models.CharField(max_length=30)
	data_model_subgroup = models.ForeignKey(DataModelSubGroup,null=True)
	translated_name = models.CharField(max_length=30)
	property_type = models.CharField(max_length=30)
	property_values = models.TextField() # possible values is more than 20 
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
	description = models.TextField(null=True,blank=True)


    
	

	def __unicode__(self):
   		return self.name



class DataSetStream(models.Model):

	data_project = models.ForeignKey(DataProject)
	data_stream = models.ForeignKey(DataSource)
   	class Meta:
   		verbose_name = "Data set stream"
   		verbose_name_plural = "Data set streams"

	def __unicode__(self):
		return self.data_set.name+'-'+self.data_stream.name

class DataSetStreamProperty(models.Model):

	ACTIONCHOICE = (
	    (0, 'SUM'),
	    (1, 'AVG'),
	    (2, 'MAX'),
	    (3,	'MIN'),
	    (4,	'GROUP BY'),

	)
	data_set_stream = models.ForeignKey(DataSetStream)
	data_model_property = models.ForeignKey(DataModelProperty)
	action = models.IntegerField(choices=ACTIONCHOICE, default=0) 
	filter_value = models.CharField(max_length=512,null=True,blank=True)

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
    
    

    


    














