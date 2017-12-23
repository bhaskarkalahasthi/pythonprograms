import calendar
n=input("please enter date in MM DD YYY format")
m=n.split();
day=int(m[1])
month=int(m[0])
year=int(m[2])
result=calendar.weekday(year, month, day)
if(result==0):
    print("MONDAY")
if(result==1):
    print("TUESDAY")
if(result==2):
    print("WEDNESDAY")
if(result==3):
    print("THURSDAY")
if(result==4):
    print("FRIDAY")
if(result==5):
    print("SATURDAY")
if(result==6):
    print("SUNDAY")
