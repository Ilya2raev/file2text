import pdf2image
import pytesseract
import os

from filename import filename
from write_file import write_file

def image_like_pdf_to_text(filename):
    pytesseract.pytesseract.tesseract_cmd = os.path.join(os.getcwd(), r"tesseract\tesseract.exe")
    image = pdf2image.convert_from_path(filename, 500, 
                                poppler_path=os.getcwd()+r'\poppler-0.68.0\bin')
    result = ''

    try:
        for page in image:
            result += pytesseract.image_to_string(page, lang='eng+rus')
            write_file(result)

    finally:
        return result

if __name__ == '__main__':
    image_like_pdf_to_text(filename)
