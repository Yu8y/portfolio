import numpy as np
from numpy import linalg as ln

#Input equations as str here
уравн1 = "x1 + 2x2 + x3 = 8"
уравн2 = "-2x1 + 3x2 - 3x3 = -5"
уравн3 = "3x1 - 4x2 + 5x3 = 10"

'''уравн1 = "0.187x1 + 0.19x2 + 0.36x3 = 0"
уравн2 = "0.19x1 + 0.187x2 + 0.3x3 = 0"
уравн3 = "0.36x1 + 0.3x2 + 0.187x3 = 0"'''

уравн1 = уравн1.replace(' ','')
уравн2 = уравн2.replace(' ','')
уравн3 = уравн3.replace(' ','')

ind1 = уравн1.find("x1")
#print(ind1)
if ind1 == 0:
    a11 = 1
else:
    a11 = уравн1[:ind1]
#print(a11)

знак1 = уравн1[ind1+2:ind1+3]
#print(знак1)

#ind - index
#уравн1 = "x1+2x2+x3=8"
ind2 = уравн1.find("x2")
ind3 = уравн1.find(знак1)
if ind2 == ind3+1:
    a12 = 1
else:
    a12 = уравн1[ind3+1:ind2]
#print(a12)

ОСТ1 = уравн1[ind2+2:]
знак2 = ОСТ1[0:1]
#print(знак2)

ind4 = ОСТ1.find("x3")
if ind4 == 1:
    a13 = "1"
else:
    a13 = ОСТ1[1:ind4]
#print(a13)

ind5 = ОСТ1.find("=")
B1 = ОСТ1[ind5+1:]
#print(B1)

if знак1 == "-":
    a12 = a12*(-1)

if знак2 == "-":
    a13 = a13*(-1)
res = str(a11) + "*x1" + знак1 + a12 + "*x2" + знак2 + str(a13) + "*x3 =" + B1
print(res)

#уравн2 = "-2x1+3x2-3x3=-5"

ind1 = уравн2.find("x1")
#print(ind1)
if ind1 == 0:
    a21 = 1
else:
    a21 = уравн2[:ind1]
#print(a21)

знак21 = уравн2[ind1+2:ind1+3]
#print(знак21)

#ind - index
#уравн1 = "x1+2x2+x3=8"
ind2 = уравн2.find("x2")
ind3 = уравн2.find(знак1)
if ind2 == ind3+1:
    a22 = 1
else:
    a22 = уравн2[ind3+1:ind2]
#print(a22)

ОСТ2 = уравн2[ind2+2:]
знак22 = ОСТ2[0:1]
#print(знак22)

ind4 = ОСТ2.find("x3")
if ind4 == 1:
    a23 = "1"
else:
    a23 = ОСТ2[1:ind4]
#print(a23)

ind5 = ОСТ2.find("=")
B2 = ОСТ2[ind5+1:]
#print(B2)

if знак21 == "-":
    a22 = a22*(-1)

if знак22 == "-":
    a23 = "-"+a23
res2 = str(a21) + "*x1" + знак21 + a22 + "*x2"  + str(a23) + "*x3 =" + B2
print(res2)

#уравн3 = "3x1 - 4x2 + 5x3 = 10"

ind1 = уравн3.find("x1")
#print(ind1)
if ind1 == 0:
    a31 = 1
else:
    a31 = уравн3[:ind1]
#print(a21)

знак31 = уравн3[ind1+2:ind1+3]
#print(знак31)

#ind - index
#уравн1 = "x1+2x2+x3=8"
ind2 = уравн3.find("x2")
ind3 = уравн3.find(знак31)
if ind2 == ind3+1:
    a32 = 1
else:
    a32 = уравн3[ind3+1:ind2]
#print(a22)

ОСТ3 = уравн3[ind2+2:]
знак32 = ОСТ3[0:1]
#print(знак22)

ind4 = ОСТ3.find("x3")
if ind4 == 1:
    a33 = "1"
else:
    a33 = ОСТ3[1:ind4]
#print(a23)

ind5 = ОСТ3.find("=")
B3 = ОСТ3[ind5+1:]
#print(B2)

if знак31 == "-":
    a32 = "-" + a32

if знак32 == "-":
    a33 = a33
res3 = str(a31) + "*x1" + str(a32) + "*x2"  + str(a33) + "*x3 =" + B3
print(res3)

#Matrix creation

eq = np.array([[float(a11),float(a12),float(a13)],[float(a21),float(a22),float(a23)],[float(a31),float(a32),float(a33)]])
print(eq)

det = ln.det(eq)
print(det)

eq1 = np.array([[float(B1),float(a12),float(a13)],[float(B2),float(a22),float(a23)],[float(B3),float(a32),float(a33)]])
print(eq1)

det1 = ln.det(eq1)
print(round(det1,3))

eq2 = np.array([[float(a11),float(B1),float(a13)],[float(a21),float(B2),float(a23)],[float(a31),float(B3),float(a33)]])
print(eq2)

det2 = ln.det(eq2)
print(round(det2,3))

eq3 = np.array([[float(a11),float(a12),float(B1)],[float(a21),float(a22),float(B2)],[float(a31),float(a32),float(B3)]])
print(eq3)

det3 = ln.det(eq3)
print(round(det3,3))

#x solution
if det != 0:
    x1 = det1/det

    x2 = det2/det

    x3 = det3/det

print(x1,x2,x3)