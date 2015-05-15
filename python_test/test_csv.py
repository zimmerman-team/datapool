from csvParse import CsvImport
test = CsvImport()

test.connect()

test.class_name = 'acled_test'
test.delimiter = ','
test.delete_data()
test.parse_csv("csv/ACLED Version 5 All Africa 1997-2014_dyadic_Updated_csv.csv")
