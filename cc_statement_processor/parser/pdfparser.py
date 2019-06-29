from tabula import convert_into

def parse_pdf(path):
	convert_into(path, "test.csv", output_format="csv")