city_name = ("pune","mumbai","solapur", "latur","dhule")

for city in city_name:
    print(city)

    #or


city_name= ("pune","mumbai","solapur", "latur","dhule")
for city_index, city in enumerate(city_name):
    print(city, city_index)