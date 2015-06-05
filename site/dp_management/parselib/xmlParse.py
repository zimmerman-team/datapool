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

	def create_class(self,class_name,element):
		cluster_id = self.client.command('create class '+class_name+' EXTENDS V')
		for attr_key in element.keys():
			print 'create property '+class_name+'.'+self.format_attrib_name(attr_key)+' STRING'
			self.client.command('create property '+class_name+'.'+self.format_attrib_name(attr_key)+' STRING')
			if 'date' in attr_key:
				self.client.command('create property '+class_name+'.'+self.format_attrib_name(attr_key)+'__iso__'+' DATETIME')
		if element.text != '':
				print 'create property '+class_name+'.text STRING'
				self.client.command('create property '+class_name+'.text STRING')

		return cluster_id

	def insert_data(self,element):
		#get_cluster_id
		class_cluster_id = None
		class_name = self.format_class_name(element.tag)
		cluster_ids = self.client.command("select classes[name='"+class_name+"'].defaultClusterId FROM 0:1")
		for cluster_id in cluster_ids:
			try:
				class_cluster_id = cluster_id.classes 
			except Exception as exception:
				class_cluster_id = self.create_class(class_name,element)
				class_cluster_id = class_cluster_id[0]

		print class_cluster_id
		print "is cluster id"

	 	#get attributes
	 	rec_data = {}
	 	for attr_key in element.keys():
	 		rec_data[self.format_attrib_name(attr_key)] =  element.get(attr_key)
	 		if 'date' in attr_key:
	 			try:
	 				date = parse( element.get(attr_key))
	 				rec_data[self.format_attrib_name(attr_key)+'__iso__'] = element.get(attr_key)
	 			except:
	 				print 'parsedate failed '+element.get(attr_key)
	 				pass
	 	if element.text != '':
	 		rec_data['text'] = unicode(element.text).replace('"','\\"').encode('utf-8')
		rec = {'@'+class_name:rec_data}
		pprint.pprint(rec)
		rec_position = self.client.record_create(class_cluster_id,rec )
		return rec_position._rid

	def create_edge(self,from_rec,to_rec,edge_name,parent,child):
		edge_command = "CREATE edge "+edge_name+" from "+from_rec+" to "+to_rec
		try:
			self.client.command(edge_command)
		except Exception as exeception:
			self.create_edge_object(edge_name,parent,child)
			self.client.command(edge_command)
	
	def create_edge_object(self,edge_name,parent,child):
		edge_command = "create class "+edge_name+" extends E"

		self.client.command(edge_command)
		self.client.command('CREATE PROPERTY '+edge_name+'.out LINK '+parent)
		self.client.command('CREATE PROPERTY '+edge_name+'.in LINK '+child)



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
			#print parent_rec
			self.create_edge(parent_rec,rec,edge_name,self.format_class_name(parent_tag),self.format_class_name(element.tag))
		for e in element.getchildren():
			if e == None or type(e).__name__ != '_Element':
				continue
				#pass
			self.parse_xml_element(e,rec,element.tag)


	

	def testWithBuza(self):
		self.connect_old()
		self.delete_classes(drop_class=False)
		#self.load_xtd('iati-activities-schema.xsd')
		self.load_xml('iati-activities.xml')
		self.parse_xml()

	def testWithMaec(self):
		self.connect_old()
		self.prefix = 'iati201'
		self.delete_classes(drop_class=False)
		#self.load_xtd('iati-activities-schema.xsd')
		self.load_xml('MAEC_IATI_INDONESIA.xml')
		self.parse_xml()

	def test_xsd(self):
		self.connect()
		self.delete_classes()
		return
		self.load_xml('iati-activities-schema.xsd')
		self.parse_xml()
		



