import os
from pypdf import PdfWriter

pdfFilter = lambda x:x.endswith(".pdf")
merger = PdfWriter()

list_files = list(filter(pdfFilter,os.listdir()))

list_files.sort()

for pdf_item in list_files:
    merger.append(pdf_item)

merger.write("merged-ww1-countries.pdf")
merger.close()