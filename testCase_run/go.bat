::关闭回显
@echo off
title 正在创建收货地址
airtest run "G:\git\testCase\1_add_address.air" --device Android://127.0.0.1:5037/YLSKL7Z9HET47TJB --log G:\git\testCase_report\1_add_address
title 正在删除收货地址
airtest run "G:\git\testCase\3_del_address.air" --device Android://127.0.0.1:5037/YLSKL7Z9HET47TJB --log G:\git\testCase_report\3_del_address
::exit