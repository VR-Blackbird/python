import pdfplumber


with pdfplumber.open("sample.pdf") as f:
    for i in f.pages:
        print(i.extract_tables())