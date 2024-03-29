import csv
import datetime
from tabula import convert_into
from .utils import Pdf


def parse_statement_pdf(creditor, path):
    result = []
    temp_file_path = "test.csv"
    unsanitized = []
    pdf = Pdf(path, creditor)
    pgs = pdf.get_page_range()
    relative_area = pdf.get_relative_area_percentages()
    convert_into(path, temp_file_path, output_format="csv", pages=pgs,
                 guess=False, area=relative_area, relative_area=True)
    with open(temp_file_path, 'r') as f:
        reader = csv.reader(f)
        unsanitized = list(reader)
    for line in unsanitized:
        sanitized_line = []
        filtered_line = list(filter(None, line))  # removes empty elements
        # Check if transaction entry
        date_name_field = filtered_line[0]
        if type(date_name_field) is str:
            date_name_list = date_name_field.split(' ', 1)
            try:
                datetime.datetime.strptime(date_name_list[0], "%m/%d")
                sanitized_line.extend(date_name_list)
                price_field = filtered_line[1]
                sanitized_line.append(eval(price_field.replace(',', '')))
                result.append(sanitized_line)
                print(sanitized_line)
            except ValueError as err:
                continue
    return result
