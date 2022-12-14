# import module
from pdf2image import convert_from_path

source = str(input("File Name: "))

images = convert_from_path(source + '.pdf',500,poppler_path=r'D:\Program Files\poppler-22.11.0\Library\bin')

for i in range(len(images)):

	# Save pages as images in the pdf
	images[i].save(source + "_" + str(i) +'.jpg', 'JPEG')