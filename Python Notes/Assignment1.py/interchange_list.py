# interchange first and last list


def swapList(sl):
    sl[0], sl[-1] = sl[-1], sl[0]
    return sl

List = [5,6,7,3,8,9,13,12,23]
print(List)
print("Swapped List: ",swapList(List))

