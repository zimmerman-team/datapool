from xmlParse import xmlImport,XsdParser
test = xmlImport()
#test.test_xsd()
test.connect()
test.prefix = "iati105"
struct = test.make_structure()
test.format_for_d3(struct)