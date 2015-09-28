# coding:utf-8
import os.path

import tornado.httpserver as httpserver
import tornado.ioloop as ioloop
import tornado.web as web

class IndexHandler(web.RequestHandler):
	"""docstring for IndexHandler"""
	#def __init__(self, arg):
	#	super(IndexHandler, self).__init__()
	#	self.arg = arg
	def get(self):
		greetingwords = self.get_argument('greeting','hello')
		self.write(greetingwords + u',再次见面分外眼红')
	def write_error(self,status_code,**Kwargs):
		self.write("<h1>日了狗，你把我服务器弄坏了！</h1>")


class ResumeHandler(web.RequestHandler):
	"""docstring for ResumeHandler"""
	#def __init__(self, arg):
	#	super(ResumeHandler, self).__init__()
	#	self.arg = arg
	def get(self):
		self.render('resume.html')
	def write_error(self,status_code,**Kwargs):
		self.write("<h1>日了狗，你把我服务器弄坏了！</h1>")


if __name__ == '__main__':
	app = web.Application(
		handlers=[(r'/',IndexHandler),(r'/resume',ResumeHandler)],
		template_path=os.path.join(os.path.dirname(__file__),"templates"),
		static_path=os.path.join(os.path.dirname(__file__), "static"),
		debug=True
		)
	http_server = httpserver.HTTPServer(app)
	http_server.listen(8080)
	ioloop.IOLoop.instance().start()