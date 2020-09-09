import os

case_path_dir = str(os.path.abspath(r'.\test_dir'))
report_path_dir = str(os.path.abspath(r'.\test_report'))

files = []
for a, b, c in os.walk(case_path_dir):
    files.append(str(a))

files2 = []
testCase_name = []
for i in files:
    # a = str(i[len(rel_path_dir)+1:len(rel_path_dir)+9:])
    # 前面截取testCase
    a = str(i[-4::])
    s = str(i[len(case_path_dir)+1:-4:])
    # 倒数截取后缀.air
    # print(testCase_name)
    if(s != ''):
        print(r'airtest run "{}" --device Android://127.0.0.1:5037/YLSKL7Z9HET47TJB --log {}\{}'.format(i, report_path_dir, s))

        testCase_name.append(s)
    if(a == ".air"):
        files2.append(i)
    

# creat_testCase_run = ''
# with open(case_path_dir+r'\testCase_run.bat', 'w') as f:
#       airtest run "G:\git\test_dir\testCase_1_add_address.air" --device Android://127.0.0.1:5037/YLSKL7Z9HET47TJB --log G:\git\test_report\testCase_1_add_address
#     # airtest run "G:\git\testCase\1_add_address.air" --device Android://127.0.0.1:5037/YLSKL7Z9HET47TJB --log G:\git\testCase_report\1_add_address
#     # airtest run "{var:i}" --device Android://127.0.0.1:5037/YLSKL7Z9HET47TJB --log {report_path_dir}\1_add_address
#     f.write()

# print(files2)
# print(testCase_name)