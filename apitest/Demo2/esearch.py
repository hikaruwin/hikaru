# coding: utf-8

from elasticsearch import Elasticsearch
import sys
from elasticsearch.exceptions import *

reload(sys)
sys.setdefaultencoding('utf-8')

def elasticSearch(classid):
    es = Elasticsearch(['192.168.40.111'], port=9200)
    try:
        res = es.get(index='qa-class', doc_type='class_record', id=str(classid))
    except NotFoundError, e:
        print u'error'
    else:
        print res

# elasticSearch(2145457)