from genericDataPool import DataPool
import csv
import pprint
import models
import urllib
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


	def parse(self,file):
		rownum = 0
		self.class_name = self.prefix
		                                                                  
		reader = csv.reader(file, delimiter=self.delimiter.encode('ascii'), quotechar=self.quotechar.encode('ascii'))
		for row in reader:
			if rownum == 0:
				self.header = row


			else:
				if rownum%1000 == 0:
					print 'thousand rows parsed'
				colnum = 0
				#print "select classes[name='"+self.class_name+"'].defaultClusterId FROM 0:1"
				if self.class_name in self.schema_classes:
					class_cluster_id = self.schema_classes[self.class_name]['cluster_id']
					print class_cluster_id
				else:
					cluster_ids = self.client.command("select classes[name='"+self.class_name+"'].defaultClusterId FROM 0:1")
					for cluster_id in cluster_ids:
						try:
							pprint.pprint(cluster_id.classes)
							class_cluster_id = cluster_id.classes
							if len(cluster_id.classes) == 0:
								class_cluster_id = self.create_class(self.header)
						except Exception as exception:
							pprint.pprint(cluster_ids)
							print 'class not found'
							class_cluster_id = self.create_class(self.header)
				rec_data = {}
				rec_data_row_on_number = {}
				for col in row:
					

					if(col != ''):
						attr_key = str(self.header[colnum])
						
						if self.new_row_on_number == True:
							if str(attr_key).isdigit():
								rec_data_row_on_number[self.header[colnum]] = self.escape_orientdb(col)
								colnum += 1
								continue
						rec_data[self.format_attrib_name(attr_key)] =  self.escape_orientdb(col)
				 		if 'date' in attr_key.lower():
				 			try:
				 				date = parse( col)
				 				rec_data[self.format_attrib_name(attr_key)+'__iso__'] = col
				 			except:
				 				print 'parsedate failed '+col
				 				pass
					colnum += 1
				for number_col in rec_data_row_on_number:
					rec_data['year'] = int(number_col);
					rec_data['year_value'] = rec_data_row_on_number[number_col];
					rec = {'@'+self.class_name:rec_data}
					#pprint.pprint(rec)
					#pprint.pprint(self.header)
					try:
						rec_position = self.client.record_create(class_cluster_id,rec )
					except:
						print 'failed '+self.class_name
				else:
					rec = {'@'+self.class_name:rec_data}
					#pprint.pprint(rec)
					#pprint.pprint(self.header)
					try:
						rec_position = self.client.record_create(class_cluster_id,rec )
					except:
						print 'failed '+self.class_name
		            
			rownum += 1

	def create_class(self,first_row):
	   	cluster_id = self.client.command('create class '+self.class_name+' EXTENDS V')
	   	cluster_ids = self.client.command("select classes[name='"+self.class_name+"'].defaultClusterId FROM 0:1")
		cluster_id = cluster_ids[0].classes
		print 'in create class cluster_id = '+str(cluster_id)
	   	data_model_class = models.DataModelClass()
		data_model_class.name = self.class_name
		data_model_class.default_cluster_id = cluster_id
		data_model_class.data_source = self.source
		data_model_class.save()
		self.schema_classes[self.class_name] = {}
		self.schema_classes[self.class_name]['cluster_id'] = cluster_id
		self.schema_classes[self.class_name]['django_object'] = data_model_class

	   	colnum = 0
	   	if(self.new_row_on_number):
	   		self.create_property(self.class_name,self.row_on_number_column_name,data_model_class)
	   		#self.client.command('create property '+self.class_name+'.'+self.row_on_number_column_name+' INTEGER')
	   		
	   		#print 'create property '+self.class_name+'.'+self.row_on_number_column_name+' INTEGER'
			self.create_property(self.class_name,self.row_on_number_column_name+'_value',data_model_class)
	   		#self.client.command('create property '+self.class_name+'.year_value STRING')
	   		
	   		#print 'create property '+self.class_name+'.year_value STRING'

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
			self.create_property(self.class_name,self.format_attrib_name(attr_key),data_model_class)
			# self.client.command('create property '+self.class_name+'.'+self.format_attrib_name(attr_key)+' STRING')
			# if 'date' in attr_key.lower():
			# 	self.client.command('create property '+self.class_name+'.'+self.format_attrib_name(attr_key)+'__iso__'+' DATETIME')
			colnum += 1
		return cluster_id

	




