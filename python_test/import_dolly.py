# -*- encoding: utf-8 -*-

# converting a unknown formatting file in utf-8
import csv
from dp_management.models import DollyData,TwitterUser
import datetime
import codecs

file_name = '/home/daan/bitofpepper/zimmerman/datapool/datapool/python_test/dolly_no_first_line.csv'
print 'delete data'
DollyData.objects.all().delete()
TwitterUser.objects.all().delete()
i = 0
with open(file_name, 'rb') as csvfile:
	#dialect = csv.Sniffer().sniff(csvfile.read(1024))   null=
	print 'in file!'   
	csvfile.seek(0)                                                                                      
	reader = csv.reader(csvfile, delimiter=',')
	twitter_users = {}
	for row in reader:
		unicode_row = [x.decode('utf8') for x in row]
		print 'row number = '+str(i)
		i = i + 1
		print 'read row'
		print 'row = '+row[0]
		dd = DollyData()
		dd.id = row[0]
		if not (row[1]) in twitter_users:
			print 'new twitter user'
			tu = TwitterUser()
			tu.u_id = row[1]
			tu.count = 1
			tu.save()
			twitter_users[row[1]] = tu
		else:
			tu = twitter_users[row[1]]
			tu.count = tu.count + 1
		print 'added twitter user'
		dd.u_id = twitter_users[row[1]]
		dd.latitude = row[2]
		dd.longtitude = row[3]
		dd.create_at = datetime.datetime.fromtimestamp(int(row[4])/1000)
		print 'befrore try'
		try:
			dd.text = unicode_row[5]
		
			dd.save()
		except:
			pass

for u_id in twitter:
	twitter_users[u_id].save()