from csvParse import CsvImport
test = CsvImport()

test.connect()

test.class_name = 'acled_test'
test.prefix = 'acled_test'
test.delete_classes(drop_class=True)

test.delimiter = ','
test.parse_csv("csv/ACLED Version 5 All Africa 1997-2014_dyadic_Updated_csv.csv")
