# ============================================Exercise 1=========================================

cars = 100 #the line creates integer value. Value presents cars amount.
space_in_a_car = 4.0 ##the line creates integer value. Value presents car's capacity.
drivers = 30 #the line creates integer value. Value presents amount of drivers.
passengers = 90 #the line creates integer value. Value presents amount of passengers.
cars_not_driven = cars - drivers #the line calculates integer value. Value present amount of cars without driver.
cars_driven = drivers #the line calculates integer value. Value presents how many cars can be driven.
carpool_capacity = cars_driven * space_in_a_car #the line calculates integer value. Value prenets how many passengers can be transpored.
average_passengers_per_car = passengers / cars_driven #the line calculates integer value. Value presents average amount of passengers in one car.


print(f"There are {cars} cars available.")
print(f"There are only {drivers} drivers available.")
print(f"There will be {cars_not_driven} empty cars today.")
print(f"We can transport {carpool_capacity} people today.")
print(f"We have {passengers} to carpool today.")
print(f"We need to put about {average_passengers_per_car} in each car.")

# ============================================Exercise 2=========================================

age = input("How old are you? ") #programm will be waiting user's string value.
print("You are {} years old".format(age)) #programm will return formatted string with the user's value.
