import operator
import PyPDF2


class Pdf():

    configs = {
        "chase": {
            "start_page": 3,
            "relative_top": 10,
            "relative_left": 0,
            "relative_bottom": 97,
            "relative_right": 100
        }
    }

    def __init__(self, path, creditor, configs=None):
        self.start_page = None
        self.relative_top = None
        self.relative_left = None
        self.relative_bottom = None
        self.relative_right = None
        self.reader = None
        self.path = path
        self._configs = self.configs if configs is None else configs
        self.creditor = creditor
        self.start_page = self.configs[creditor]["start_page"]
        self.relative_top = self.configs[creditor]["relative_top"]
        self.relative_left = self.configs[creditor]["relative_left"]
        self.relative_bottom = self.configs[creditor]["relative_bottom"]
        self.relative_right = self.configs[creditor]["relative_right"]

    path = property(operator.attrgetter('_path'))

    @path.setter
    def path(self, p):
        try:
            # Validations
            self.reader = PyPDF2.PdfFileReader(open(p, "rb"))
            print("PDF file valid")
        except Exception:
            raise ValueError("Error: Invalid PDF file")
        self._path = p

    creditor = property(operator.attrgetter('_creditor'))

    @creditor.setter
    def creditor(self, c):
        if c not in self.configs:
            raise ValueError("Configs for creditor: %s does not exist" % c)
        self._creditor = c

    def get_last_page(self):
        return str(self.reader.getNumPages())

    def get_page_range(self):
        return "%s-%s" % (self.start_page, self.get_last_page())

    def get_relative_area_percentages(self):
        return [
            self.relative_top,
            self.relative_left,
            self.relative_bottom,
            self.relative_right
        ]
