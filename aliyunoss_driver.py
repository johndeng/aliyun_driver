#!/usr/bin/env  python
#-*- coding:utf-8 -*-

from oosAPI.oss_api import *


class driver_oss():
	"""
	
	此模块提供文件上传，删除文件接口	
	
	"""

	def __init__(self, host, id, key):
		self.host = host
		self.id   = id
		self.key  = key
		self.oss  = OssAPI(host, id, key)


	def upload_data(self, bucket, object, filename):

		res = self.oss.put_object_from_file(bucket, object, filename)
		if (res.status / 100) == 2:
			print "upload_file Sccess"
		else:
			print "upload_file Error"

	def delete_data(self, bucket, object):  

		res = self.oss.delete_object(bucket, object)
		if (res.status / 100) == 2:
			print "delete_file Sccess"
		else:
			print "delete_file Error"
