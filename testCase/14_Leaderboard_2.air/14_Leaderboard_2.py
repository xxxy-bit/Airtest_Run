# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)

touch(Template(r"tpl1596506583789.png", record_pos=(-0.37, 1.003), resolution=(1080, 2340)))
swipe(Template(r"tpl1597129963078.png", record_pos=(-0.236, 0.656), resolution=(1080, 2340)), vector=[0.0191, -0.4696])
sleep(0.5)
touch(Template(r"tpl1597130035670.png", record_pos=(-0.008, 0.012), resolution=(1080, 2340)))
sleep(0.5)
assert_exists(Template(r"tpl1597130054899.png", record_pos=(-0.306, -0.773), resolution=(1080, 2340)), "进入“推咖排行榜”页面成功")

touch(Template(r"tpl1594885416705.png", record_pos=(-0.436, -0.942), resolution=(1080, 2340)))

