# -*- encoding=utf8 -*-
__author__ = "xy"
__title__ = "查看我的钱包"
__desc__ = """
用例内容：
1.点击我的钱包
2.显示收益明细数据
3.返回主页
"""

from airtest.core.api import *

auto_setup(__file__)

touch(Template(r"tpl1596506583789.png", record_pos=(-0.37, 1.003), resolution=(1080, 2340)))
touch(Template(r"tpl1596506763631.png", record_pos=(-0.119, -0.243), resolution=(1080, 2340)))
sleep(1)

assert_exists(Template(r"tpl1596506772070.png", record_pos=(0.003, -0.835), resolution=(1080, 2340)), "进入'我的钱包'页面成功")
sleep(0.5)
touch(Template(r"tpl1594885416705.png", record_pos=(-0.436, -0.942), resolution=(1080, 2340)))

