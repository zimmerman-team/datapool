# -*- coding: utf-8 -*-
import pyorient
from lxml import etree
from lxml import objectify
from io import StringIO, BytesIO
from dateutil.parser import parse
import json
import re
import pprint
from filegrabber import FileGrabber
import models


class DataPool():
	db_name = 'datapool'
	user_name = 'root'
	password = 'solaria07'
	xml_tree = None
	schema = None
	prefix = 'iati105'
	max_rows_to_delete = 9999
	file_to_parse = None
	schema_properties = {}
	schema_classes = {}
	schema_edges = {}
	encoding = 'ascii'

	def create_class(self,class_name):
		if(existing_cluster_id != None):
			cluster_id_text = ' CLUSTER '+existing_cluster_id
		else:
			cluster_id_text = ''

		cluster_ids = self.client.command('create class '+class_name+' EXTENDS V '+cluster_id_text)

		cluster_id = cluster_ids[0]
		print 'create class cluster_id = '+cluster_id+' '+class_name
		for cl_id in cluster_ids:
			print 'cl_id = '+cl_id
		cluster_ids = self.client.command("select classes[name='"+class_name+"'].defaultClusterId FROM 0:1")
		cluster_id = cluster_ids[0].classes
		print 'query for  cluster_id = '+str(cluster_id)+' '+class_name
		for cl_id in cluster_ids:
			print 'cl_id = '+str(cl_id.classes)
		data_model_class = models.DataModelClass()
		data_model_class.name = class_name
		data_model_class.default_cluster_id = cluster_id
		data_model_class.data_source = self.source
		data_model_class.save()
		self.schema_classes[class_name] = {}
		self.schema_classes[class_name]['cluster_id'] = cluster_id
		self.schema_classes[class_name]['django_object'] = data_model_class

		

		return cluster_id

	def create_property(self,class_name,property_name,data_model_class):
		prop_name =self.format_attrib_name(property_name)
		self.schema_properties[class_name+'.'+prop_name] = True
		data_model_class_property = models.DataModelProperty()
		data_model_class_property.data_model_class = data_model_class
		data_model_class_property.name = prop_name
		data_model_class_property.type = 'STRING'
		data_model_class_property.save()
		print 'create property '+class_name+'.'+prop_name+' STRING'
		self.client.command('create property '+class_name+'.'+prop_name+' STRING')
		if 'date' in prop_name:
			data_model_class_property_iso_ = models.DataModelProperty()
			data_model_class_property_iso_.data_model_class = data_model_class
			data_model_class_property_iso_.name = prop_name+'__iso__'
			data_model_class_property_iso_.type = 'DATETIME'
			data_model_class_property_iso_.save()
			self.client.command('create property '+class_name+'.'+prop_name+'__iso__'+' DATETIME')


	def create_edge(self,from_rec,to_rec,edge_name,parent,child):
		edge_command = "CREATE edge "+edge_name.encode(self.encoding)+" from "+from_rec+" to "+to_rec
		try:
			self.client.command(edge_command)
		except Exception as exeception:
			self.create_edge_object(edge_name,parent,child)
			self.client.command(edge_command)
	
	def create_edge_object(self,edge_name,parent_object,child_object):
		edge_command = "create class "+edge_name.encode(self.encoding)+" extends E"
		#add edge to list

		self.client.command(edge_command)
		self.client.command('CREATE PROPERTY '+edge_name.encode(self.encoding)+'.out LINK '+parent_object.name.encode(self.encoding))
		self.client.command('CREATE PROPERTY '+edge_name.encode(self.encoding)+'.in LINK '+child_object.name.encode(self.encoding))
		django_edge = models.DataModelEdge()
		django_edge.name = edge_name
		django_edge.class_out = parent_object
		django_edge.class_in = child_object
		django_edge.data_source = self.source
		django_edge.save()
		self.schema_edges[edge_name] = django_edge



	def connect(self,db_name,user_name,password,host,port,prefix):
		self.client = pyorient.OrientDB(host, port)
		print user_name+' '+password
		self.client.connect(user_name.encode(self.encoding),password.encode(self.encoding))
		self.client.db_open(db_name, user_name,password )
		self.prefix = prefix


	def connect_old(self):
		self.client = pyorient.OrientDB("localhost", 2424)
		self.client.connect(self.user_name,self.password)
		self.client.db_open(self.db_name, self.user_name,self.password )

	def delete_classes(self,drop_class=False):
		list_command = "SELECT classes FROM 0:1"
		classes = self.client.command(list_command)
		for clss in classes[0].classes:
			print clss.get('name')
			print clss.get('superClass')
			if str(clss.get('name')).startswith(self.prefix):
				#get number of rows
				result = self.client.command("SELECT COUNT(@rid) as num_rows FROM "+clss.get('name'))
				for num_row_res in result:
					num_rows = int(num_row_res.num_rows)
				#numrows = result[0]['num_rows']

				type_class = 'EDGE'
				if(clss.get('superClass') == 'V'):
					type_class = 'VERTEX'
				while(num_rows > 0):
					print 'DELETE '+type_class+' '+clss.get('superClass')+' WHERE @class="'+clss.get('name')+'" LIMIT '+str(self.max_rows_to_delete)
					self.client.command('DELETE '+type_class+' '+clss.get('superClass')+' WHERE @class="'+clss.get('name')+'" LIMIT '+str(self.max_rows_to_delete))
					
					num_rows = num_rows - self.max_rows_to_delete
				if drop_class == True:
					print 'DROP CLASS '+clss.get('name')
					self.client.command('DROP CLASS '+clss.get('name'))


	def format_class_name(self,tag_name):
		#replace minus
		tag_name = re.sub("(\{.*\})","",tag_name) 
		tag_name = tag_name.replace('-','_')
		tag_name = tag_name.replace('"','').encode(self.encoding)
		
		return self.prefix+'_'+tag_name.replace(' ','_')

	def format_attrib_name(self,tag_name):
		#replace minus
		tag_name = re.sub("(\{.*\})","",tag_name) 
		tag_name = tag_name.replace('-','_')
		tag_name = tag_name.replace('"','')
		return tag_name.replace(' ','_').encode(self.encoding)

	def escape_orientdb(self,text):
		escapechars = '@()"%'
		for special_char in escapechars:
			text = text.replace(special_char,'\\'+special_char)
		return text

	def make_structure(self):
		query = 'SELECT classes FROM 0:1'
		db_classes = self.client.command(query)

		edges = {}
		classes = {}
		data_tree = {}
		for db_class in db_classes:
			for db_class_info in db_class.classes:
				if not str(db_class_info['name']).startswith(self.prefix):
					continue
				if db_class_info['superClass'] in ['E']:
					edges[db_class_info['name']] = {}
					for db_property in db_class_info['properties']:
						edges[db_class_info['name']][db_property['name']] = db_property['linkedClass']
				if db_class_info['superClass'] in ['V']:
					classes[db_class_info['name']] = {}
					for db_property in db_class_info['properties']:
						classes[db_class_info['name']][db_property['name']] = db_property['type']
		
		#loop through edges to make get parents
		parent_data = {}
		child_data = {}
		for key in edges:
			edge = edges[key]

			parent_data[edge['in']] = edge['out']
			if(edge['out'] not in child_data):
				child_data[edge['out']] = []
			child_data[edge['out']].append(edge['in'])


		

		#find root edge
		root = ''
		for key in parent_data:
			if(parent_data[key] not in parent_data):
				root = parent_data[key]
		if len(parent_data) == 0:
			#only one class
			root = self.prefix

		structure_tree = {}
		self.make_tree(root,child_data,structure_tree,classes)
		
		return structure_tree


	def load_url(self, url):
		filegrabber = FileGrabber()
		self.file_to_parse = file_grabber.get_the_file(url)
		


	def make_tree(self,element_name,child_data,tree_dict,classes):

		tree_dict[element_name] = {}
		tree_dict[element_name]['attributes'] = classes[element_name]
		first_loop = True
		if element_name not in child_data:
			return
		for sub_element in child_data[element_name]:
			#first
			if first_loop == True:
				tree_dict[element_name]['subclasses'] = {}
				first_loop = False

			self.make_tree(sub_element,child_data,tree_dict[element_name]['subclasses'],classes)
		return 



	def format_for_d3(self,structure_tree):
		d3_tree = {'name':'data','size':100,'children':[]}
		for element in structure_tree:
			self.make_d3_tree(element,structure_tree[element],d3_tree['children'])

		json_tree = json.dumps(d3_tree)
		print json_tree


	def make_d3_tree(self,element_name,element,sub_structure_tree):
		element_data = {'name':str(element_name).replace(self.prefix+'_',''),'size':100}
		element_data['attributes'] = element['attributes']
		element_data['children'] = []
		
		for attr_name in element['attributes']:
			element_data['children'].append({'name':'attribute '+attr_name})
		if not 'subclasses' in element:
			sub_structure_tree.append(element_data)
			return
		for sub_class in element['subclasses']:	
			self.make_d3_tree(sub_class,element['subclasses'][sub_class],element_data['children'])

		
		
		sub_structure_tree.append(element_data)


	def create_pivot(self,from_class,to_class,from_match, to_match):
		class_name = from_class+"_"+to_class
		query = 'CREATE CLASS '+class_name+'_pivot EXTENDS V'
		#self.client.command(query)
		query = 'CREATE PROPERTY '+class_name+'.match STRING'
		#self.client.command(query)
		edge_to_name = ''
		query = 'CREATE CLASS '+class_name+' EXTENDS E'
		#self.client.command(query)
		query = "SELECT "+from_match+' FROM '+from_class+' GROUP BY '+from_match
		matches = self.client.command(query)
		for match in matches:
			print match.get('from_match')

	def parse(self):
		pass


	def load_schema(self):
		#load schema from django models
		source = self.source
		#get classes
		classes = models.DataModelClass.objects.filter(data_source=source)
		for data_model_class in classes:
			cluster_ids = self.client.command("select classes[name='"+data_model_class.name+"'].defaultClusterId FROM 0:1")
			print "select classes[name='"+data_model_class.name+"'].defaultClusterId FROM 0:1"
			if len(cluster_ids[0].classes) == 0 :
				models.DataModelProperty.objects.filter(data_model_class=data_model_class).delete()
				data_model_class.delete()
				print len(cluster_ids[0].classes)
				print 'deleted'
				print 'exiting'
				continue
			
			#print data_model_class.name
			self.schema_classes[data_model_class.name] = {}
			self.schema_classes[data_model_class.name]['cluster_id'] = data_model_class.default_cluster_id
			self.schema_classes[data_model_class.name]['django_object'] = data_model_class
			
			for class_prop in models.DataModelProperty.objects.filter(data_model_class=data_model_class):
				self.schema_properties[data_model_class.name+'.'+class_prop.name] = True
				
		for data_model_edge in models.DataModelEdge.objects.filter(data_source=source):
			cluster_ids = self.client.command("select classes[name='"+data_model_edge.name+"'].defaultClusterId FROM 0:1")
			if len(cluster_ids[0].classes) == 0 :
				data_model_edge.delete()
				continue
			self.schema_edges[data_model_edge.name] = data_model_edge






