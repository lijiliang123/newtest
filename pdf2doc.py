# by thomas_ljl on 2023/12/2
# 将PDF文件转换为docx文件

from pdf2docx import parse

pdf_file = 'sample.pdf'
docx_file = 'sample2.docx'

# convert pdf file into docx file
parse(pdf_file, docx_file)
