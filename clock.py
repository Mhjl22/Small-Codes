import time
import math
hours = input("set hours: ")
minutes = input("set minutes: ")
seconds = input("set seconds: ")
nh = int(hours)
nm = int(minutes)
ns = int(seconds)
def ns0():
    global sdigits
    if ns > 0:
        sdigits = int(math.log10(ns))+1
    elif ns == 0:
        sdigits = 1
def nm0():
    global mdigits
    if nm > 0:
        mdigits = int(math.log10(nm))+1
    elif nm == 0:
        mdigits = 1
def nh0():
    global hdigits
    if nh > 0:
        hdigits = int(math.log10(nh))+1
    elif nh == 0:
        hdigits = 1
while True:
    ns0()
    nm0()
    nh0()
    if hdigits == 1 and mdigits == 1 and sdigits == 1:
        print("0" + str(nh) + ":0" + str(nm) + ":0" + str(ns))       
    elif hdigits > 1 and mdigits > 1 and sdigits > 1:
        print(str(nh) + ":" + str(nm) + ":" + str(ns))       
    elif hdigits == 1 and mdigits == 1 and sdigits > 1:
        print("0" + str(nh) + ":0" + str(nm) + ":" + str(ns))       
    elif hdigits == 1 and mdigits > 1 and sdigits > 1:
        print("0" + str(nh) + ":" + str(nm) + ":" + str(ns))        
    elif hdigits > 1 and mdigits == 1 and sdigits == 1:
        print(str(nh) + ":0" + str(nm) + ":0" + str(ns))        
    elif hdigits > 1 and mdigits == 1 and sdigits > 1:
        print(str(nh) + ":0" + str(nm) + ":" + str(ns))        
    elif hdigits > 1 and mdigits > 1 and sdigits == 1:
        print(str(nh) + ":" + str(nm) + ":0" + str(ns))        
    elif hdigits == 1 and mdigits > 1 and sdigits == 1:
        print("0" + str(nh) + ":" + str(nm) + ":0" + str(ns))
    ns = ns + 1
    time.sleep(1)
    if ns == 60:
        nm = nm + 1
        ns = 0
    if nm == 60:
        nh = nh + 1
        nm = 0
    if nh == 24:
        nh = 0

