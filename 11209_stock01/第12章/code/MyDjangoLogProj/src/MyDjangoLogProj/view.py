#!/usr/bin/env python
#coding=utf-8
from django.http import HttpResponse
import sys
import imp
imp.reload(sys) 
import logging
# 參考django日志案例
def logDemo(request):
    logger = logging.getLogger(__name__)
    logger.debug("debug level log")
    logger.warning("warning level log")
    logger.info("info level log")
    logger.error("error level log")
    return HttpResponse("Demo Log.")
# 參考errorOnly日志案例
def errorOnlyDemo(request):
    logger = logging.getLogger('errorOnly')
    logger.debug("debug level log")
    logger.warning("warning level log")
    logger.info("info level log")
    logger.error("error level log")
    return HttpResponse("Only display error log.")