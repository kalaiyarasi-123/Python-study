#Boolean OR Operator

a = 5
b = 3
c = 8

if a > b or b < c:
    print("True")

#Boolean And Operator    

a = 0
b = 2
c = 4

if a > b and b<c:
    print("if satifaction of both condtion only return",True)
else:
    print("if not satifaction of both condtion return",False)

#Boolean Not Operator    
#Boolean Not operator only requires one argument 

a = 0

if not a:
    print("False")

#Python Boolean == (equivalent) and != (not equivalent) Operator 

a = 0
b = 1

if a == 0:
    print(True)
    
if a == b:
    print(True)
    
if a != b:
    print(True)   
 