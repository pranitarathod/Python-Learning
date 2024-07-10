s1 = "Pranita Rathod        "
s2 = "pranita rathod"

print(s1)
s1 = s1.rstrip()
print(s1)

if s1.lower == s2.lower:
    print("name correct")

else:
    print("name incorret")