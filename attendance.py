import csv
file = open(input('Enter the present sheet:').replace('"',''))
csvobj = csv.reader((line.replace('\0', '') for line in file),delimiter='\t')
cap = False
attendance = [ 'Aarav Anil Kumar',
 'Aaryan ManojKumar Pawar', 'Abhineet Waghmare', 'Adeetya Nitin Agarwal', 'Aditya Ajay Utpat', 'Aniruddha Shreekumar Nair', 'Arnav Sonawane', 'ATHARV KIDE', 'BHAVIKA BHOSALE', 'Chaitanya Joshi', 'Dev Palak Patel', 'KAREENA Prakash SOLANKI', 'Kartik Salwe', 'Kartiki Watkar', 'Kavya Rajendra Zanzane', 'Kinjal Mahesh Sutar', 'Manas Chintawar', 'Nathen Robert Gaikwad', 'Niti Sameer Turakhia', 'Om Sharma', 'Prachit Rohit Bhalgat', 'Pranaya Amol Malokar', 'Prisha Dhruv Modi', 'Rehan Jagdish Tahalyani', 'RONAK JOSHI', 'Samruddhi Amit Agarwal','Sanskruti Patil', 'Shreya Pankaj Patil', 'Siddhant Sharma', 'Siddhi Amit Agarwal', 'Siddhi Yogesh Wake', 'Snehal Chandrakant Shinde', 'Swapnil Anand Tulaskar', 'Vedanshi Pradip Thakur', 'Yashashree Patil', 'Angela Solomon Guttal', 'Adwita Tripathi']
present = []
absent = []
for row in csvobj:
    if len(row) == 0:
        continue
    if row[0] == 'Full Name':
        cap = True
        continue
    if row[0] == 'Meeting Start Time':
        date = row[1].split(',')[0]
    if cap == True:
        present.append(row[0])
present = list(set(present))
date= date.replace('/',',')
for i in attendance:
    if i not in present:
        absent.append(i)
out = open('attendance_'+date+'.csv','w')
out.write('Present\n')
for i in present:
    out.write(i+'\n')
out.write('\n\nAbsent\n')
for i in absent:
    out.write(i+'\n')
out.close()
print('File created')
input('Press enter to exit')
