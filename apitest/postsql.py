# coding: utf-8

import psycopg2

# 数据库连接参数
conn = psycopg2.connect(database="bank_dev_test", user="zhuhang", password="123456a", host="172.16.0.20", port="5432")
value = 'allergy.patient_allergy'
cur = conn.cursor()

cur.execute('SELECT * FROM allergy.patient_allergy')
rows = cur.fetchall()        # all rows in table
print(rows[0][0])
conn.commit()
cur.close()
conn.close()