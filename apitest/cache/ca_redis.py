# coding: utf-8

import redis

def caRedis(classid, recordid):
    r = redis.Redis(host='192.168.40.112', port=6379, db=7)
    data = 'music-class_room-'+str(classid)
    data1 = 'music-class_record-'+str(recordid)
    rs = r.get(data)
    rs1 = r.get(data1)
    print rs
    print rs1

# caRedis(2144751, 42119)

def caRedisSigne(classid, recordid):
    r = redis.Redis(host='192.168.40.112', port=6379, db=7)
    data = 'music-class_room-'+str(classid)
    data1 = 'music-class_record-'+str(recordid)
    rs = r.get(data)
    rs1 = r.get(data1)
    print rs
    print rs1