# coding: utf-8

import MySQLdb

def selectMySql_user(user):
    value = user
    try:
        conn = MySQLdb.connect(host='192.168.40.219', port=3306, user='wenjiaan', passwd='wenjiaan_2017', db='music')
        cur = conn.cursor()
    except Exception, e:
        print u'操作mysql数据库失败'
    else:
        cur.execute('select id from user where mobile = (%s)', value)
        data = cur.fetchall()
    finally:
        cur.close()
        conn.close()

    userid = data[0][0]

    return userid

def selectMySql_teacher(teacher):
    value = teacher
    try:
        conn = MySQLdb.connect(host='192.168.40.219', port=3306, user='wenjiaan', passwd='wenjiaan_2017', db='music')
        cur = conn.cursor()
    except Exception, e:
        print u'操作mysql数据库失败'
    else:
        cur.execute('select id from user_teacher where mobile = (%s)', value)
        data = cur.fetchall()
    finally:
        cur.close()
        conn.close()
    teacherid = data[0][0]
    return teacherid

# selectMySql_user(14155667788)

# conn = MySQLdb.connect(host='192.168.40.219', port=3306, user='chengeng', passwd='chengeng123', db='music')
# cur = conn.cursor()
# cur.execute('select * from user where mobile = 14155667788')
# data = cur.fetchall()
# print data