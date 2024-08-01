from pdf2docx import Converter
pdfFile = 'some.pdf'
docxFile = 'some.docx'
cv = Converter(pdfFile)
cv.convert(docxFile)
cv.close()