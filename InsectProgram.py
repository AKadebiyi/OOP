import InsectClass as i


# my_insect = i.Insect()
bug1 = i.Insect('mosquito', 2, 4)
bug2 = i.Insect('housefly', 4, 8)

bug1.length_of_flight()
bug2.length_of_flight()

print(f"The {bug1.get_name()} has {bug1.get_flight()}miles of flight")
print(f"The {bug2.get_name()} has {bug2.get_flight()}miles of flight")
