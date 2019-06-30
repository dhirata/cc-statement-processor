import sys
from parser.pdfparser import parse_statement_pdf

def main():
	# put main stuff here
	parse_statement_pdf(sys.argv[1])

