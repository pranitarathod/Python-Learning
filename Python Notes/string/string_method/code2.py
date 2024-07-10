s1 = "           virat kohli"
s2 = "virat kohli"

print(s1)

s1 = s1.lstrip()

print(s1)

if s1.lower() == s2.lower(): # True
    print("Both are same")
else:
    print("Both are not same.")