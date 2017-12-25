
student_list={'raja':120,'ravi':121,'siva':122,'bhargav':123,'pavan':124,'eswar':125,'akhil':126,'mani':127,'suresh':130,'bhaskar':131,'chaitu':132,'alok':133}
system_details={'mcalab':{'1':['free','good'],'2':['free','good'],'3':['free','repair'],'4':['allocate','good'],'5':['free','repair'],'6':['free','good'],'7':['free','good'],'8':['allocate','good'],'9':['free','good'],'10':['free','repair']},'ciscolab':{'1':['free','good'],'2':['free','good'],'3':['free','good'],'4':['free','repair'],'5':['free','repair'],'6':['free','good'],'7':['free','good'],'8':['allocate','good'],'9':['allocate','good'],'10':['free','repair']}}
student_rollno_list=list(student_list.values())
student_name_list=list(student_list.keys())
a=list(system_details.keys())
print(a)
b=list(system_details[a[0]])
print(b)
system_number_and_labname=[]
for i in range(len(a)):
    for j in range(len(b)):
        if(system_details[a[i]][b[j]][0]=="free" and system_details[a[i]][b[j]][1]=="good"):
            
            system_number_and_labname.append([a[i],b[j]])
x=0
for i in range(len(student_rollno_list)):
    if(x<len(system_number_and_labname)):
        print(student_name_list[i],"-",student_rollno_list[i],"-", system_number_and_labname[i][0],"-",system_number_and_labname[i][1])
        x=x+1
    else:
        print(student_name_list[i],"-",student_rollno_list[i],"-system not allocated because system not free")
        
   
