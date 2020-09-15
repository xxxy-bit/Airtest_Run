# -*- encoding=utf8 -*-
__author__ = "xy"
__title__ = "使用连连支付付款"
__desc__ = """
用例内容：
1.点击申领机器按钮
2.跳转礼包页面
3.选择礼包
4.输入银行卡信息
5.跳转连连支付页面
6.跳转成功，返回主页
"""

from airtest.core.api import *

auto_setup(__file__)

touch(Template(r"tpl1596506583789.png", record_pos=(-0.37, 1.003), resolution=(1080, 2340)))
touch(Template(r"tpl1596507561470.png", record_pos=(-0.062, 0.166), resolution=(1080, 2340)))
sleep(1)
touch(Template(r"tpl1600047550133.png", record_pos=(0.113, -0.675), resolution=(1080, 2340)))
sleep(1)
touch(Template(r"tpl1600047574524.png", record_pos=(0.333, 1.005), resolution=(1080, 2340)))
sleep(1)
touch(Template(r"tpl1600047574524.png", record_pos=(0.333, 1.005), resolution=(1080, 2340)))
sleep(1)
touch(Template(r"tpl1596849512075.png", record_pos=(-0.091, -0.023), resolution=(1080, 2340)))
text("黄小元")
touch(Template(r"tpl1596849530275.png", record_pos=(-0.052, 0.094), resolution=(1080, 2340)))
text("441900199410112017")
touch(Template(r"tpl1596849546579.png", record_pos=(-0.021, 0.209), resolution=(1080, 2340)))
text("622908393179901817")

touch(Template(r"tpl1596849595322.png", record_pos=(0.004, 0.499), resolution=(1080, 2340)))
sleep(1)
assert_exists(Template(r"tpl1596849674120.png", record_pos=(-0.14, -0.794), resolution=(1080, 2340)), "进入支付页面成功")

touch(Template(r"tpl1594885416705.png", record_pos=(-0.436, -0.942), resolution=(1080, 2340)))