#!/usr/bin/python
# coding:utf-8

import os.path

settings = dict(template_path=os.path.join(os.path.dirname(__file__),"templates"),
				static_path=os.path.join(os.path.dirname(__file__), "static"),
				debug=True
				)

DB_HOST     = 'localhost'
DB_PORT     = 27017
DB_PASSWORD = None