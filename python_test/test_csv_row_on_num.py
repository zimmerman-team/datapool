from csvParse import CsvImport
test = CsvImport()

test.connect()

test.class_name = 'ken_country'
test.prefix = 'ken_country'
test.delete_classes(drop_class=True)
test.new_row_on_number = True

test.delimiter = ','
test.parse_csv("csv/ken_Country_en_csv_v2.csv")
