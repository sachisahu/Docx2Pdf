#install package pip install docx2pdf
#import library
#pip install fpdf



import os
from fpdf import FPDF
from docx2pdf import convert
#Convertion of .txt to .pdf
pdf=FPDF()
pdf.add_page()
pdf.set_font("Arial", size = 15)
f = open("sam.txt", "r")
for x in f:
    pdf.cell(200, 10, txt = x, ln = 1, align = 'C')
pdf.output("txt/mygfg.pdf")
print("\nTxt File Conversion Successful")

#Convertion of .docx to .pdf
x=os.path.basename('sample.docx')
y=x.split('.')
out=y[0]+".pdf"
convert(x,r"docx/")
print("\nFile "+x+" to " + out + " \nConversion Successful")




