import xlsxwriter 
import re

def open_list():
	with open('list.txt', 'r') as f:
		c = f.read()
		f.close()
		return c

def making_list():
	str_list = open_list()
	list_file = str_list.split('\n')
	return list_file


def script_to_xls(name):
	workbook = xlsxwriter.Workbook('name.xls')
	worksheet = workbook.add_worksheet()

	row = 1
	col = 0
	
	worksheet.write(0,0,'№')
	worksheet.write(0,1,'Адреса')


	list_file = making_list()
	#for d in list_file:
	#	results = re.findall(r'',d)
	#	
	#	print(results)
	

	for n in range(1, len(list_file) + 1):
		worksheet.write(row, col, n)
		row +=1

	row = 1

	for m in (list_file):
		worksheet.write(row, col + 1, m)
		row += 1

	workbook.close() 

making_list()
script_to_xls('check1')