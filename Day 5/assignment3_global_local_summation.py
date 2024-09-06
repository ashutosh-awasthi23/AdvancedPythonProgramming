sumi_global = 0


def summation(li_):
    global sumi_global
    sumi = sum(li_)
    sumi_global = sumi


def resetter():
    global sumi_global
    sumi_global = 0


li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"The value of global variable before function call is: {sumi_global}")
summation(li)
print(f"The value of global variable after function call is: {sumi_global}")
resetter()
print(f"The value of global variable after resetting  is: {sumi_global}")
