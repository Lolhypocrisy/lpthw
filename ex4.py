#num of cars
cars = 100
#number of people in a car
space_in_a_car = 4
#num of drivers
drivers = 30
#num of passengers
passengers = 90
#calculate cars not driven
cars_not_driven = cars - drivers
#assign cars driven
cars_driven = drivers
#determine carpool_capacity
carpool_capacity = cars_driven * space_in_a_car
#compute average passengers
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available")
print("There are only", drivers, "available")
print("There will be", cars_not_driven, "empty cars today")
print("We can transport", carpool_capacity, "people today")
print("We have", passengers, "to carpool today")
print("We need to put about", average_passengers_per_car,
      "in each car.")
