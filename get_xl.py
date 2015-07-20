# coding: utf-8
import openpyxl
import urllib3
import json

"""
一覧取得Webサービス
Python3
"""

FILE_NAME = "test.xlsx"
URL = 'http://127.0.0.1:8000/api/application_inf/'
HTTP_METHOD = 'GET'
COLUMNS = [
    'id', 'name', 'team'
]

if __name__ == '__main__':

    # 既存のファイルをロード
    wb = openpyxl.load_workbook(FILE_NAME)
    ws = wb.active

    http = urllib3.PoolManager()
    r = http.request(HTTP_METHOD, URL)

    # binaryで返ってくるため ascii にdecode
    stream = r.data.decode('ascii')
    decoder = json.JSONDecoder()

    print(stream)
    obj, index = decoder.raw_decode(stream)

    # enumerate で object と index を返す
    for row_num, row in enumerate(obj, start=1):
        for col_num, col in enumerate(COLUMNS, start=1):
            ws.cell(row=row_num, column=col_num, value=row[col])

    # 上書き保存
    wb.save(FILE_NAME)
