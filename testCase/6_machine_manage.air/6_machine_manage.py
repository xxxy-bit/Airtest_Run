# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)

touch(Template(r"tpl1596506583789.png", record_pos=(-0.37, 1.003), resolution=(1080, 2340)))

touch(Template(r"tpl1596506912885.png", record_pos=(0.097, -0.239), resolution=(1080, 2340)))
sleep(1)

touch(Template(r"tpl1596506952419.png", record_pos=(-0.007, 0.947), resolution=(1080, 2340)))
sleep(1)
assert_exists(Template(r"tpl1596506990033.png", record_pos=(-0.032, 0.627), resolution=(1080, 2340)), "进入'机器申请'页面成功")
sleep(0.5)

touch(Template(r"tpl1594885416705.png", record_pos=(-0.436, -0.942), resolution=(1080, 2340)))




