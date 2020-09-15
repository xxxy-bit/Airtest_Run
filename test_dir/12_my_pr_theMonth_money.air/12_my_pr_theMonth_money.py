# -*- encoding=utf8 -*-
__author__ = "xy"
__title__ = "查看本月交易额"
__desc__ = """
用例内容：
1.点击本月交易额
2.显示我的业绩数据
3.返回主页
"""

from airtest.core.api import *

auto_setup(__file__)

touch(Template(r"tpl1596506583789.png", record_pos=(-0.37, 1.003), resolution=(1080, 2340)))

touch(Template(r"tpl1596508023012.png", record_pos=(-0.253, 0.346), resolution=(1080, 2340)))

assert_exists(Template(r"tpl1596506628752.png", record_pos=(-0.008, -0.782), resolution=(1080, 2340)), "进入'本月交易额'页面成功")
sleep(0.5)

touch(Template(r"tpl1594885416705.png", record_pos=(-0.436, -0.942), resolution=(1080, 2340)))