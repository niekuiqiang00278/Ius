#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/24 4:38
# @Author  : cap669
# @File    : DataConfig.py
# @Software: PyCharm
# from abc import ABC,ABCMeta,abstractmethod
from pydantic import BaseModel, BaseConfig, BaseSettings
from functools import lru_cache

from Config import env


class DataConfig(BaseSettings):
    executable_path:str= 'C:\Kac\Tool\chromedriver.exe'
    host:str= '127.0.0.1'
    port:int
    clash:bool
class DevDataConfig(DataConfig):
    port = 9222
    clash = True

class ProDataConfig(DataConfig):
    port = 9222
    clash = False

@lru_cache()
def register_config() -> DataConfig:
    return dict(
        dev=DevDataConfig,
        por=ProDataConfig,
    )[env]()


dataconf = register_config()

# Tips     :
