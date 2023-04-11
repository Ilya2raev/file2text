from pdf2image import convert_from_path
import os

def pdf_to_image(filename):
    pages_list = []
    pages = convert_from_path(filename, 500, 
                              poppler_path=os.getcwd()+r'\poppler-0.68.0\bin')

    for i in range(len(pages)):
        pages[i].save('page' + str(i) + '.jpg', 'JPEG')
        pages_list.append('page' + str(i) + '.jpg')

    return sorted(pages_list)
