# -*- encoding=utf8 -*-
__author__ = "xy"
__title__ = "删除收货地址"
__desc__ = """
用例内容：
1.删除收货地址
2.返回我的主页
"""

from airtest.core.api import *

auto_setup(__file__)

# start test

touch(Template(r"tpl1594884554769.png", record_pos=(0.372, 1.0), resolution=(1080, 2340)))
touch(Template(r"tpl1594884563203.png", record_pos=(-0.355, 0.575), resolution=(1080, 2340)))
sleep(1)

touch((1005,654))
sleep(1)

touch(Template(r"tpl1594885080025.png", record_pos=(-0.344, -0.072), resolution=(1080, 2340)))
sleep(1)

touch(Template(r"tpl1596504852596.png", record_pos=(0.021, 0.171), resolution=(1080, 2340)))
sleep(1)

assert_exists(Template(r"tpl1594885184051.png", record_pos=(0.006, 0.943), resolution=(1080, 2340)), "删除地址成功")

touch(Template(r"tpl1594885416705.png", record_pos=(-0.436, -0.942), resolution=(1080, 2340)))




