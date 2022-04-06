import xlrd


book = xlrd.open_workbook('E:\大三下\人工智能\data.xls')
sheet = book.sheet_by_name('Sheet1')
for i in range(sheet.nrows):
    print(sheet.row_values(i))