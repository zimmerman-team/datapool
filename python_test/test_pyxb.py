import binding


xml = open('iati-activities.xml').read()
tree = binding.CreateFromDocument(xml)
for item in tree.iati-activity:
	print item.generated_datetime
