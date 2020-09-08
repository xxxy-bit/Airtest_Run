::关闭回显
@echo off
G:
cd tester\Airtest_test
title 正在创建收货地址
airtest run "G:\tester\Airtest_test\1_add_address.air" --device Android://127.0.0.1:5037/YLSKL7Z9HET47TJB --log G:\tester\Aittest_report\1_add_address
title 正在删除收货地址
airtest run "G:\tester\Airtest_test\3_del_address.air" --device Android://127.0.0.1:5037/YLSKL7Z9HET47TJB --log G:\tester\Aittest_report\3_del_address
::exit