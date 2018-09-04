from django.test import TestCase
from models import Event, Guest
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from views import index
from django.template.loader import render_to_string
from django.template import RequestContext

# Create your tests here.
# class ModelTest(TestCase):
#     def setUp(self):
#         Event.objects.create(id=1, name="oneplus 3 event", status=True, limit=2000, address='shenzhen', start_time='2018-08-31 02:18:22')
#         Guest.objects.create(id=1, event_id=1, realname='alen', phone='13711001101', email='alen@mail.com', sign=False)
#
#     def test_event_models(self):
#         result = Event.objects.get(name="oneplus 3 event")
#         self.assertEqual(result.address, "shenzhen")
#         self.assertTrue(result.status)
#         print result.status
#
#     def test_guest_models(self):
#         result = Guest.objects.get(phone='13711001101')
#         self.assertEqual(result.realname, "alen")
#         self.assertFalse(result.sign)

class IndexPageTest(TestCase):
    '''测试index登录首页'''
    def test_root_url_resolves_to_index_page(self):
        '''测试根目录是否解析到登录页'''
        found = resolve('/')
        self.assertEqual(found.func, index)