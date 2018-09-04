# coding: utf-8

import os
import csv
import xlrd
import xml.dom.minidom
import sqlite3
import MySQLdb

class Config(object):
    def __init__(self):
        pass
    @staticmethod
    def data_dirs():
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        DATA_DIRS = (os.path.join(BASE_DIR, 'Data-Driven'),)
        print DATA_DIRS
        d = '/'.join(DATA_DIRS)
        print d
        return d

class DataHelper(object):
    def __init__(self):
        pass
    # def data_dirs(self):
    #     BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #     # print BASE_DIR
    #     DATA_DIRS = (os.path.join(BASE_DIR, 'Data-Driven'),)
    #     # print DATA_DIRS
    #     d = '/'.join(DATA_DIRS)
    #     # print d
    #     return d

    def getList(self):
        list = [['', '', u'请您输入手机/邮箱/用户名'],['admin', '', u'请您输入密码'],['admin', 'admin', u'请您输入验证码']]
        return list

    def readFile(self, index):
        f = open(Config.data_dirs()+'/system.txt', 'r')
        d = f.readlines()
        f.close()
        return d[index]

    def readCsv(self, value1, value2):
        rows = []
        data_file = open(Config.data_dirs()+'/system.csv')
        reader = csv.reader(data_file)
        next(reader, None)
        for row in reader:
            rows.append(row)
        return ''.join(rows[value1][value2]).decode('gb2312')

    def readExcel(self, rowValue, colValue):
        book = xlrd.open_workbook(Config.data_dirs()+'/system.xlsx')
        sheet = book.sheet_by_index(0)
        return sheet.cell_value(rowValue, colValue)

    def readExcels(self):
        rows = []
        book = xlrd.open_workbook(Config.data_dirs()+'/system.xlsx')
        sheet = book.sheet_by_index(0)
        for row in range(1, sheet.nrows):
            print row
            print sheet.nrows
            rows.append(list(sheet.row_values(row, 0, sheet.ncols)))
            print sheet.ncols
            # print rows
        # print rows
        return rows



    def getXmlData(self, value):
        dom = xml.dom.minidom.parse(Config.data_dirs()+'/system.xml')
        db = dom.documentElement
        name = db.getElementsByTagName(value)
        nameValue = name[0]
        return nameValue.firstChild.data

    def getXmlUser(self, parent, child):
        dom = xml.dom.minidom.parse(Config.data_dirs() + '/system.xml')
        db = dom.documentElement
        itemlist = db.getElementsByTagName(parent)
        item = itemlist[0]
        return item.getAttribute(child)

class SqliteHelper(object):
    def selectSqlite(self, value1, value2):
        rows = []
        try:
            conn = sqlite3.connect(Config.data_dirs()+'/mydatabase.db')
            cur = conn.cursor()
            sql = 'select * from element'
            cur.execute(sql)
            data = cur.fetchall()
            for d in data:
                rows.append()
            return rows[value1][value2]
        except:
            print u'操作sqlite3数据库失败'
        finally:
            cur.close()
            conn.close()

class MySQLHelper(object):
    def __init__(self):
        pass
    # @property
    def selectMySQL(self, index1, index2):
        rows = []
        try:
            conn = MySQLdb.connect(host='192.168.40.219', port=3306, user='chengeng', passwd='chengeng123', db='music')
            cur = conn.cursor()
        except Exception ,e:
            print u'操作mysql数据库失败'
        else:
            cur.execute('select * from user WHERE mobile = 14155667788;')
            data = cur.fetchall()
            for d in data:
                rows.append(d)
            print rows
            abc = rows[index1][index2]
            print abc
            return rows[index1][index2]
        finally:
            cur.close()
            conn.close()

    @property
    def insertMySQL(self):
        try:
            conn = MySQLdb.connect(host='192.168.40.219', port=3306, user='chengeng', passwd='chengeng123', db='music')
            cur = conn.cursor()
            sql = 'insert into user(id, name, sex, adress) VALUE (%s, %s, %s, %s)'
            params = ('1', 'selenium 2', 'boy', 'USA')
            cur.execute(sql, params)
            conn.commit()
        except Exception ,e:
            print u'操作mysql数据库失败'
        else:
            print u'插入后表的数据为：'
            self.selectMySQL
        finally:
            cur.close()
            conn.close()

    @property
    def updateMySQL(self):
        try:
            conn = MySQLdb.connect(host='192.168.40.219', port=3306, user='chengeng', passwd='chengeng123', db='music')
            cur = conn.cursor()
            sql = 'update user set NAME=%s where id=%s'
            params = ('selenium webdriver', '1')
            cur.execute(sql, params)
            conn.commit()
        except Exception ,e:
            print u'操作mysql数据库失败'
        else:
            print u'修改后表的数据为：'
            self.selectMySQL
        finally:
            cur.close()
            conn.close()

    @property
    def deleteMySQL(self):
        try:
            conn = MySQLdb.connect(host='192.168.40.219', port=3306, user='chengeng', passwd='chengeng123', db='music')
            cur = conn.cursor()
            sql = 'delete from USER WHERE id=%s'
            params = ('1')
            cur.execute(sql, params)
            conn.commit()
        except Exception ,e:
            print u'操作mysql数据库失败'
        else:
            print u'删除后表的数据为：'
            self.selectMySQL
        finally:
            cur.close()
            conn.close()

# f = MySQLHelper()
# f.selectMySQL(0,0)

class User(object):
    def __init__(self):
        self.__helper = MySQLHelper()

    def get_One(self, id):
        sql = 'select * from account WHERE id=%s'
        params=(id,)
        return self.__helper.get_One(sql, params)

    def checkValidate(self, name, address):
        sql = 'select * from account WHERE username=%s and passwd=%s'
        params = (name, address,)
        return self.__helper.get_One(sql, params)

if __name__ == '__main__':
    obj = Config()
    obj.data_dirs()