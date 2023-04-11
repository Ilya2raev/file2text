import io
import os
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

from filename import filename
from write_file import write_file

def pdf_to_text(filename):
    rm = PDFResourceManager()
    f = io.StringIO()
    con = TextConverter(rm, f)
    pinter = PDFPageInterpreter(rm, con)

    with open(os.path.join(os.getcwd(), filename), 'rb') as pp:
        for page in PDFPage.get_pages(pp, caching=True, check_extractable=True):
            pinter.process_page(page)
        text = f.getvalue()

    return text

if __name__ == '__main__':
    result = pdf_to_text(filename)
    write_file(result)
    