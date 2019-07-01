import sys
from parser import parse_statement_pdf
from parser import validate_pdf_path


def main():
    # put main stuff here
    path_to_pdf = sys.argv[1]
    validate_pdf_path(path_to_pdf)
    parse_statement_pdf(path_to_pdf)
