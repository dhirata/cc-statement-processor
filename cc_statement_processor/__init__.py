import sys
from parser.pdfparser import parse_pdf

def main():
	# put main stuff here
	print("hello world")
	print(sys.argv)
	parse_pdf(sys.argv[1])

