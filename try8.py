####s='ppets'
##lst=[]
##for i in s:
##    lst+=i
##print(lst)

##lst=[]
##for i in range(5):
##    print("Enter:", i+1)
##    n=int(input())
##    lst.append(n)
##print(lst)

##str_x=input('Enter:')
##s=str_x.split(',')
##lst=[]
##for i in s:
##    lst+=i
##print(lst)

##st=input("enter a term")
##st=st.upper()
##st=st.split()
##for i in st:
##    print(i[0], end='')
##    

#DICTIONARY

i=1
s={}
while True:
    print('Enter Data student:',i)
    roll=int(input('Roll:'))
    name=input('name:')
    s.update({roll:name})
    if i==3:
        break
    i+=1
print(s)















          
