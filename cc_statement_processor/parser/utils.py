import operator
import PyPDF2


class Pdf():
    def __init__(self, path):
        self.reader = None
        self.path = path
        self.start_page = "3"

    path = property(operator.attrgetter('_description'))

    @path.setter
    def path(self, p):
        try:
            # Validations
            self.reader = PyPDF2.PdfFileReader(open(p, "rb"))
            print("PDF file valid")
        except Exception:
            raise ValueError("Error: Invalid PDF file")
        self._path = p

    def get_last_page(self):
        return str(self.reader.getNumPages())

    def get_page_range(self):
        return "%s-%s" % (self.start_page, self.get_last_page())
