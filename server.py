#!/usr/bin/python
# coding:utf-8

import tornado.httpserver as httpserver
import tornado.ioloop as ioloop
import tornado.web as web

from pymongo import MongoClient

from config import settings,DB_HOST,DB_PORT


class IndexHandler(web.RequestHandler):
	"""docstring for IndexHandler"""
	def get(self):
		# greetingwords = self.get_argument('greeting','hello')
		# self.write(greetingwords + u',再次见面分外眼红')
		self.render('index.html')

class ResumeHandler(web.RequestHandler):
	"""docstring for ResumeHandler"""
	def get(self):
		self.render('resume.html')


class MsgHandler(web.RequestHandler):
	"""docstring for MsgHandler"""
	def post(self):
		print 'MsgHandler post'
		try:
			self.coll = self.application.db.leavemsg
		except:
			print 'except'


class GoogleVerify(web.RequestHandler):
	def get(self):
		self.render('google05df3613559d1aa7.html')		
		
class App(web.Application):
	"""docstring for App"""
	def __init__(self):
		handlers = [(r'/',IndexHandler),
					(r'/resume',ResumeHandler),
					(r'/leavemsg',MsgHandler),
					(r'/google05df3613559d1aa7.html',GoogleVerify)
					]
		self.db = MongoClient(DB_HOST,DB_PORT)['usertest']
		web.Application.__init__(self,handlers,**settings)


if __name__ == '__main__':
	http_server = httpserver.HTTPServer(App())
	print 'app has runs on server'
	http_server.listen(8080)
	ioloop.IOLoop.instance().start()
