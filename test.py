# -*- coding: utf-8 -*-
# extracting_text.py
import PyPDF2
from PyPDF2 import PdfFileReader


def text_extractor(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)

        # get the first page
        page = pdf.getPage(1)
        print(page)
        print('Page type: {}'.format(str(type(page))))

        text = page.extractText()
        print(text)


if __name__ == '__main__':
    path1 = '1800271039-1.pdf'
    path = 'ipsn2016.pdf'
    pdfFileObj1 = open(path, 'rb')
    pdfFileObj2 = open(path, 'rb')
    pdfReader1 = PyPDF2.PdfFileReader(pdfFileObj1)
    pdfReader2 = PyPDF2.PdfFileReader(pdfFileObj2)

    pdfWriter = PyPDF2.PdfFileWriter()
    # 合并pdf
    for pageIndex in zip(range(pdfReader1.numPages), range(pdfReader2.numPages - 1, -1, -1)):
        page1 = pdfReader1.getPage(pageIndex[0])
        page2 = pdfReader2.getPage(pageIndex[1])
        # print(page1.extractText())
        pdfWriter.addPage(page1)
        pdfWriter.addPage(page2)

    pdfOutput = open('output.pdf', "wb")
    pdfWriter.write(pdfOutput)
    pdfOutput.close()
    pdfFileObj1.close()
    pdfFileObj2.close()
