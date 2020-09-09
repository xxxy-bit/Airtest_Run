import os

rel_path_dir = str(os.path.abspath(r'.\test_dir'))

files = []
for a, b, c in os.walk(rel_path_dir):
    files.append(str(a))

files2 = []
for i in files:
    # a = str(i[len(rel_path_dir)+1:len(rel_path_dir)+9:])
    # 前面截取testCase
    a = str(i[-4::])
    # 倒数截取后缀.air
    if(a == ".air"):
        files2.append(i)

print(files2)