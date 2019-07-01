import csv
import datetime
from tabula import convert_into


def parse_statement_pdf(path):
	result = []
	temp_file_path = "test.csv"
	unsanitized = []
	convert_into(path, temp_file_path, output_format="csv", pages="3,4", guess=False, area=[10, 0, 97, 100], relative_area=True)
	with open(temp_file_path, 'r') as f:
		reader = csv.reader(f)
		unsanitized = list(reader)
	for line in unsanitized:
		sanitized_line = []
		filtered_line = list(filter(None, line)) # removes empty elements in line
		# Check if transaction entry
		date_name_field = filtered_line[0]
		if type(date_name_field) is str:
			date_name_list = date_name_field.split(' ', 1)
			try:
				datetime.datetime.strptime(date_name_list[0], "%m/%d")
				sanitized_line.extend(date_name_list)
				sanitized_line.append(eval(filtered_line[1].replace(',', '')))
				result.append(sanitized_line)
				print(sanitized_line)
			except ValueError as err:
				continue
	return result