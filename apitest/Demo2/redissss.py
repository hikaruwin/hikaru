# coding: utf-8

from rediscluster import StrictRedisCluster

def redisCluster(classid, recordid):
    startup_nodes = [{'host': '192.168.40.112', 'port': '7000'}, {'host': '192.168.40.133', 'port': '7000'}, {'host': '192.168.40.141', 'port': '7000'}, {'host': '192.168.40.112', 'port': '7001'}, {'host': '192.168.40.133', 'port': '7001'}, {'host': '192.168.40.141', 'port': '7001'}]
    r = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)
    data1 = 'music-class_room-'+str(classid)
    data2 = 'music-class_record-'+str(recordid)
    rs = r.get(data1)
    rs1 = r.get(data2)
    print rs
    print rs1

# redisCluster(1814805, 12347)