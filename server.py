# coding:utf-8

import tornado.httpserver as httpserver
import tornado.ioloop ioloop
import tornado.web as web

class IndexHandler(web.RequestHandler):
	"""docstring for IndexHandler"""
	def __init__(self, arg):
		super(IndexHandler, self).__init__()
		self.arg = arg
	def get(self):
		greetingwords = self.get_argument('greeting','hello')
		self.write(greetingwords + ',see you again now')


if __name__ == '__main__':
	app = web.Application(handlers=[(r'/',IndexHandler)])
	http_server = httpserver.HTTPServer(app)
	http_server.listen(80)
	ioloop.IOLoop.instance().start()