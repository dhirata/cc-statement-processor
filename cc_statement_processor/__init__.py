import PyPDF2
import sys
from parser.pdfparser import parse_statement_pdf

def main():
	# put main stuff here
	path_to_pdf = sys.argv[1]
	try:
		# Validations 
		PyPDF2.PdfFileReader(open(path_to_pdf, "rb"))
		print("PDF file valid")
	except:
		raise ValueError("Error: Invalid PDF file")
	parse_statement_pdf(path_to_pdf)

