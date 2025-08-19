import PyPDF2, os
from pathlib import Path

password = input("Enter Password to encrypt pdf\n")

# Encrypting Files
pdf_folder = "pdf"
encrypted_pdf_folder = "encrypted_pdf"
file_location = Path.cwd().parent / encrypted_pdf_folder
for folderName, subfolders, filenames in os.walk(Path.cwd().parent / pdf_folder):
    for filename in filenames:
        if filename.endswith('.pdf'):
            full_path = os.path.join(folderName, filename)
            pdfFileReader = PyPDF2.PdfReader(full_path)
            pdfFileWriter = PyPDF2.PdfWriter()
            for pageNum in range(len(pdfFileReader.pages)):
                pdfFileWriter.add_page(pdfFileReader.pages[pageNum])
            pdfFileWriter.encrypt(password)
            full_path_encrypted = os.path.join(file_location, filename)
            resultPdf = open(full_path_encrypted + '_encrypted.pdf', 'wb')
            pdfFileWriter.write(resultPdf)
            pdfFileWriter.close()
