import sys
from parser import parse_statement_pdf


def main():
    # put main stuff here
    creditor = sys.argv[1]
    path_to_pdf = sys.argv[2]
    parse_statement_pdf(creditor, path_to_pdf)
