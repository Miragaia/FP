def closerToTarget(x,y, target):
    if abs(x-target) < abs(y-target):
        return x
    elif abs(y-target)< abs(x-target):
        return y
    else:
        if x-y < 0:
            return x
        elif y-x < 0:
            return y
        else:
            return x

print(closerToTarget(-31, 33, 1))