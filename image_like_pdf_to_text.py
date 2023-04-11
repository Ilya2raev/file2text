import os

from pdf_to_image import pdf_to_image
from image_to_text import image_to_text
from write_file import write_file
from filename import filename

if __name__ == '__main__':
    try:               
        result = ''
        pages_list = pdf_to_image(filename)

        for page in pages_list:
            result += image_to_text(page)

    finally:
        write_file(result)

        for image in pages_list:
            os.remove(image)
            