from genericDataPool import DataPool
import csv
import pprint
import models
import urllib
import sys
import datetime
import re

from dateutil.parser import parse as date_parse
"""
	class for importing CSV files, sepertator , can be set
	it has the new row on number functionality
	if this is set it will generate a new row if the column name is a number 
	This is usefull when the data set has year as columns
	for example: 	indicator, 	location, 	2001,	2002,	2003,	2004
					'poverty',	'kenya',	23,		43,		12,		54
					'riches',	'kenya',	33,		53,		22,		64

	with new_row_on_number = True
	and row_on_number_column_name = 'year'
	this can be transformed into 
					indicator, 	location, 	year, 	year_value
					'poverty',	'kenya',	2001,	23
					'poverty',	'kenya',	2002,	43
					'poverty',	'kenya',	2003,	12
					'poverty',	'kenya',	2004,	54
					'riches',	'kenya',	2001,	33
					'riches',	'kenya',	2002,	53
					'riches',	'kenya',	2003,	22
					'riches',	'kenya',	2004,	64

	this is a lot better for querying and grouping by year.


"""
class CsvImport(DataPool):

	name_cvs = ''
	class_name = ''
	header = None
	delimiter = ','
	quotechar = '"'
	remove_quotes = False;
	new_row_on_number = False;
	row_on_number_column_name = 'year'

	schema_properties = {}
	schema_classes = {}
	schema_edges = {}
	errors = []

	def parse(self,file):
		rownum = 0
		self.class_name = self.prefix #if csv the table (class) nae is the prefix
		                                                                  
		reader = csv.reader(file, delimiter=self.delimiter.encode('ascii'), quotechar=self.quotechar.encode('ascii'))
		for row in reader:			
			if rownum == 0:
				self.header = row


			else:
				if rownum%1000 == 0:
					print 'thousand rows parsed'#just for debugging to see how fast it's parsing , can be removed 
				colnum = 0
				if self.class_name in self.schema_classes:
					class_cluster_id = self.schema_classes[self.class_name]['cluster_id'] # get the cluster id stored in the django model
				else:
					# if not set get ist from orient and create django object 
					cluster_ids = self.client.command("select classes[name='"+self.class_name+"'].defaultClusterId FROM 0:1") 
					for cluster_id in cluster_ids:
						try:
							pprint.pprint(cluster_id.classes)
							class_cluster_id = cluster_id.classes
							if len(cluster_id.classes) == 0:
								class_cluster_id = self.create_django_class(self.header)
						except Exception as exception:
							pprint.pprint(cluster_ids)
							print 'class not found'
							class_cluster_id = self.create_django_class(self.header)
				if self.create_schema == True :
					#if run to create schema break here and do not insert data TODO : seperate schema creation from data insertion 
					break
				rec_data = {}
				rec_data_row_on_number = {}
				for col in row:
					#print 'column = '+col 
					#print 'header is '+self.header[colnum]
					if(col != ''):
						try:
							attr_key = str(self.header[colnum])
						except:
							error = 'error at line '+str(rownum)
							print error;
							colnum += 1
							continue
						if self.new_row_on_number == True:
							#if new_ro_on number is set to True , make a new Row for each number (see class comment)
							if str(attr_key).isdigit():
								col_obj = self.schema_properties[self.prefix+'.year_value']['django_object']
								col = self.run_regex(col,col_obj)# run regular expressions
								rec_data_row_on_number[self.header[colnum]] = self.escape_orientdb(col)
								colnum += 1
								continue
						col_obj = self.schema_properties[self.prefix+'.'+self.format_attrib_name(attr_key)]['django_object'] # get django object for property
						col = self.run_regex(col,col_obj)
						rec_key = col_obj.orient_name
						# try to set coumn with the right data type
						try:
							if col_obj.property_type == 1:
								rec_data[self.format_attrib_name(rec_key)] =  int(col)
							elif col_obj.property_type == 2:
								rec_data[self.format_attrib_name(rec_key)] =  float(col)
							elif col_obj.property_type == 4:
								if col_obj.time_format != '':
									rec_data[self.format_attrib_name(rec_key)] =  datetime.datetime.strptime(col, col_obj.time_format)
								else:
									 rec_data[self.format_attrib_name(rec_key)] = date_parse(col)
							elif col_obj.property_type == 10 :
								rec_data[self.format_attrib_name(rec_key)] = datetime.datetime.fromtimestamp(int(col))
							elif col_obj.property_type == 11 :
								rec_data[self.format_attrib_name(rec_key)] = datetime.datetime.fromtimestamp(int(col)/1000)
							else:
								rec_data[self.format_attrib_name(rec_key)] =  self.escape_orientdb(col)
						except:
							print sys.exc_info()[0]
							pprint.pprint(rec_data)
							print 'failed '+self.class_name
							colnum += 1
							continue
				 		
					colnum += 1
				for number_col in rec_data_row_on_number:
					#make data for seprerate columns that are now rows
					rec_data['year'] = int(number_col);
					rec_data['year_value'] = rec_data_row_on_number[number_col];
					rec = {'@'+self.class_name:rec_data}
					#pprint.pprint(rec)
					#pprint.pprint(self.header)
					try:
						rec_position = self.client.record_create(class_cluster_id,rec )
					except:
						print sys.exc_info()[0]
						pprint.pprint(rec)
						print 'failed '+self.class_name
				else:
					#create regular record in orient db
					rec = {'@'+self.class_name:rec_data}
					#pprint.pprint(rec)
					#pprint.pprint(self.header)
					try:
						if not self.create_schema:
							rec_position = self.client.record_create(class_cluster_id,rec )
					except Exception as exception:
						print sys.exc_info()[0]
						pprint.pprint(rec)
						print 'failed '+self.class_name
		            
			rownum += 1

	"""
		create the class for django , this is not the same as the one in genericDatapool because of the new_row_on_number
		
	"""
	def create_django_class(self,first_row):
	   	
	   	data_model_class = models.DataModelClass()
		data_model_class.name = self.class_name
		data_model_class.translated_name = self.class_name
		data_model_class.orient_name = self.class_name
		data_model_class.default_cluster_id = 0
		data_model_class.data_source = self.source
		data_model_class.save()
		self.schema_classes[self.class_name] = {}
		self.schema_classes[self.class_name]['cluster_id'] = 0
		self.schema_classes[self.class_name]['django_object'] = data_model_class

	   	colnum = 0
	   	if(self.new_row_on_number):
	   		self.create_property_model(self.class_name,self.row_on_number_column_name,data_model_class)
	   		
			self.create_property_model(self.class_name,self.row_on_number_column_name+'_value',data_model_class)
	   		

		for attr_key in first_row:
			attr_key = str(attr_key).replace(self.quotechar,'')
			if(attr_key == ''):
				attr_key = 'column'+str(colnum)
			if str(attr_key).isdigit():
				if(self.new_row_on_number):
					colnum += 1
					continue
				attr_key = 'num_'+str(attr_key)
				print 'set column is digit'
			self.header[colnum] = attr_key
			print 'create property '+self.class_name+'.'+self.format_attrib_name(attr_key)+' STRING'
			self.create_property_model(self.class_name,self.format_attrib_name(attr_key),data_model_class)
			colnum += 1
		return data_model_class



	




