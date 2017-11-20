#!/usr/bin/env python
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
from glob import glob
try:
    from PyPDF2 import PdfFileReader, PdfFileWriter
except ImportError:
    from pyPdf import PdfFileReader, PdfFileWriter
import os


def decrpt_pdf(pdfFile, filename):
    if pdfFile.isEncrypted:
        try:
            pdfFile.decrypt('')
            print 'File Decrypted (PyPDF2)'
        except:
            command="cp " + filename + " temp.pdf; qpdf --password='' --decrypt temp.pdf " + filename
            os.system(command)
            print 'File Decrypted (qpdf)'
            #re-open the decrypted file
            fp = open(filename)
            pdfFile = PdfFileReader(fp, 'rb', strict=False)
        return pdfFile

def merge(path, output_filename):
    output = PdfFileWriter()

    for root, dirs, files in os.walk(path):
        for f in files:
            if f.endswith(".pdf"):
                print("Parse '%s'" % os.path.join(root, f))
                document = PdfFileReader(open(os.path.join(root, f), 'rb'), strict=False)
                if document.isEncrypted:
                    document = decrpt_pdf(document, os.path.join(root, f))

                for i in range(document.getNumPages()):
                    output.addPage(document.getPage(i))

    print("Start writing '%s'" % output_filename)
    with open(output_filename, "wb") as f:
        output.write(f)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-o", "--output",
                        dest="output_filename",
                        default="merged.pdf",
                        help="write merged PDF to FILE",
                        metavar="FILE")
    parser.add_argument("-p", "--path",
                        dest="path",
                        default=".",
                        help="path of source PDF files")

    args = parser.parse_args()
    merge(args.path, args.output_filename)
