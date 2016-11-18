import xlrd
import xlwt

book = xlrd.open_workbook("Workbook1.xlsx")

print "the number of worksheet is {0}".format(book.nsheets)

print "worksheet name: {0}".format(book.sheet_names())

sh = book.sheet_by_index(0)

print "{0}  {1} {2}".format(sh.name, sh.nrows, sh.ncols)

for rowindex in range(0, sh.nrows):
	for column_value in sh.row_values(rowindex):
		print column_value

# print "Cell D2 is {0}".format(sh.cell_value(rowx=2, colx=3))

# workbook = xlwt.Workbook()

# sheet = workbook.add_sheet('Sheettttt')

# toWrite = {
# 	"a" : "b",
# 	"c" : "d",
# 	"e" : "f"
# }

# for index, value in enumerate(toWrite):
# 	sheet.write(0, index, value)

# workbook.save("XLWT.xls")

