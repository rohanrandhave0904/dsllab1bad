def union(a,b):
    ans = a.copy()
    for i in b:
        if i not in a:
            ans.append(i)
    return ans

def intersection(a,b):
    ans=[]
    for i in a:
        if i in b:
            ans.append(i)
    return ans

def minus(a,b):
    ans=[]
    for i in a:
        if i not in b:
            ans.append(i)
    return ans




u=input("ENTER THE NAMES OF THE SECOND YEAR ENGINEERING STUDENT ").split(",")
c=input("ENTER THE NAMES OF THE STUDENT WHO PLAY CRICKET ").split(",")
b=input("ENTER THE NAMES OF THE STUDENT WHO PLAY BADMINTON ").split(",")
f=input("ENTER THE NAMES OF THE STUDENT WHO PLAY FOOTBALL").split(",")
print("STUDENT WHO PLAY BOTH CRICKET AND BADMINTON BOTH ",union(c,b))
print("student who play either cricket or badminton but not both",minus(union(c,b),intersection(c,b)))
print("number of the student who plaay neither cricket nor badminton ",len(minus(u,union(c,b))))
print("number of the student who play cricket and football but not badminton ",len(intersection(union(c,f),b)))