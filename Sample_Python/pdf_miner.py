# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 11:29:03 2020

@author: Muhammed Hassan M
"""


try:
    from cStringIO import StringIO
except ImportError:
    from io import BytesIO

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import re

def convert(fname):
    pages=None
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = BytesIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = open(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    print(text)

    # write to .txt
    text_file = open("output.txt", "w")
    text = re.sub("\s\s+", " ", text.decode('utf-8'))
    text_file.write("%s" % text)
    text_file.close()

convert('C:/Users/Muhammed Hassan M/Desktop/FIR (35).pdf')
