# -*- coding: utf-8 -*-
import pyorient
from lxml import etree
from lxml import objectify
from io import StringIO, BytesIO
from dateutil.parser import parse
from genericDataPool import DataPool
import json
import re
import pprint


class xmlImport(DataPool):
	
	

	schema_only = False
	schema_properties = {}
	schema_classes = {}
	schema_edges = {}
	source = None


	def insert_data(self,element):
		#get_cluster_id
		class_cluster_id = None
		class_name = self.format_class_name(element.tag)
		if class_name in self.schema_classes:
			class_cluster_id = self.schema_classes[class_name]['cluster_id']

		else:
			class_cluster_id = self.create_class(class_name)

		django_object = self.schema_classes[class_name]['django_object']

		print class_cluster_id
		print "is cluster id"

	 	#get attributes
	 	rec_data = {}
	 	for attr_key in element.keys():
	 		if not class_name+'.'+self.format_attrib_name(attr_key) in self.schema_properties:
	 			self.create_property(class_name,attr_key,django_object)

	 		rec_data[self.format_attrib_name(attr_key)] =  element.get(attr_key)
	 		if 'date' in attr_key:
	 			try:
	 				date = parse( element.get(attr_key))
	 				rec_data[self.format_attrib_name(attr_key)+'__iso__'] = element.get(attr_key)
	 			except:
	 				print 'parsedate failed '+element.get(attr_key)
	 				pass
	 	if element.text != '':
	 		if not class_name+'.text' in self.schema_properties:
	 			self.create_property(class_name,'text',django_object)
	 		rec_data['text'] = unicode(element.text).replace('"','\\"').encode('utf-8')
		rec = {'@'+class_name:rec_data}
		pprint.pprint(rec)
		rec_position = self.client.record_create(class_cluster_id,rec )
		return rec_position._rid



	def load_xtd(self,xtd_file):
		self.schema = etree.XMLSchema(file=xtd_file)




	def load_xml(self,file_name):
		if(self.schema == None):
			xml_parser = etree.XMLParser(schema=self.schema)
			self.xml_tree = etree.parse(file_name,parser=xml_parser)

		else:
			parser = objectify.makeparser(schema = self.schema)
			objectify.set_default_parser(parser)
			pprint.pprint(objectify.getRegisteredTypes())
			#return
			self.xml_tree = objectify.parse(file_name,parser=parser)
			#objectify.xsiannotate(self.xml_tree,ignore_old=False,ignore_pytype=True)


	def parse_xml(self):
		root = self.xml_tree.getroot()
		objectify.deannotate(root, cleanup_namespaces=True)
		self.parse_xml_element(root,None,None)


	def parse_xml_element(self,element,parent_rec,parent_tag):
		#return if end is reached
		
		if element == None:
			return
		rec = self.insert_data(element);
		#rec = 0
		
		if(parent_tag != None):
			edge_name = self.format_class_name(parent_tag)+'_'+self.format_class_name(element.tag)
			print edge_name
			print parent_rec
			print rec
			parent_obj = self.schema_classes[self.format_class_name(parent_tag)]['django_object']
			child_obj = self.schema_classes[self.format_class_name(element.tag)]['django_object']
			self.create_edge(parent_rec,rec,edge_name,parent_obj,child_obj)
		for e in element.getchildren():
			if e == None or type(e).__name__ != '_Element':
				continue
				#pass
			self.parse_xml_element(e,rec,element.tag)



	
