import sys
import openpyxl

words = list()
wb = openpyxl.Workbook()
sheet = wb.active

if len(sys.argv) > 2:
    for i in range(1, len(sys.argv)):
        with open(sys.argv[i], 'r') as file:
            while True:
                line = file.readline()
                if not line:
                    break
                words.append(line.removesuffix("\n"))
        file.close()
        print(words)
        for k in range(1, len(words)+1):
            sheet.cell(row=k, column=i).value = words[k-1]
        words = list()

    wb.save("text_to_excel.xlsx")
else:
    print("No files found")

