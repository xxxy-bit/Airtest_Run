# -*- encoding=utf8 -*-
__author__ = "xy"
__title__ = "新增收货地址"
__desc__ = """
用例内容：
1.新增收货地址
2.填写地址信息
3.保存
"""

from airtest.core.api import *

auto_setup(__file__)

# start test

touch(Template(r"tpl1594866876384.png", record_pos=(0.381, 1.011), resolution=(1080, 2340)))
sleep(0.5)

touch(Template(r"tpl1596506241383.png", record_pos=(-0.358, 0.582), resolution=(1080, 2340)))
sleep(0.5)

touch(Template(r"tpl1594866669489.png", record_pos=(0.014, 0.943), resolution=(1080, 2340)))
sleep(0.5)

touch(Template(r"tpl1594866680799.png", record_pos=(-0.04, -0.811), resolution=(1080, 2340)))
sleep(0.5)
text("张三")

touch(Template(r"tpl1594866689579.png", record_pos=(-0.025, -0.686), resolution=(1080, 2340)))
sleep(0.5)
text("18832132132")

touch(Template(r"tpl1594866707544.png", record_pos=(-0.309, -0.473), resolution=(1080, 2340)))

touch(Template(r"tpl1594866760901.png", record_pos=(-0.259, -0.69), resolution=(1080, 2340)))

sleep(1)

touch(Template(r"tpl1594866957392.png", record_pos=(-0.045, -0.469), resolution=(1080, 2340)))

touch(Template(r"tpl1594866773684.png", record_pos=(-0.235, 0.119), resolution=(1080, 2340)))

sleep(1)

touch(Template(r"tpl1594866986319.png", record_pos=(0.263, -0.471), resolution=(1080, 2340)))

touch(Template(r"tpl1594866793615.png", record_pos=(-0.278, -0.139), resolution=(1080, 2340)))

sleep(1)
touch(Template(r"tpl1594866802156.png", record_pos=(0.006, -0.33), resolution=(1080, 2340)))
text("北京收货地址",enter=False)
sleep(0.5)

touch(Template(r"tpl1594885520110.png", record_pos=(0.177, -0.194), resolution=(1080, 2340)))
sleep(1.0)

touch(Template(r"tpl1594885369743.png", record_pos=(-0.346, 0.13), resolution=(1080, 2340)))

touch(Template(r"tpl1594866854072.png", record_pos=(0.003, 0.943), resolution=(1080, 2340)))
sleep(0.5)

assert_exists(Template(r"tpl1594884490100.png", record_pos=(-0.075, -0.09), resolution=(1080, 2340)), "添加地址成功")

touch(Template(r"tpl1594884386990.png", record_pos=(-0.431, -0.94), resolution=(1080, 2340)))





