# coding: utf-8

import MySQLdb

# 数据库查找classroom


def selectMySql(classid):
    # global recordid
    value = classid
    try:
        conn = MySQLdb.connect(host='192.168.40.219', port=3306, user='wenjiaan', passwd='wenjiaan_2017', db='music')
        # conn = MySQLdb.connect(host='192.168.40.219', port=3306, user='root', passwd='123456', db='music')
        cur = conn.cursor()
        cur.execute('SELECT time_class,time_end FROM class_room WHERE id = (%s)', value)
        data = cur.fetchall()
        start_time = data[0][0] - 7200
        end_time = data[0][1] - 7200
        print start_time
        print end_time
        upsql = "update class_room set time_class = %s,time_end = %s, status = 1 where id = %s"
        upparams = (start_time, end_time, value)
        cur.execute(upsql, upparams)
        # conn.commit()
        insql = "insert into class_record (class_id, content, student_content, target, process, remark, undo_reason, performance, note_accuracy, rhythm_accuracy, coherence, score, on_time, net, manner, understanding, tag_bit, zan_times, time_created, time_updated, time_send, time_comment, class_left, class_used, is_view, total_score, teacher_grade, is_student_comment, self_audio, is_read, student_comment, time_read, is_edit) values (%s,'sdfadfsdf','','','asfsdfsdf','','','0','0','0','0','0','0','0','0','0','','0','1516616334','0','0','0','0','0','0','0','0','0','','0','','0','0')"
        cur.execute(insql, value)
        conn.commit()
    except Exception, e:
        print e
    else:
        cur.execute('SELECT * FROM class_record WHERE class_id = (%s)', value)
        data1 = cur.fetchall()
        recordid = data1[0][0]
        print data1
        print recordid
    finally:
        cur.close()
        conn.close()
    return recordid

def selectMySql2(classid):
    value = classid
    try:
        conn = MySQLdb.connect(host='192.168.40.219', port=3306, user='wenjiaan', passwd='wenjiaan_2017', db='music')
        # conn = MySQLdb.connect(host='192.168.40.219', port=3306, user='root', passwd='123456', db='music')
        cur = conn.cursor()
    except Exception, e:
        print e
    else:
        cur.execute('SELECT * FROM class_record WHERE class_id = (%s)', value)
        data1 = cur.fetchall()
        recordid = data1[0][0]
        print data1
        print recordid
    finally:
        cur.close()
        conn.close()
    return recordid



    # print data
    # start_time = data[0][0]-86400
    # end_time = data[0][1]-86400
    # try:
    # conn = MySQLdb.connect(host='192.168.40.238', port=3306, user='root', passwd='123456', db='music')
    # cur = conn.cursor()
    # sql = "update class_room set time_class = %s,time_end = %s where id = %s"
    # params = (start_time, end_time, value)
    # cur.execute(sql, params)
    # conn.commit()
    # except Exception, e:
    #     print u'操作mysql数据库失败'
    # else:
    #     print u'修改后表的数据为：' + selectMySql(classid)
    # finally:
    # cur.close()
    # conn.close()
    # print start_time
    # print end_time
    # return userid

# 数据库更新
# def updateMySQL():
#     try:
#         conn = MySQLdb.connect(host='192.168.40.219', port=3306, user='chengeng', passwd='chengeng123', db='music')
#         cur = conn.cursor()
#         sql = 'update user set NAME=%s where id=%s'
#         params = ('selenium webdriver', '1')
#         cur.execute(sql, params)
#         conn.commit()
#     except Exception ,e:
#         print u'操作mysql数据库失败'
#     else:
#         print u'修改后表的数据为：'+selectMySql(user)
#     finally:
#         cur.close()
#         conn.close()

# def selectMySql_teacher(teacher):
#     value = teacher
#     try:
#         conn = MySQLdb.connect(host='192.168.40.219', port=3306, user='wenjiaan', passwd='wenjiaan_2017', db='music')
#         cur = conn.cursor()
#     except Exception, e:
#         print u'操作mysql数据库失败'
#     else:
#         cur.execute('select id from user_teacher where mobile = (%s)', value)
#         data = cur.fetchall()
#     finally:
#         cur.close()
#         conn.close()
#     teacherid = data[0][0]
#     return teacherid

# selectMySql(118818956)

# conn = MySQLdb.connect(host='192.168.40.219', port=3306, user='chengeng', passwd='chengeng123', db='music')
# cur = conn.cursor()
# cur.execute('select * from user where mobile = 14155667788')
# data = cur.fetchall()
# print data