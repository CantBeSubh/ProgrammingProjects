import sys
import math

sql_query = input()
print(sql_query.find('where'))

rows = int(input())
table_header = input().split(" ")
print(*table_header,sep=" ")
for i in range(rows):
    table_row = input()
    print(table_row,sep=" ")