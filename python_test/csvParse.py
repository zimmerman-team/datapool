import xmlParse
import csv
import pprint

class CsvImport(xmlParse.xmlImport):

	name_cvs = ''
	class_name = ''
	header = None
	delimiter = ','
	quotechar = '"'
	remove_quotes = False;
	new_row_on_number = False;
	def parse_csv(self,file_name):
		rownum = 0
		with open(file_name, 'rb') as csvfile:
			#dialect = csv.Sniffer().sniff(csvfile.read(1024))      
			csvfile.seek(0)                                                                                      
			reader = csv.reader(csvfile, delimiter=self.delimiter, quotechar=self.quotechar)
			for row in reader:
				if rownum == 0:
					self.header = row


				else:
					colnum = 0
					print "select classes[name='"+self.class_name+"'].defaultClusterId FROM 0:1"
					cluster_ids = self.client.command("select classes[name='"+self.class_name+"'].defaultClusterId FROM 0:1")
					for cluster_id in cluster_ids:
						try:
							class_cluster_id = cluster_id.classes
						except Exception as exception:
							pprint.pprint(cluster_ids)
							print 'class not found'
							class_cluster_id = self.create_class(self.header)
							class_cluster_id = class_cluster_id[0]
					rec_data = {}
					for col in row:
						if(col != ''):
							print 'colnum '+str(colnum)+' '+col
							attr_key = str(self.header[colnum])
							rec_data[self.format_attrib_name(attr_key)] =  col
					 		if 'date' in attr_key.lower():
					 			try:
					 				date = parse( col)
					 				rec_data[self.format_attrib_name(attr_key)+'__iso__'] = col
					 			except:
					 				print 'parsedate failed '+col
					 				pass
						colnum += 1
					rec = {'@'+self.class_name:rec_data}
					pprint.pprint(rec)
					pprint.pprint(self.header)
					try:
						rec_position = self.client.record_create(class_cluster_id,rec )
					except:
						print 'failed'
			            
				rownum += 1

	def create_class(self,first_row):
	   	cluster_id = self.client.command('create class '+self.class_name+' EXTENDS V')
	   	colnum = 0
		for attr_key in first_row:
			attr_key = str(attr_key).replace(self.quotechar,'')
			if(attr_key == ''):
				attr_key = 'column'+str(colnum)
			if str(attr_key).isdigit():

				attr_key = 'num_'+str(attr_key)
				print 'set column is digit'
			self.header[colnum] = attr_key
			print 'create property '+self.class_name+'.'+self.format_attrib_name(attr_key)+' STRING'
			self.client.command('create property '+self.class_name+'.'+self.format_attrib_name(attr_key)+' STRING')
			if 'date' in attr_key.lower():
				self.client.command('create property '+self.class_name+'.'+self.format_attrib_name(attr_key)+'__iso__'+' DATETIME')
			colnum += 1
		return cluster_id

	def delete_data(self):
		try:
			self.client.command('DELETE VERTEX '+self.class_name)
			self.client.command('DROP CLASS '+self.class_name)
		except:
			pass





