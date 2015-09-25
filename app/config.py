# coding: utf-8
#
# Copyright (c) 2014 Tirith
# Copyright (c) 2015 Netsevers Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License")
#
# Author: Thiago Ribeiro
# Email ribeiro dot it at gmail dot com
# Created: Sep 4, 2014, 2:39 PM
#
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# Statement for enabling the development environment
DEBUG = False
DEBUG_TB_INTERCEPT_REDIRECTS = False
# App name
APP_NAME = os.environ['APP_NAME'] if 'APP_NAME' in os.environ else 'AD password changer'
# App host
SERVER_HOST = '0.0.0.0'
# App port
SERVER_PORT = 7777
# Secret key for signing cookies
# echo '<your_passphrase>' | md5
SECRET_KEY = os.environ['SECRET_KEY'] if 'SECRET_KEY' in os.environ else 'de7d72d42dc64185bfc7d37b911fac65'
# Ad Server
AD_SERVER = os.environ['AD_SERVER']
