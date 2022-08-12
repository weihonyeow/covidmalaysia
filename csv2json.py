'''
parse csv to json
:param csv: csv_text
:return: json
'''
import json 
import csv
def csv2json(csv_text):
    # split csv_text to rows
    rows = csv_text.split('\n')
    # split each row to columns
    columns = rows[0].split(',')
    # return a object of json
    json = {}
    for row in rows[1:]:
        if row:
            json [row.split(',')[0]] = {
                columns[i]: row.split(',')[i] for i in range(1, len(columns))
            }
    return json
    
# for debug only!
if __name__ == '__main__':
    print(csv2json('date,confirmed,recovered,deaths\n'
                '1/1/2020,1,0,0\n'
                '1/2/2020,2,0,0\n'
                '1/3/2020,3,0,0\n'
                '1/4/2020,4,0,0\n'
                '1/5/2020,5,0,0\n'
    ))