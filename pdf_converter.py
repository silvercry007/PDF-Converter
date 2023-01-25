from pdf2docx import Converter

pdf_file = "Resume.pdf"
docx_file = "New_doc.docx"
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()