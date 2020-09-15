# -*- encoding=utf8 -*-
__author__ = "xy"
__title__ = "查看排行榜"
__desc__ = """
用例内容：
1.点击排行榜
2.显示排行榜数据
3.返回主页
"""

from airtest.core.api import *

auto_setup(__file__)

touch(Template(r"tpl1596506583789.png", record_pos=(-0.37, 1.003), resolution=(1080, 2340)))

touch(Template(r"tpl1596507266663.png", record_pos=(0.314, -0.235), resolution=(1080, 2340)))
sleep(1)
assert_exists(Template(r"tpl1596507278786.png", record_pos=(-0.317, -0.776), resolution=(1080, 2340)), "进入'排行榜'页面成功")
sleep(0.5)
touch(Template(r"tpl1594885416705.png", record_pos=(-0.436, -0.942), resolution=(1080, 2340)))