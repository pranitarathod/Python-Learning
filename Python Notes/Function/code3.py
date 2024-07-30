def find_max(no1,no2,no3):
    if no1 > no2 and no1 > no3:
        print(f"{no1} is max")

    if no2 > no3 and no2 > no1:
        print(f"{no2} is max")

    if no3 > no2 and no3 > no1:
        print(f"{no3} is max")

find_max(23,54,67)
find_max(12,34,68)
find_max(32,45,87)
