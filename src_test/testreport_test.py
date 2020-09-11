'''
生成用例报告文件代码编写测试
'''

import os

# 用例文件夹
case_path_dir = str(os.path.abspath(r'.\test_dir'))
# 报告文件夹
report_path_dir = str(os.path.abspath(r'.\test_report'))

# 遍历获取用例文件夹
files = []
for a, b, c in os.walk(case_path_dir):
    files.append(str(a))

repo_text = []
for i in files:
    # 生成报告文件夹名称
    report_name = str(i[len(case_path_dir)+1:-4:])
    if(report_name != ''):
        repo_text.append(str(r'airtest report "{}" --log_root {}\{} --outfile {}\{}\log.html --lang zh'.format(i, report_path_dir, report_name, report_path_dir, report_name)))
# 生成用例运行文件
with open(case_path_dir+r'\testRepo.bat', 'w', encoding='utf-8') as f:
    for i in repo_text:
        f.write(i + '\n')
        