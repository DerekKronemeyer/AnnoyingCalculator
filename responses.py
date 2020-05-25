import random
import math

def getResponse(result):
    method = random.randint(0,5)
    #method = 5
    if method == 0:
        result = function0(result)
    if method == 1:
        result = function1(result)
    if method == 2:
        result = function2(result)
    if method == 3:
        result = function3(result)
    if method == 4:
        result = function4(result)
    if method == 5:
        result = function5(result)
    return result 

def function0(result):
    return "between " + str(int(result)-1) + " and " + str(int(result)+1)

def function1(result):
    return str(float(result)/math.pi) + "π"

def function2(result):
    return str(math.sqrt(float(result))) + "^2"

def function3(result):
    return str(bin(int(result)))[2:] + " is the answer in binary"

def function4(result):
    if(float(result)>0):
        return "the answer is positive"
    elif(float(result)<0):
        return "the answer is negative"
    else:
        return "you get NOTHING! YOU LOSE! GOOD DAY SIR!"

def function5(result):
    sub = random.uniform(0,float(result))
    return str(sub) + " + " + str(float(result)-sub)