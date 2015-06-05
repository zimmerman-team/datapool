from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class DataConnection(models.Model):
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	host = models.URLField()
	port = models.IntegerField(default=2424)
	name = models.CharField(max_length=30)
	
	def __unicode__(self,):
		return "%s - %s" % (self.name, self.host)


class DataSource(models.Model):

	DATATYPECHOICE = (
	    (0, 'CSV'),
	    (1, 'XML'),
	    (2, 'JSON'),
	)

	OLDDATACHOICE = (
	    (0, 'REMOVE'),
	    (1, 'APPEND'),
	    (2, 'OVERWRITE'),
	)
	name = models.CharField(max_length=30)
	url = models.URLField()
	owner = models.ForeignKey(User)
	prefix = models.CharField(max_length=10)
	private = models.BooleanField(default=False)
	data_connection = models.ForeignKey(DataConnection)
	data_type = models.IntegerField(choices=DATATYPECHOICE, default=0) 
	old_data_choice = models.IntegerField(choices=OLDDATACHOICE, default=0) 
	csv_seprator = models.CharField(max_length=5)
	new_row_on_number = models.BooleanField(default=False)
	new_row_on_number_name = models.CharField(max_length=30)
	overwrite_fields = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name


class DataModelClass(models.Model):
	data_source = models.ForeignKey(DataSource)
	name = models.CharField(max_length=30)
	default_cluster_id = models.CharField(max_length=5)

	def __unicode__(self):
		return self.name


class DataModelProperty(models.Model):
	data_model_class = models.ForeignKey(DataModelClass)
	name = models.CharField(max_length=30)
	property_type = models.CharField(max_length=30)

	def __unicode__(self):
		return "%s.%s" % (self.data_model_class.name, self.name)

class DataModelEdge(models.Model):
	class_in = models.ForeignKey(DataModelClass)
	class_out = models.ForeignKey(DataModelClass)

class DataModelEdgeProperty(models.Model):
	data_model_edge = models.ForeignKey(DataModelEdge)
	name = models.CharField(max_length=30)
	property_type = models.CharField(max_length=30)

	def __unicode__(self):
		return "%s.%s" % (self.data_model_edge.name, self.name)














