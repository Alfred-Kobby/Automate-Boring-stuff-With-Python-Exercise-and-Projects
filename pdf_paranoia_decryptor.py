import PyPDF2, os
from pathlib import Path

password = input("Enter Password to encrypt pdf\n")

pdf_folder = "encrypted_pdf"

# Decrypting Files
for folderName, subfolders, filenames in os.walk(Path.cwd().parent / pdf_folder):
    for filename in filenames:
        if filename.endswith('.pdf'):
            full_path = os.path.join(folderName, filename)
            pdfFileReader2 = PyPDF2.PdfReader(full_path)
            if pdfFileReader2.is_encrypted:
                print("Decrypting file: ", filename)
                pdfFileReader2.decrypt(password)
                print(pdfFileReader2.pages[0])
