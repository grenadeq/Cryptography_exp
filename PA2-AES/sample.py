#coding = utf8
from oracle import *
import sys
"""
if len(sys.argv) < 2:
    print "Usage: python sample.py <filename>"
    sys.exit(-1)
"""
data = "9F0B13944841A832B2421B9EAF6D9836813EC9D944A5C8347A7CA69AA34D8DC0DF70E343C4000A2AE35874CE75E64C31"
ctext = [(int(data[i:i+2],16)) for i in range(0, len(data), 2)]
iv_true = ctext[0:16]
iv_p = [0]*16
data1 = ctext[16:32]
data1_middle = []
data2_middle = []
data2 = ctext[32:48]

Oracle_Connect()

for x in range(16)[::-1]:
	for y in range(256):
		iv_p[x] = y
		data_p = iv_p + data2
		rc = Oracle_Send(data_p,2)
		if rc == 1:
			print y
			print len(data1_middle) + 1
			m = y ^ (len(data1_middle)+1)
			data1_middle.insert(0,m)
			break;
	iv_p[x:] = [a ^ (len(data1_middle)+1) for a in data1_middle]
	print data1_middle
	print iv_p
	print "\n\n"


Oracle_Disconnect()
print data1_middle
print iv_p

a = [data1_middle[i] ^ iv_true[i] for i in range(len(iv_true))]
a = [chr(i) for i in a]
ptext = ''.join(a)
print ptext

