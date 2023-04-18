import pytesseract
import cv2
import os

from filename import filename
from write_file import write_file

def image_to_text(filename):
    pytesseract.pytesseract.tesseract_cmd = os.path.join(os.getcwd(), r"tesseract\tesseract.exe")
    image = cv2.imread(os.path.join(os.getcwd(), filename))
    string = pytesseract.image_to_string(image, lang='eng+rus')

    return string

if __name__ == '__main__':
    result = ''
    
    try:
        result = image_to_text(filename)
    finally:
        write_file(result)
    