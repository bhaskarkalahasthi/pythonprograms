#!/bin/python3

import sys

def solve(year):
    # Complete this function
    date=[]
    sum=0
    year_months=[31,28,31,30,31,30,31,31,30,31,30,31]
    for i in range(8):
        if(year>=1700 and year<=1917):
            if((year%4==0 or year%400==0)):
                
                year_months[1]=29
                sum=sum+year_months[i]
            else:
              
                sum=sum+year_months[i]

        
       
        if(year==1918):
            
            year_months[1]=15
            sum=sum+year_months[i]
        if(year>1918):
            if(year%400==0 or (year%4==0 and year%100!=0)):
                year_months[1]=29
                sum=sum+year_months[i]
            else:
                sum=sum+year_months[i]
    #1918
    #26.09.1918
    #2100
    #13.09.2100
    #print(sum)
    res=256-sum
    date.append(str(res))
    date.append('09')
    date.append(str(year))
    result=".".join(date)
    return result

year = int(input().strip())
result = solve(year)
print(result)
