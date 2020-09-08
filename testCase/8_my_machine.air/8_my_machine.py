# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)

touch(Template(r"tpl1594866876384.png", record_pos=(0.381, 1.011), resolution=(1080, 2340)))

touch(Template(r"tpl1597132427371.png", record_pos=(-0.118, -0.074), resolution=(1080, 2340)))
sleep(1)

touch(Template(r"tpl1596506952419.png", record_pos=(-0.007, 0.947), resolution=(1080, 2340)))
sleep(1)
assert_exists(Template(r"tpl1596506990033.png", record_pos=(-0.032, 0.627), resolution=(1080, 2340)), "进入'我的机器'页面成功")
sleep(0.5)

touch(Template(r"tpl1594885416705.png", record_pos=(-0.436, -0.942), resolution=(1080, 2340)))




