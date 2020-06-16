#!/usr/bin/python3
import os, time

Time_gap = 55
CMD_Ph1  = "raspistill -o "
CMD_Ph2  = " -w 2560 -h 1440 -v -vf"

def TakePhoto(Name):
    CMD = CMD_Ph1 + Name + CMD_Ph2
    os.system(CMD)

def Kill(PID):
    os.system("kill "+PID)

def Stream():
    CMD_run  = "bash Blive &  pid=$!; echo PID=$pid| grep PID="
    STR = os.popen(CMD_run).read()
    PID = STR.replace('PID=','').replace('\n','')
    print(PID)
    return PID

Time = time.time()

PID = Stream()
while True:
    time.sleep(1)
    if time.time() - Time > Time_gap:
        Kill(PID)
        time.sleep(4)
        TakePhoto("Pictures/" + time.ctime().replace(' ',"_") + ".jpg")
        os.system("echo Photo "+ str(time.ctime())+ " >> log.python_belive")
        PID = Stream()
        Time = time.time()



while [ 1 -eq 1 ]
do bash Blive &  PID=$!
echo $PID
sleep 50
kill $PID
Name=$(date "+%Y_%m_%d_%H_%M_%S")
raspistill -o Pictures/$Name.jpe -w 2560 -h 1440 -v -vf
echo Photo $Name >> log.python_belive
done
