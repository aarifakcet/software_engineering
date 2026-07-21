'''for i in range(5,-10,-2):
    print(i,end=" ")
print()'''
'''
*****
****
***
**
*
'''

n=5
for i in range(n):
    for j in range(n-i,0,-1):
        print("*",end=" ")
    print()