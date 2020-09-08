# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)

touch(Template(r"tpl1594866876384.png", record_pos=(0.381, 1.011), resolution=(1080, 2340)))
sleep(0.5)

touch(Template(r"tpl1597135376577.png", record_pos=(0.11, 0.341), resolution=(1080, 2340)))
sleep(1)
assert_exists(Template(r"tpl1597135403988.png", record_pos=(0.007, -0.842), resolution=(1080, 2340)), "进入“收益明细”页面成功")

touch(Template(r"tpl1594885416705.png", record_pos=(-0.436, -0.942), resolution=(1080, 2340)))