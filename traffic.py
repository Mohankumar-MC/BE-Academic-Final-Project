from signal import pause
import RPi.GPIO as GPIO
import time
from threading import Timer
import datetime
from firebase import firebase


GPIO.setmode(GPIO.BCM)

IR_PIN=2
IR_PIN2=3
IR_PIN3=14
IR_PIN4=4

GPIO.setup(IR_PIN,GPIO.IN)
GPIO.setup(IR_PIN2,GPIO.IN)
GPIO.setup(IR_PIN3,GPIO.IN)
GPIO.setup(IR_PIN4,GPIO.IN)

count1=0
count2=0
count3=0
count4=0
sub1=0
sub2=0
sub3=0
sub4=0

while 1:
    something=GPIO.input(IR_PIN)
    something1=GPIO.input(IR_PIN2)
    something2=GPIO.input(IR_PIN3)
    something3=GPIO.input(IR_PIN4)
    
    if not something:
        sub1+=1
        print("signal 1 detected".format(sub1))
        #print("signal format1"+str(sub1))
        start_time=datetime.datetime.now().time().strftime('%H:%M:%S')
        time.sleep(3)
        end_time=datetime.datetime.now().time().strftime('%H:%M:%S')
        tital_time=(datetime.datetime.strptime(end_time,'%H:%M:%S')-datetime.datetime.strptime(start_time,'%H:%M:%S'))
       # print(sub1)
        if(tital_time):
            if sub1<2:
                print('loose')
                traffic='loose'
                fb=firebase.FirebaseApplication('https://m1signal.firebaseio.com/',None)
                result=fb.put('signal1','density',traffic)
                # sub1=0
            if sub1>2 and sub1<5:
                print('moderate')
                traffic='moderate'
                fb=firebase.FirebaseApplication('https://m1signal.firebaseio.com/',None)
                result=fb.put('signal1','density',traffic)
                # sub1=0
            if sub1>5:
                print('Conjested')
                traffic='conjested'
                fb=firebase.FirebaseApplication('https://m1signal.firebaseio.com/',None)
                result=fb.put('signal1','density',traffic)
                sub1=0

    if not something1:
        sub2+=1
        start_time=datetime.datetime.now().time().strftime('%H:%M:%S')
        time.sleep(3)
        end_time=datetime.datetime.now().time().strftime('%H:%M:%S')
        tital_time=(datetime.datetime.strptime(end_time,'%H:%M:%S')-datetime.datetime.strptime(start_time,'%H:%M:%S'))
        print("Signal 2 Detected")
       # print("signal format1"+str(sub2))
        if(tital_time):
            if sub2<2:
                print('loose')
                traffic='loose'
                fb=firebase.FirebaseApplication('https://m1signal.firebaseio.com/',None)
                result=fb.put('signal2','density',traffic)
                # sub2=0
            if sub2>2 and sub2<5:
                traffic='moderate'
                fb=firebase.FirebaseApplication('https://m1signal.firebaseio.com/',None)
                result=fb.put('signal2','density',traffic)
                print('moderate')
                # sub2=0
            if sub2>5:
                traffic='conjested'
                fb=firebase.FirebaseApplication('https://m1signal.firebaseio.com/',None)
                result=fb.put('signal2','density',traffic)
                print('conjested')
                sub2=0
            
    if not something2:
        sub3+=1
        print("Signal 4 Detected")
        # print("signal format3 "+str(sub3))
        start_time=datetime.datetime.now().time().strftime('%H:%M:%S')
        time.sleep(3)
        end_time=datetime.datetime.now().time().strftime('%H:%M:%S')
        tital_time=(datetime.datetime.strptime(end_time,'%H:%M:%S')-datetime.datetime.strptime(start_time,'%H:%M:%S'))
        if(tital_time):
            if sub3<2:
                print('loose')
                traffic='loose'
                fb=firebase.FirebaseApplication('https://m1signal.firebaseio.com/',None)
                result=fb.put('signal4','density',traffic)
                # sub3=0
            if sub3>2 and sub2<5:
                print('moderate')
                traffic='moderate'
                fb=firebase.FirebaseApplication('https://m1signal.firebaseio.com/',None)
                result=fb.put('signal4','density',traffic)
                # sub3=0
            if sub3>5:
                print('Conjested')
                traffic='conjested'
                fb=firebase.FirebaseApplication('https://m1signal.firebaseio.com/',None)
                result=fb.put('signal4','density',traffic)
                sub3=0
    if not something3:
        sub4+=1
        print("Signal 3 Detected")
        start_time=datetime.datetime.now().time().strftime('%H:%M:%S')
        time.sleep(3)
        end_time=datetime.datetime.now().time().strftime('%H:%M:%S')
        tital_time=(datetime.datetime.strptime(end_time,'%H:%M:%S')-datetime.datetime.strptime(start_time,'%H:%M:%S'))
        # print("Signal 2 Detected")
        if(tital_time):
            if sub4<2:
                print('loose')
                traffic='loose'
                fb=firebase.FirebaseApplication('https://m1signal.firebaseio.com/',None)
                result=fb.put('signal3','density',traffic)
                # sub4=0
            if sub4>2 and sub2<5:
                print('moderate')
                traffic='moderate'
                fb=firebase.FirebaseApplication('https://m1signal.firebaseio.com/',None)
                result=fb.put('signal3','density',traffic)
                # sub4=0
            if sub4>5:
                print('conjested')
                traffic='conjested'
                fb=firebase.FirebaseApplication('https://m1signal.firebaseio.com/',None)
                result=fb.put('signal3','density',traffic)
                sub4=0
