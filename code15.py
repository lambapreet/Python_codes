'''
r = 8
for i in range(1,r+1):
    # print("*"*i, end=" ")
    # print("*" * i)
    print(r*i)

f = 5
for i in range(1,f+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    
'''

def diamond(n):
    for i in range(n):
        print(" "*(n-i-1),end=" ")
        print("*"*(2*i+1))
        
    for i in range(n-2,-1,-1):
        print(" "*(n-i-1),end=' ')
        print('*'*(2*i+1))
        
n = diamond(5)
# print(diamond(n))