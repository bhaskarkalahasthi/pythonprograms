import sys
def timeConversion(s):
    # Complete this function
    b=s.split(":")
    li=[]
    for i in range(len(b)):
        
        if(i==0):
            res=b[2]
            HH=b[0]
            if "PM" in res:
                if(int(b[i])<12):
                    value=int(b[i])+12
                    li.append(str(value))
            if "AM" in res:
                if(int(b[1])==12):
                    
                    b[2]="00"
                else:
                    li.append(b[i])
                    
        else:
            li.append(b[i])
    abc=":".join(li).strip("PM")
    return abc

s = input().strip()
result = timeConversion(s)
print(result)
