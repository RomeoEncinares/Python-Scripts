# import module
from PyPDF2 import PdfReader, PdfWriter

source = str(input("File Name: "))

reader = PdfReader(source)
writer = PdfWriter()

for page in reader.pages:
    page.compress_content_streams()  # This is CPU intensive!
    writer.add_page(page)

with open("out.pdf", "wb") as f:
    writer.write(f)