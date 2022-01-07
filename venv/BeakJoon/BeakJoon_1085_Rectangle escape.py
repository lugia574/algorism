def Rectangle (x, y, w, h):
    distance =min(x, y, h-y, w-x)

    return distance


x, y, w, h = map(int,input().split())
distance = Rectangle(x, y, w, h)
print(distance)