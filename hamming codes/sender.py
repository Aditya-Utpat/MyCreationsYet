file = input('Enter file:')
file = open(file,'r')
f= file.read()
msglen= len(f)
msg = [bin(ord(x)).replace('0b','') for x in f]
print(msg)
for i in range(msglen):
    z = 8-len(msg[i])
    msg[i]=('0'*z)+msg[i]
i =1
n = (2**i)-i -1
while n< (msglen*8):
    x = n
    i =i+1
    n = (2**i)-i -1
