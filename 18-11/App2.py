marks1=130
marks2=40
marks3=60
marks4=50
print(marks1 < marks2 and marks1<marks3 and marks1<marks4)
'''
logical operators
=================
and
C1          C2           C3          result
F           F            F            False
T           F            F            F
t           r            F            f
t           t            t            t
or
not

'''

'''
<=
>=
!=
<
>
==

in 
not in
is
is not
'''

Max_Marks=None;
marks1=int(input("Enter the ma"))
marks2=int(input("Enter the ma"))
marks3=int(input("Enter the ma"))
marks4=int(input("Enter the ma"))

if(marks3 > marks2 and marks3 > marks1 and marks3 > marks4):
    Max_Marks="Marks 3 is Max"
elif(marks1 > marks2 and marks1 > marks4):
     Max_Marks="Marks 1 is Max"
elif(marks2>marks4):
    Max_Marks="Marks 2  is Max"
else:
    Max_Marks="Marks 4 is Max"
print(Max_Marks)