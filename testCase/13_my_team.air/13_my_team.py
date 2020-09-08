# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)

touch(Template(r"tpl1594866876384.png", record_pos=(0.381, 1.011), resolution=(1080, 2340)))
sleep(0.5)
touch(Template(r"tpl1597130340286.png", record_pos=(-0.124, 0.35), resolution=(1080, 2340)))
sleep(0.5)
assert_exists(Template(r"tpl1597130361036.png", record_pos=(0.0, -0.602), resolution=(1080, 2340)), "进入“我的团队”页面成功")
touch(Template(r"tpl1594885416705.png", record_pos=(-0.436, -0.942), resolution=(1080, 2340)))


