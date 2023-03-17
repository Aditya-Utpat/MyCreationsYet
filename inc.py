b = open('C:\\Users\\aditya\\Desktop\\assignmnts\\week.txt').read()
print(b)
a = open('C:\\Users\\aditya\\Desktop\\assignmnts\\week.txt','w')
if b == 'ab':
    a.write('cd')
elif b == 'cd':
    a.write('ab')
a.close()
