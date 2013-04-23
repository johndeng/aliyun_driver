#!/usr/bin/env  python
#-*- coding:utf-8 -*-

from oss_api import *
from oss_xml_handler import *

HOST = ''
ACCESS_ID = ''
SECRET_ACCESS_KEY = ''

class driver_oss():
	"""
	
	此模块提供文件上传，删除文件接口	
	
	"""

	def __init__(self, host, id, key):
		self.host = host
		self.id   = id
		self.key  = key
		self.oss  = OssAPI(HOST, id, key)


	def upload_data(self, bucket, object, filename):

		res = self.oss.put_object_from_file(bucket, object, filename)
		if (res.status / 100) == 2:
			print "upload_file Sccess"
		else:
			return "upload_file Error"

	def delete_data(self, bucket, object):  

		res = self.oss.delete_object(bucket, object)
		if (res.status / 100) == 2:
			print "delete_file Sccess"
		else:
			print "delete_file Error"