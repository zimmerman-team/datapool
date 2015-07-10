from genericDataPool import DataPool
import csv
import pprint

class CsvImport(DataPool):

	name_cvs = ''
	class_name = ''
	header = None
	delimiter = ','
	quotechar = '"'
	remove_quotes = False;
	new_row_on_number = False;
	row_on_number_column_name = 'year'
	def parse_csv(self,file_name):
		rownum = 0
		with open(file_name, 'rb') as csvfile:
			#dialect = csv.Sniffer().sniff(csvfile.read(1024))      
			csvfile.seek(0)                                                                                      
			reader = csv.reader(csvfile, delimiter=self.delimiter, quotechar=self.quotechar)
			for row in reader:
				unicode_row = [x.decode('utf8') for x in row]
				row = unicode_row
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
					rec_data_row_on_number = {}
					for col in row:
						if(col != ''):
							print 'colnum '+str(colnum)+' '+col
							attr_key = str(self.header[colnum])
							
							if self.new_row_on_number == True:
								if str(attr_key).isdigit():
									rec_data_row_on_number[self.header[colnum]] = col
									colnum += 1
									continue
							rec_data[self.format_attrib_name(attr_key)] =  col
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
						pprint.pprint(rec)
						pprint.pprint(self.header)
						try:
							rec_position = self.client.record_create(class_cluster_id,rec )
						except:
							print 'failed'
					else:
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
	   	if(self.new_row_on_number):
	   		self.client.command('create property '+self.class_name+'.'+self.row_on_number_column_name+' INTEGER')
	   		print 'create property '+self.class_name+'.'+self.row_on_number_column_name+' INTEGER'
	   		self.client.command('create property '+self.class_name+'.year_value STRING')
	   		print 'create property '+self.class_name+'.year_value STRING'
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
			self.client.command('create property '+self.class_name+'.'+self.format_attrib_name(attr_key)+' STRING')
			if 'date' in attr_key.lower():
				self.client.command('create property '+self.class_name+'.'+self.format_attrib_name(attr_key)+'__iso__'+' DATETIME')
			colnum += 1
		return cluster_id

	




