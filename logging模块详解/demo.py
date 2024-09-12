# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      : 2024/9/12 11:49
# @FileName  : demo.py
# @Author    : Doraemon
import logging.config

config = {
    'version': 1,
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        },
        # 其他的 formatter
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'simple'
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'logging.log',
            'level': 'DEBUG',
            'formatter': 'simple'
        },
        # 其他的 handler
    },
    'loggers':{
        # 默认的 logger，无法匹配其他logger对象时，默认使用它，如果匹配，则使用匹配的logger + 默认的logger
        '': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
        'error': {
            # 既有 console Handler，还有 file Handler
            'handlers': ['console'],
            'level': 'ERROR',
        },
        'app.member': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },

        # 其他的 Logger
    }
}

logging.config.dictConfig(config)

# 假如__name__的值无法匹配 logger的name，则使用默认的 logger，如果匹配，则使用匹配的 logger+默认的logger
# logger = logging.getLogger(__name__)
# logger.warning("default")

logger = logging.getLogger("app.member.xx")
logger.warning("member")



