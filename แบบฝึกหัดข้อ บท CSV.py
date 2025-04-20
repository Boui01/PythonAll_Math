#print(end='')ทำให้ไม่ต้องเว้นบรรทัด

lines = [line for line in open("google_stock_data.csv")]
print('ข้อที่ 1')
for i in range(5):
    print(lines[i])

print('ข้อที่ 2')
lines = [line for line in open("google_stock_data.csv")]
for line in lines[-5:]:print(line)#สูตรถอยหลัง
print('\n')

print('ข้อที่ 3')
lines = [line for line in open("google_stock_data.csv")]
lines1 = lines[:5]#เลือกบรรทัด
for line in lines[:5]:
    words = line.split(',')#ใช้เครื่องหมายลูกน้ำค่อมระหว่างข้อความ
    print(words[:3]);#เลือกคอลัมการทำเลือก 2 ครั้งจะเลือกคอลัม
print('\n')


print('ข้อที่ 4')
import csv
file = open("google_stock_data.csv")
reader = csv.reader(file)
data = [ row for row in reader]
for i in range(5):
    Data = data[i]
    print(Data[0:3])
print('\n')

print('ข้อที่ 5')
import json

import pandas as pd

data = pd.read_csv('google_stock_data.csv')
data.head()
data.to_json('google_stock_data.json')
data_json = pd.read_json('google_stock_data.json')
print(data_json.head())
