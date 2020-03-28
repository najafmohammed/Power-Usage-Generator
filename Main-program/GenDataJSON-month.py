import json 
from numpy.random import seed
from numpy.random import randint
import numpy as np
import os.path
class GetValues: 
    def __init__(Values): 
        Values.username = input("Enter username:")
        Values.month = input("Enter Month:")
        Values.year = input("Enter Year:")
        Values.interval=input("Interval for values(1 to 60):")

def retrivedValues():
    return GetValues()

def getMvalue(month,leapYear):
    mValue=0
    if(int(month)==2):
        if(leapYear==True):
            mValue=29
        if(leapYear==False):
            mValue=28
    elif (int(month)%2==0):
        mValue=30
    else:
        mValue=31
    return mValue
        

def generatefile(username,month,year,interval):
    dictionary ={
        "username": username,
        "month":month,
        "year":year,
        "values": [
        ]
    }
    leapYear=False
    if (int(year) % 4) == 0:
        if(int(year) % 100) == 0:
            if(int(year) % 400) == 0:
                leapYear=True
            else:
                leapYear=False
        else:
            leapYear=True
    else:
        leapYear=False
    flagDef=input("Use default directory (y/n)")
    flagSerial=input("Serialise JSON file?(y/n)")
    for i in range(getMvalue(month,leapYear)):
        vLim=1440/int(interval)
        powerMultiplier=10*int(interval)
        add={"day":[1,2,3,4,5,6,7,8,9],"dayTotal":72}
        values1 = randint(0, int(powerMultiplier), int(vLim))
        total=np.sum(values1)
        add['day']=values1.tolist()
        add['dayTotal']=total.item()
        dictionary['values'].append(add)
    if(flagSerial=="y"):
        json_object = json.dumps(dictionary, indent = 4)
        subdir="Serialised"
    else:
        json_object = json.dumps(dictionary)
        subdir="UnSerialised"  
    if(flagDef=="n"):
        name_of_file = input("What is the name of the file:")
        save_path = input("Enter name of Directory:")
    else:
        name_of_file = str(username+"-"+month+year)
        save_path = 'Generated Files'+"["+str(subdir)+"]"
    completeName = os.path.join(save_path, name_of_file+".json") 
    if not os.path.isdir(save_path):
        os.mkdir(save_path)
    file = open(completeName, "w")
    file.write(json_object)
    file.close()
        
val=retrivedValues()

generatefile(val.username,val.month,val.year,val.interval)
