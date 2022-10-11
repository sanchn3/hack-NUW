# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 00:24:39 2022
@author: sanch
Title: Spanish number validation
"""
def check_pars(val):
    p=0
    chars = ["(",")","+"]
    val1=val.replace(" ","")
    if chars[2] in val1:
        if val[0]!=chars[2]: return False            
    val1 = list(val1)
    if chars[0] in val1 and chars[1] not in val1 or chars[1] in val1 and chars[0] not in val1: return False
    elif chars[0] in val1 and chars[1] in val1: pass
    elif val1.count("-")>1:#check -s(dashes)
        for i in range(-1,-len(val1),-1):
            if val1[i]=="-":
                if p==i:
                    return False
                    p=val[i]
                if i%3!=0 and i%4!=0: return False            
        val2=val.replace("-","").replace("+","")
        if val2[0:2]=="34": val2=val2.replace("34","")
        try:           
            if val2.index(chars[0])==1 and val2.index(chars[1])==5: 
                val2 = list(val2)
                val2.remove("(")
                val2.remove(")")
                if (chars[0] or chars[1]) in val2: return False
        except:
            pass
                
def checkNumber(val):
    if check_pars(val)==False: return False
    val=val.replace(" ","")
    if val[0].isdigit()==True or val[0] == "+" or val[0] == "(": pass
    else:return False
    for i in list(val):
        if i == '-' or i == "(" or i == ")" or i =="+": continue
        elif i.isdigit()==True: continue
        else:return False
    val=val.replace("-","").replace("(","").replace(")","").replace("+","")
    if len(val) == 9 or (len(val) == 11 and val[0:2]=="34"): return True
    else: return False
    
while __name__ == "__main__":
    x=str(input("Enter Test Value:\n"))
    #x = "972-35-56-57"
    if x == "quit":break

    print(checkNumber(x))
    






