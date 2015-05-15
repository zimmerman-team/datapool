# -*- coding: utf-8 -*-
import pyorient
from lxml import etree
from lxml import objectify
from io import StringIO, BytesIO
from dateutil.parser import parse
import re
import pprint


class xmlImport():
	
	db_name = 'datapool'
	user_name = 'root'
	password = 'solaria07'
	xml_tree = None
	schema = None
	prefix = 'iati105'

	def connect(self):
		self.client = pyorient.OrientDB("localhost", 2424)
		self.client.connect(self.user_name,self.password)
		self.client.db_open(self.db_name, self.user_name,self.password )

	def create_class(self,class_name,element):
		cluster_id = self.client.command('create class '+class_name+' EXTENDS V')
		for attr_key in element.keys():
			print 'create property '+class_name+'.'+self.format_attrib_name(attr_key)+' STRING'
			self.client.command('create property '+class_name+'.'+self.format_attrib_name(attr_key)+' STRING')
			if 'date' in attr_key:
				self.client.command('create property '+class_name+'.'+self.format_attrib_name(attr_key)+'__iso__'+' DATETIME')
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
	 		rec_data['text'] = unicode(element.text).replace('"','')
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


	def delete_classes(self,drop_class=False):
		list_command = "SELECT classes FROM 0:1"
		classes = self.client.command(list_command)
		for clss in classes[0].classes:
			print clss.get('name')
			print clss.get('superClass')
			if clss.get('superClass') == 'E' or clss.get('superClass') == 'V':
				if(clss.get('superClass') == 'V'):
					self.client.command('DELETE VERTEX '+clss.get('name'))
				else:
					self.client.command('DELETE edge '+clss.get('name'))

				if drop_class == True:
					print 'DROP CLASS '+clss.get('name')
					self.client.command('DROP CLASS '+clss.get('name'))


	def format_class_name(self,tag_name):
		#replace minus
		tag_name = tag_name.replace('-','_')
		
		return self.prefix+'_'+tag_name.replace(' ','_')

	def format_attrib_name(self,tag_name):
		#replace minus
		tag_name = re.sub("(\{.*\})","",tag_name) 
		tag_name = tag_name.replace('-','_')
		tag_name = tag_name.replace('"','')
		return tag_name.replace(' ','_')

	def testWithBuza(self):
		self.connect()
		self.delete_classes()
		#self.load_xtd('iati-activities-schema.xsd')
		self.load_xml('iati-activities.xml')
		self.parse_xml()

	def test_xsd(self):
		self.connect()
		self.delete_classes()
		return
		self.load_xml('iati-activities-schema.xsd')
		self.parse_xml()


class XsdParser(xmlImport):
	"""make a tree with attribute types, for storing with the right data type in orient db /or any other db"""
	attributeTypeTree = {}

	def parse_xml(self):
		self.parse_xml_element(self.xml_tree.getroot(),None)
	
	def parse_xml_element(self,element,tag_name):
		print 'start attributes for ' + element.tag
		for key in element.attrib:
			print key+' '+element.attrib.get(key) +' is attribute'
			#print type(element.attrib.get(key))
		print 'end attributes'+"\n\n\n\n\n"
		for e in element.getchildren():
			if e == None or type(e).__name__ != '_Element':	
				#continue
				pass
			self.parse_xml_element(e,element.tag)




