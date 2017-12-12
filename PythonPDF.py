import PyPDF2

pdfFileObj = open('medicalex.pdf')
pdfReader = PyPDF2.PdfFileReader()

pdfFileObj.close()
