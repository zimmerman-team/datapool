from csvParse import CsvImport
test = CsvImport()

test.connect()

test.class_name = 'twitterdata'
test.prefix = 'twitterdata'
test.delete_classes(drop_class=True)

test.delimiter = ','
test.parse_csv("ccountryken-twitteraf2012.csv")
