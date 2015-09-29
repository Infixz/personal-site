#!/usr/bin/python
# coding:utf-8

import tornado.httpserver as httpserver
import tornado.ioloop as ioloop
import tornado.web as web

from pymongo import MongoClient

from config import settings


class IndexHandler(web.RequestHandler):
	"""docstring for IndexHandler"""
	#def __init__(self, arg):
	#	super(IndexHandler, self).__init__()
	#	self.arg = arg
	def get(self):
		greetingwords = self.get_argument('greeting','hello')
		self.write(greetingwords + u',再次见面分外眼红')


class ResumeHandler(web.RequestHandler):
	"""docstring for ResumeHandler"""
	#def __init__(self, arg):
	#	super(ResumeHandler, self).__init__()
	#	self.arg = arg
	def get(self):
		self.render('resume.html')


class App(web.Application):
	"""docstring for App"""
	def __init__(self):
		handlers = [(r'/',IndexHandler),(r'/resume',ResumeHandler)]
		client = MongoClient()
		self.db = client.usertest
		web.Application.__init__(self,handlers,**settings)




if __name__ == '__main__':
	"""app = web.Application(
		handlers=[(r'/',IndexHandler),(r'/resume',ResumeHandler)],
		
		debug=True
		)"""
	http_server = httpserver.HTTPServer(App())
	http_server.listen(8080)
	ioloop.IOLoop.instance().start()