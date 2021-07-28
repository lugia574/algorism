import math

def geometry(R):
    pie = math.pi
    euclid = round(R**2 * pie,6)
    taxi = 2*R*R

    return euclid,taxi

R = int(input())

euclid, taxi = geometry(R)
print(euclid)
print(format(taxi,'.6f'))
