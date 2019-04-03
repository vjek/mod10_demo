#!/usr/bin/env python3
# script to demonstrate mod10 Message + Key = Ciphertext and reverse
# shows it horizontally and vertically, uses terminal columns and lines
# to limit output to reasonable amounts.
###
import random,os
def get_next_rand(rand_inst):
    return rand_inst.randint(0,9)

def mod10(num): #this function will discard the tens place of a given two digit number
    num %= 10
    return num

if os.name != "posix": #this will check if this is a posix compatible environment
    print("This was meant to run under a posix OS, so it probably won't look right for you")
    os._exit(1)

ts = os.get_terminal_size()
s_len = ts.columns - 2
#s_len=20
yl1='\033[33m' #yellow
mg1='\033[35m' #magenta
cy1='\033[36m' #cyan
wh1='\033[37m' #white
seed1=8675 #this should not be done, normally, but it's procedural/deterministic
seed2=309 #you can change these seeds to whatever you want

rand1=random.Random()
rand1.seed(seed1)
rand2=random.Random()
rand2.seed(seed2)

mess1=''
print(yl1+'M|',end='') #yellow
for a in range(0,s_len):
    mess1 += str(rand1.randint(0,9)) #take each val and add to message string
print(mess1)

key1=''
print(mg1+'K+',end='') #magenta
for a in range(0,s_len):
    key1 += str(rand2.randint(0,9)) #take each val and add to the key string
print(key1)

ciph1=''
print(cy1+'C|',end='') #cyan
for a in range(0,s_len):
    m1=int(mess1[a])
    k1=int(key1[a])
    ciph1 += str(mod10(m1+k1)) #take M+K to add to cipher string
print(ciph1)
# now print the K & M again to show subtraction
print(mg1+'K-',end='') #magenta
print(key1)
print(yl1+'M|',end='') #yellow
print(mess1)

##
# vertical representation below
##
rand1.seed(seed1) #reset/re-seed each rand instance
rand2.seed(seed2)
print(str.format("{}M {}+ {}K {}= {}C {}- {}K {}= {}M",yl1,wh1,mg1,wh1,cy1,wh1,mg1,wh1,yl1))
print(wh1+"-   -   -   -   -")
for w in range(0,ts.lines-10):
    a = get_next_rand(rand1)    #Message
    b = get_next_rand(rand2)    #Key
    result1=mod10(a + b)        #makes cipher
    result2=mod10(result1 - b)  #uses key to recover message from cipher
    print(str.format("{}{} {}+ {}{} {}= {}{} {}- {}{} {}= {}{}",\
            yl1,a,wh1,mg1,b,wh1,cy1,result1,wh1,mg1,b,wh1,yl1,result2)) #prints it all out
