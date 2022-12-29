n=int(input("enter the number of the student: "))
present,sum,min,max,absent=0,0,100,0,0
marks =[]
for i in range(n):
    temp=input("enter the marks of the student "+str(i+1)+" or AB if absent : ")
    marks.append(temp)
    if temp!="AB":
        present=present+1
        sum=sum+int(temp)
        if int(temp)>max:
            max=int(temp)
        if int(temp)<min:
            min=int(temp)
    else:
        absent=absent+1

avg=sum/present

max_f=0
mark=[]
for i in range(0,101):
    f=0
    for j in marks:
        if j!="AB" and i==int(j):
            f=f+1
    if f>max_f:
        max_f=f
        mark.clear()
        mark.append(i)
    elif f==max_f:
        mark.append(i)




print("1.average score of the class ",avg)
print("2.highest score and lowest score of the class ",max, "and",min)
print("3.count of the student who were absent for the test ",absent)
print("4.display marks with highest frequency ",max_f, "and" ,mark)
