import sys
from parser import parse_statement_pdf


def main():
    # put main stuff here
    path_to_pdf = sys.argv[1]
    parse_statement_pdf(path_to_pdf)
