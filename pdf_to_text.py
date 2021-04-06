from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from io import StringIO
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter


class PdfToText:
    def __init__(self):
        self.pages = []

    def read_pdf(self, pdf_path):
        """Reads PDF file, extracted text is stored in self.pages
        :type pdf_path: str"""
        with open(pdf_path, "rb") as pdf_file:
            # Code adapted from http://survivalengineer.blogspot.com/2014/04/parsing-pdfs-in-python.html
            # Create the document model from the file
            parser = PDFParser(pdf_file)
            document = PDFDocument(parser)
            # Try to parse the document
            if not document.is_extractable:
                raise PDFTextExtractionNotAllowed
            # Create a PDF resource manager object
            # that stores shared resources.
            rsrc_mgr = PDFResourceManager()
            # Create a buffer for the parsed text
            ret_str = StringIO()
            # Spacing parameters for parsing
            laparams = LAParams()

            # Create a PDF device object
            device = TextConverter(rsrc_mgr, ret_str, laparams=laparams)
            # Create a PDF interpreter object
            interpreter = PDFPageInterpreter(rsrc_mgr, device)

            # Process each page contained in the document.
            # Split each page into lines and append to self.pages
            # pdf_pages = PDFPage.create_pages(document)
            # for page in pdf_pages:
            #     interpreter.process_page(page)
            #     # self.pages.append(ret_str.getvalue())
            #     self.pages.append(ret_str.getvalue().splitlines())
            for page in PDFPage.get_pages(pdf_file):
                interpreter.process_page(page)
                self.pages.append(ret_str.getvalue().splitlines())

                # Has to be zero, otherwise the next page will include text from all pages
                # ret_str.truncate(0)
                ret_str.seek(0)

    def get_page(self, page_num):
        """Returns a specific page from self.pages. Pages start from zero 0.
        :type page_num: int
        :rtype """
        if page_num < len(self.pages):
            requested_page = self.pages[page_num]
            page_text = ""
            for line in requested_page:
                page_text += line + "\n"

            return page_text
        else:
            return f"Cannot return page num {page_num}. Document has only {len(self.pages)} page/s."
