import re
File = open('regex_sum_1079222.txt')
flag = 0
for line in File:
    lst = re.findall('[0-9]+',line)
    for i in lst:
        flag = flag + int(i)
print(flag)
