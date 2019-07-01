import PyPDF2


def validate_pdf_path(path):
    try:
        # Validations
        PyPDF2.PdfFileReader(open(path, "rb"))
        print("PDF file valid")
    except Exception:
        raise ValueError("Error: Invalid PDF file")
