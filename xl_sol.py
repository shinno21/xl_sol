# coding: utf-8
import xlrd

if __name__ == '__main__':
    book = xlrd.open_workbook('test_data.xlsx')
    sheet1 = book.sheet_by_index(0)

    for col in [0,1,3]:
        print("------------------")
        for row in range(sheet1.nrows):
            print(sheet1.cell(row, col).value)
