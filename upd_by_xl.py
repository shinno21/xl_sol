import openpyxl
import urllib3
import json

"""
一覧取得Webサービス
Python3
"""

FILE_NAME = "test.xlsx"
URL = 'http://127.0.0.1:8000/api/application_inf/'
HTTP_METHOD = 'POST'
COLUMNS = [
    'id', 'name', 'r_name', 'classification', 'team', 'summary', 'text', 'user'
]

CONTENT_TYPE = 'application/json'
AUTH_PREFIX = 'Token '
AUTH_TOKEN = '3799dec4212f96d6aa9b03827c2d08325c2d1c20'
AUTHORIZATION = AUTH_PREFIX + AUTH_TOKEN


if __name__ == '__main__':
    # 既存のファイルをロード
    wb = openpyxl.load_workbook(FILE_NAME)
    ws = wb.active

    # 表全体の取得
    rows = ws.rows

    # 初期化 行ごとのリスト
    table_list = []

    # 初期化 1行を辞書化
    row_dict = {}

    # 表の内容を辞書のリスト化
    for row in rows:
        for col_num, col in enumerate(row):
            row_dict[COLUMNS[col_num]] = col.value
        table_list.append(row_dict)
        row_dict = {}
    
    table = json.dumps(table_list[0], separators=(',', ':'))
    print(table)

    http = urllib3.PoolManager()
    r = http.request(HTTP_METHOD, URL,
        headers={'Content-Type': CONTENT_TYPE,
                'Authorization': AUTHORIZATION},
        body=table)
    print(r.status, r.data)
