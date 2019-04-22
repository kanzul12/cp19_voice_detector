s1=input("enter first string: ")
s2=input("enter second string: ")
a=list(set(s1)and set(s2))
print("The common words are: ")
for i in a:
    print(i)