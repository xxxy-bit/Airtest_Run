import os, time

report_path_dir = os.path.abspath(r'.\testCase_report')

a1=[]
b1=[]
c1=[]

for dir_path, dir_name, files in os.walk(report_path_dir): 
    a1.append(dir_path)
    b1.append(dir_name)
    c1.append(files)

print(a1)
print('--------------------')
print(b1)
print('--------------------')
print(c1)

temp = []
for i in range(1,len(a1)):
    # temp.append(a1[i]+r'\log.html')
    os.startfile(a1[i]+r'\log.html')
    time.sleep(2)