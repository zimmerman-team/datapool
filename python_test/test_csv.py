from csvParse import CsvImport
test = CsvImport()

test.connect()


test.class_name = 'dolly'
test.prefix = 'dolly'
test.delete_classes()

test.delimiter = ','
test.parse_csv("ccountryken-twitteraf2012.csv")
