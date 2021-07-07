import math
def fx(x):
    return math.e**(x**2-x)
pi = math.pi
e = math.e
x = 0
a=2
b=0
ls = []
das=[]
for i in range(11):
    da = a + (b-a) / 10 * i
    das.append("{:10.4}".format(da))
    ls.append(fx(da))
an = (b-a)/30 * (ls[0]+ls[10]+4*(ls[1]+ls[3]+ls[5]+ls[7]+ls[9])+2*(ls[2]+ls[4]+ls[6]+ls[8]))
for j in range(11):
    print("[{:2}]    {:}    {:10.4}".format(j, das[j], ls[j]))
print(an)
