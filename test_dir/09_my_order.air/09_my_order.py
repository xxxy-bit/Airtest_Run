# -*- encoding=utf8 -*-
__author__ = "xy"
__title__ = "查看我的订单"
__desc__ = """
用例内容：
1.点击我的订单
2.显示下单机器数据
3.返回主页
"""

from airtest.core.api import *

auto_setup(__file__)

touch(Template(r"tpl1594866876384.png", record_pos=(0.381, 1.011), resolution=(1080, 2340)))
sleep(0.5)

touch(Template(r"tpl1597132866347.png", record_pos=(0.106, -0.077), resolution=(1080, 2340)))
sleep(1)

assert_exists(Template(r"tpl1597132905569.png", record_pos=(-0.334, -0.835), resolution=(1080, 2340)), "进入“我的订单”页面成功")
touch(Template(r"tpl1594885416705.png", record_pos=(-0.436, -0.942), resolution=(1080, 2340)))

