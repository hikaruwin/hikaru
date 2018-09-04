# coding: utf-8

import time
import ca_crmAdd
import ca_sql
import ca_redis
import ca_data
import ca_cancle
from Demo2.esearch import *
from Demo2.redissss import *

def ca_s(data):

    for i in range(1, 2):
        classid = ca_crmAdd.crm(data)
        # time.sleep(2)
        recordid = ca_sql.selectMySql(classid)
        time.sleep(2)
        # redisCluster(classid,recordid)
        ca_redis.caRedis(classid, recordid)
        elasticSearch(classid)
        data = ca_data.ti(data)
        classid = ca_crmAdd.crm(data)
        ca_cancle.crmCn(classid)
        recordid = ca_sql.selectMySql2(classid)
        # redisCluster(classid,recordid)
        time.sleep(2)
        ca_redis.caRedis(classid, recordid)
        elasticSearch(classid)
        data = ca_data.ti(data)

        # time.sleep(3)

ca_s('2018-2-9 14:00')